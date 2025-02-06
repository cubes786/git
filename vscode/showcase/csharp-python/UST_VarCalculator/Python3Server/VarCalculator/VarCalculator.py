import pyodbc
import pandas as pd
import numpy as np
import re
import json
from decimal import Decimal, getcontext
from scipy.stats import norm


class VarCalculator:
    def __init__(self):
       with open('VarCalculatorConfig.json') as f:
            data = json.load(f)
       self.connection_string = data['connection_string']
       self.instruments = set(data['instruments'])
       self.start_date = data['start_date']
       self.end_date = data['end_date']
       self.yields_df=pd.DataFrame()
    
    def get_instruments_data(self, start_date, end_date):
        def merge_dataframes(dfs):
            merged_df = pd.DataFrame()    
            for instrument, df in dfs.items():        
                df.rename(columns={'Yield': f'{instrument}_Yield'}, inplace=True)
        
                if merged_df.empty:
                    merged_df = df
                else:
                    merged_df = pd.merge(merged_df, df, left_index=True, right_index=True, how='outer')
    
            return merged_df

        instrument_data = {}
        
        for instrument in self.instruments:
            df = self.get_yield_data_from_db(instrument, start_date, end_date)
        
            # Store the DataFrame in the instrument_data dictionary
            instrument_data[instrument] = df
        yields_df=merge_dataframes(instrument_data)    

        return yields_df

    def GetInstrumentList(self):
        return self.instruments
    
    def GetYields(self):      
        if self.yields_df.empty:
            self.yields_df = self.get_instruments_data(self.start_date, self.end_date)

        # Return a clone of yields_df
        return self.yields_df.copy()

    def CalculatePortfolioYield(self, weights):
        df = self.GetYields()

        df['Portfolio_Yield'] = 0
        for instrument, weight in weights.items():        
            df['Portfolio_Yield'] += df[f'{instrument}_Yield'] * weight

        df['Portfolio_Delta_Yield'] = df['Portfolio_Yield'].diff()
        
        # Backward fill NaN values --TODO: this is needed to replace initial NAN with first non NAN val - causes issue on JSON translation
        df['Portfolio_Delta_Yield'] = df['Portfolio_Delta_Yield'].bfill()

        return df

    def CalculateVar_HistoricalSimulation(self, weights, confidence_level):
        df = self.CalculatePortfolioYield(weights)
        
        if 'Portfolio_Return' not in df.columns:
            df['Portfolio_Return'] = df['Portfolio_Yield'].pct_change()
    
        df = df.dropna()
    
        # Sort in ascending order
        sorted_returns = df['Portfolio_Return'].sort_values()
    
        index = int((1 - confidence_level) * len(sorted_returns))
    
        # Find the VaR at the desired confidence level
        var = sorted_returns.iloc[index]
    
        return var

    def CalculateDV01(self):
        # Set the precision
        getcontext().prec = 10
    
        df = self.GetYields()
        yield_columns = [col for col in df.columns if 'W_Yield' in col]

        for yield_col in yield_columns:
            N = int(re.search(r'(\d+)W_Yield', yield_col).group(1))

            T = Decimal(N / 52)

            dv01_col = yield_col.replace('Yield', 'DV01')
            
            df[dv01_col] = df[yield_col].apply(lambda y: float((T / (100 * (1 + y / 2) ** (2 * T + 1)))))

        return df

    def CalculateVar_Parametric(self, weights, confidence_level):
        df = self.CalculatePortfolioYield(weights)
        
        if 'Portfolio_Return' not in df.columns:
            df['Portfolio_Return'] = df['Portfolio_Yield'].pct_change()
        df['Portfolio_Return'] = df['Portfolio_Return'].astype(float)    
    
        df = df.dropna()
    
        mean = df['Portfolio_Return'].mean()
        std_dev = df['Portfolio_Return'].std()
    
        z_score = norm.ppf(confidence_level)
    
        var = mean - z_score * std_dev
    
        return var

    def get_yield_data_from_db(self, instrument, start_date, end_date):
        def fill_missing_dates(df, start_date, end_date):    
            # Create a new dataframe with a continuous date range
            new_index = pd.date_range(start=start_date, end=end_date)
            df_new = df.reindex(new_index)
    
            pd.set_option('future.no_silent_downcasting', True)
            # Forward fill NaN values
            df_new['Yield'] = df_new['Yield'].ffill()

            # Backward fill NaN values
            df_new['Yield'] = df_new['Yield'].bfill()
    
            return df_new        


        conn = pyodbc.connect(self.connection_string)    
        cursor = conn.cursor()
    
        # Execute the stored procedure
        cursor.execute("EXEC dbo.GetYieldData @Values = ?, @StartDate = ?, @EndDate = ?", instrument, start_date, end_date)
    
        rows = cursor.fetchall()
    
        columns = [column[0] for column in cursor.description]
    
        # Convert the rows to a pandas DataFrame
        df = pd.DataFrame.from_records(rows, columns=columns)
        df['Date'] = pd.to_datetime(df['Date'])
    
        df.set_index('Date', inplace=True)
    
        cursor.close()
        conn.close()
    
        df_with_missing_dates=fill_missing_dates(df, start_date, end_date)

        return df_with_missing_dates

    
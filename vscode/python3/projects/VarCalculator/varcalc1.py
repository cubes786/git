import pyodbc
import pandas as pd

def GetYieldData(instrument, start_date, end_date, connection_string):
    # Create a new connection
    conn = pyodbc.connect(connection_string)
    
    # Create a new cursor from the connection
    cursor = conn.cursor()
    
    # Execute the stored procedure
    cursor.execute("EXEC dbo.GetYieldData @Values = ?, @StartDate = ?, @EndDate = ?", instrument, start_date, end_date)
    
    # Fetch all rows from the last executed statement
    rows = cursor.fetchall()
    
    # Get the column names from the cursor description
    columns = [column[0] for column in cursor.description]
    
    # Convert the rows to a pandas DataFrame
    df = pd.DataFrame.from_records(rows, columns=columns)
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return df
connection_string=r"Data Source=(local)\SQLEXPRESS;Initial Catalog=AdventureWorksLT2022;Integrated Security=True"
pd=GetYieldData("4W", "2022-04-18", "2022-05-18", connection_string)
print(pd)
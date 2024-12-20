from datetime import datetime

def date_to_year_quarter(dates):
    # Function to determine the quarter
    def get_quarter(date):
        month = date.month
        if 1 <= month <= 3:
            return 'Q1'
        elif 4 <= month <= 6:
            return 'Q2'
        elif 7 <= month <= 9:
            return 'Q3'
        elif 10 <= month <= 12:
            return 'Q4'

    # List to store the results
    year_quarter_list = []

    for date_str in dates:
        # Convert the string to a datetime object
        date = datetime.strptime(date_str, '%Y-%m-%d')
        # Get the year and quarter
        year = date.year
        quarter = get_quarter(date)
        # Combine into the desired format
        year_quarter_list.append(f'{year}{quarter}')

    return year_quarter_list

# Example usage
dates = ['2013-03-01', '2034-10-22']
result = date_to_year_quarter(dates)
print(result)

"""
This script reads the IBRD historical data to extract a mapping of country to country code.
"""
import pandas
df=pandas.read_csv('IBRD_Statement_Of_Loans_-_Historical_Data.csv')
country_name_code = df[['Country Code','Country']].drop_duplicates()
country_name_code.to_csv('country_code_to_name.csv')

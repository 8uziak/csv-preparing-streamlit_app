import streamlit 
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("The process of preparing the data for use ")
streamlit.header("(cleaning CSV table)")

streamlit.text("columns are split incorrectly, commas should be used, not semicolons")
streamlit.text("there are 1 column and 160735 rows in the table now, there should be 3 rows ")
streamlit.text("after the columns are split")
df = pd.read_csv("https://raw.githubusercontent.com/8uziak/Python-Panda-Library/main/cleaning%20CSV%20table/BCL_TaskCreation.csv") 
streamlit.dataframe(df) 

streamlit.text("I used a delimiter to properly separate the columns")
streamlit.text("now table has 3 columns with headers dataStream, rowCount and probingTimestamp")
df = pd.read_csv('https://raw.githubusercontent.com/8uziak/Python-Panda-Library/main/cleaning%20CSV%20table/BCL_TaskCreation.csv',delimiter=';')
streamlit.dataframe(df) 

streamlit.text("I split the probingTimestamp column containing date and time together into")
streamlit.text("two separate columns: 'Date' and 'Time'")
streamlit.text("I removed the original column (probingTimestamp) to avoid repeating the same data")
streamlit.text("table has 4 columns and 160735 rows")
df[['Date','Time']] = df['probingTimestamp'].str.split(' ', expand=True)
df.drop('probingTimestamp', inplace=True, axis=1)
streamlit.dataframe(df)

streamlit.text("I checked to see if it was worth leaving the 'dataStream' column")
streamlit.text("I used a function to check the number of unique values in a cell")
streamlit.text("the output told me that the cell named 'BCL_TaskCreation' repeats 160734 times")
streamlit.text("so from the beginning (without header of course) to the last index the cells are the same")
df['dataStream'].unique()
streamlit.dataframe(df)

streamlit.text("I decided to remove the 'dataStream' column due to its worthless nature in this table")
df.drop('dataStream', inplace=True, axis=1)
streamlit.dataframe(df)

streamlit.text("there is no specific hourly time, from the beginning of the day to the end of the day ")
df.sort_values(by=['Time'], inplace=True)
streamlit.dataframe(df)

streamlit.text("I noticed that the data in the table is not sorted in any way")
streamlit.text("you can see above in the 'Date' column in rows 1, 2 and 3 that the dates are not in sequence")
streamlit.text("I came to the conclusion to sort the table by cells from the earliest date to the oldest")
streamlit.text("and from earliest time to latest time")
df.sort_values(by=['Date','Time'], inplace=True)
streamlit.dataframe(df)

streamlit.text("I corrected the row names so that the indexing is from zero upwards")
df.index = range(0,160735) 
streamlit.dataframe(df)

streamlit.text("I checked that each date has a unique value from the 'rowCount' column and from analyzing")
streamlit.text("of the following output that the rowCount value is not specified for a particular date")
df.groupby(['rowCount', 'Date']).size()
streamlit.dataframe(df)

streamlit.text("the values in the rowCount column are assigned to each day in the closed interval ")
streamlit.text("from 2020-01-10 to 2020-05-02")
df['Date'].unique()
streamlit.dataframe(df)

streamlit.text("SUMMARY")
streamlit.text("The task solved by Mateusz Buziak - github.com/8uziak")
streamlit.text("table after cleaning has 3 columns and 160735 rows")
streamlit.text("What I did with the table itself:")
streamlit.text("- I split the columns from the incorrectly saved csv file, ")
streamlit.text("- split the probingTimestamp column into 2 other columns and deleted the probingTimestamp column, ")
streamlit.text("deleted the dataStream column,")
streamlit.text("- I sorted the rows from the smallest values (priority) Date and Time from the smallest")
streamlit.text("value to the highest value, ")
streamlit.text("- I fixed the indexing of all rows after sorting.")

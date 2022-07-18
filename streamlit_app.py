import streamlit 
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("The process of preparing the data for use ")
streamlit.header("(cleaning CSV table)")

streamlit.markdown("Columns are split incorrectly, commas should be used, not semicolons. There are 1 column and 160735 rows in the table now, \
    there should be 3 rows after the columns are split")
df = pd.read_csv("https://raw.githubusercontent.com/8uziak/Python-Panda-Library/main/cleaning%20CSV%20table/BCL_TaskCreation.csv") 
streamlit.dataframe(df) 

streamlit.markdown("I used a delimiter to properly separate the columns, now table has 3 columns with headers dataStream, rowCount and probingTimestamp")
df = pd.read_csv('https://raw.githubusercontent.com/8uziak/Python-Panda-Library/main/cleaning%20CSV%20table/BCL_TaskCreation.csv',delimiter=';')
streamlit.dataframe(df) 

streamlit.markdown("I split the probingTimestamp column containing date and time together into two separate columns: 'Date' and 'Time'. \
    I removed the original column (probingTimestamp) to avoid repeating the same data table has 4 columns and 160735 rows")
df[['Date','Time']] = df['probingTimestamp'].str.split(' ', expand=True)
df.drop('probingTimestamp', inplace=True, axis=1)
streamlit.dataframe(df)

streamlit.markdown("I checked to see if it was worth leaving the 'dataStream' column. I used a function to check the number \
    of unique values in a cell the output told me that the cell named 'BCL_TaskCreation' repeats 160734 times \
        so from the beginning (without header of course) to the last index the cells are the same")
df['dataStream'].unique()
streamlit.dataframe(df)

streamlit.markdown("I decided to remove the 'dataStream' column due to its worthless nature in this table")
df.drop('dataStream', inplace=True, axis=1)
streamlit.dataframe(df)

streamlit.markdown("there is no specific hourly time, from the beginning of the day to the end of the day ")
df.sort_values(by=['Time'], inplace=True)
streamlit.dataframe(df)

streamlit.markdown("I noticed that the data in the table is not sorted in any way. You can see above in the 'Date' column in rows 1, 2 and 3 that the dates are not in sequence. \
    I came to the conclusion to sort the table by cells from the earliest date to the oldest and from earliest time to latest time")
df.sort_values(by=['Date','Time'], inplace=True)
streamlit.dataframe(df)

streamlit.markdown("I corrected the row names so that the indexing is from zero upwards")
df.index = range(0,160735) 
streamlit.dataframe(df)

streamlit.markdown("I checked that each date has a unique value from the 'rowCount' column and from analyzing \
    of the following output that the rowCount value is not specified for a particular date")
df.groupby(['rowCount', 'Date']).size()
streamlit.dataframe(df)

streamlit.markdown("the values in the rowCount column are assigned to each day in the closed interval from 2020-01-10 to 2020-05-02")
df['Date'].unique()
streamlit.dataframe(df)

streamlit.header("SUMMARY")
streamlit.markdown("Table after cleaning has 3 columns and 160735 rows")
streamlit.markdown("What I did with the table itself:")
streamlit.markdown("- I split the columns from the incorrectly saved csv file,")
streamlit.markdown("- split the probingTimestamp column into 2 other columns and deleted the probingTimestamp column,")
streamlit.markdown("- I sorted the rows from the smallest values (priority) Date and Time from the smallest value to the highest value,")
streamlit.markdown("- I fixed the indexing of all rows after sorting.")
streamlit.markdown("The task solved by Mateusz Buziak - github.com/8uziak")

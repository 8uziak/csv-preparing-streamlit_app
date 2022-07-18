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


df = pd.read_csv('https://raw.githubusercontent.com/8uziak/Python-Panda-Library/main/cleaning%20CSV%20table/BCL_TaskCreation.csv',delimiter=';')
streamlit.dataframe(df) 

streamlit.text("!")
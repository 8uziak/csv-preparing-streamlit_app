import streamlit 
import pandas as pd
import requests
import snowflake.connector

streamlit.title("Hello World")
streamlit.header("Pancakes recipe")
streamlit.text("1 cup of milk")
streamlit.text("3 table spoons of ...")
streamlit.text("test test test")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),["Avocado","Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show) 

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')

streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

fruits_choice = streamlit.text_input('What fruit would you like information about?','Banana')
streamlit.write('The user entered ', fruits_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruits_choice)
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("wybieraj!!!")
streamlit.dataframe(my_data_rows)

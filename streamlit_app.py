import streamlit 
import pandas as pd

streamlit.title("Hello World")
streamlit.header("Pancakes recipe")
streamlit.text("1 cup of milk")
streamlit.text("3 table spoons of ...")
streamlit.text("test test test")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list) 


import streamlit 
import pandas as pd

streamlit.title("Hello World")
streamlit.header("Pancakes recipe")
streamlit.text("1 cup of milk")
streamlit.text("3 table spoons of ...")
streamlit.text("test test test")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
streamlit.dataframe(fruit_list) 


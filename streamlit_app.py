import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & BlueBerry Oatmeal')
streamlit.text('🥗 Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocodo Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
#New request to display fruity vice api response
#New section to Display Fruitvise API Response
streamlit.header("Fruityvise Fruit Advice!")
fruit_choice=streamlit.text_input('What Fruit would you like information about?','KIWI')
streamlit.write('the use entered',fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
##streamlit.text(fruityvice_response.json()) #just writes the jason data on the screen
#Take the json version of the response and normalise it
fruityvice_normalised=pandas.json_normalize(fruityvice_response.json())
#output it to the screen as Table
streamlit.dataframe(fruityvice_normalised)


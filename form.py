import streamlit as st
import data

st.title("Films")
name = st.text_input("Film name:")
year = st.number_input("Film year:", min_value=2010, max_value=2025)
note = st.slider("Film note:", min_value=0.0, max_value=10.0)

if st.button('Add'):
    data.insert_data(name, year, note)
    st.success('Registered film!')

films = data.data_obtain()
st.header("Films list")
st.table(films)

import streamlit as st
import functions

todos = functions.get_todos()

st.title("My To Do App")
st.subheader("This is my todo App")
st.write("Learning streamlit")
for todo in todos:
    st.checkbox(todo)

st.text_input(label="New To Do",placeholder="Add new To Do",label_visibility='hidden')
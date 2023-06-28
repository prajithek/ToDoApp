import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    functions.write_todos(new_todo+"\n")
    st.session_state.new_todo = ''





st.title("My To Do App")
st.subheader("This is my todo App")
st.write("Learning streamlit")
for todo in todos:
    st.checkbox(todo,key=todo+"1")

st.text_input(label="New To Do",placeholder="Add new To Do",label_visibility='hidden',on_change=add_todo,key="new_todo")
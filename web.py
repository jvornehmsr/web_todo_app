import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    st.session_state['new_todo'] = ''
    todos = functions.get_todos()
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my Todo app.")
st.write("This app is intended to improve your productivity.")

for index, todo in enumerate(todos):
    st.checkbox(todo, key=todo)
    if st.session_state[todo]:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

import streamlit as st
import functions

todos= functions.get_todos()
def new_todo():
    todo = st.session_state['new_todo']+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Web App")
st.subheader("Massive Productivity Improvement Tool")
todos = functions.get_todos()

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder='Enter a New Todo',
              on_change=new_todo, key='new_todo')

#st.session_state
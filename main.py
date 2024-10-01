import streamlit as st

st.title('This is text')

st.write('This is a **text** :books')

st.buttin('Reset', type='primary')
if st.buttin('say Hello'):
  st.write('Hello There')
else:
  st.write('goodbye')
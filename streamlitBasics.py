# imports
import pandas as pd
import streamlit as st

# Texts in Streamlit
st.image('flowers.jpg', caption = "nature")
st.text(' <h1>HELLO WORLD </h1>')
# tx = st.text_area(label='Enter text')
s_1 = st.text_input(label='Enter your 1st Input')
st.write(':+:')
s_2 = st.text_input(label='Enter your 2nd Input')

# Buttons in streamlit

button = st.button(label='Add',key='ta')
if button:
    try:
        st.write(f'{float(s_2) + float(s_1)}')
    except:
        st.toast('Please enter numbers only', icon=":material/thumb_up:")

    # st.button(label='Click me')



# Dataframe in streamlit

data = {'First':[1,11,111],'Second':[2,22,222],}

st.dataframe(pd.DataFrame(data))
import streamlit as st
import pandas as pd
# st.set_page_config(layout= 'wide')

data = {
    'name': [1,2,3,4,5,6],
    'place': ['CA', 'NV', 'WS', 'NY', 'OR', 'ZL'],
    'age': [13,14,15,16,17,18],
    'description': ['good', 'bad', 'mid', 'unkown', 'very good', 'zebra']
}

df = pd.DataFrame(data = data)

# st.dataframe(df)

if "df" not in st.session_state:
    st.session_state.df = df

st.dataframe(df.style.highlight_max(axis = 0))
event = st.dataframe(st.session_state.df, on_select = 'rerun', key = 'data', selection_mode = ['multi-row', 'multi-column'])
event.selection
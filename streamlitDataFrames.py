import streamlit as st
import pandas as pd
# st.set_page_config(layout= 'wide')

data = {
    'name': [1,2,3,4,5],
    'place': ['CA', 'NV', 'WS', 'NY', 'OR'],
    'age': [13,14,15,16,17],
    'description': ['good', 'bad', 'mid', 'unkown', 'very good']
}

df = pd.DataFrame(data = data)

# st.dataframe(df)

if "df" not in st.session_state:
    st.session_state.df = df

event = st.dataframe(st.session_state.df, st.session_state.df.style.highlight_max(axis=0), on_select = 'rerun', key = 'data', selection_mode = ['multi-row', 'multi-column'])
event.selection
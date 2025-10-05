import streamlit as st
import pandas as pd

data = {
    'num_1': [1,2,4],
    'num_2': [6,7,8],
}

def callback():
    # if 'key_1' not in st.session_state:
        # st.session_state.df = df
    edf = st.session_state['key_1']
    print(edf['edited_rows'])
    # edf['add'] = edf.apply(lambda x: x['num_1'] + x['num_2'], axis = 1)
    # st.session_state.df = edf

df = pd.DataFrame(data=data)
df['add'] = df.apply(lambda x: x['num_1'] + x['num_2'], axis = 1)
editordf = st.data_editor(df, key = 'key_1', on_change = callback)
# df['add'] = editordf['add']
print(editordf)
import streamlit as st

st.title("Unit converter (Lbs, Kg)")

# st.session_state

# Callback functions
def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs / 2.2046

def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg * 2.2046

st.number_input('Pounds', key = 'lbs', on_change = lbs_to_kg)
st.number_input('Kilograms', key = 'kg', on_change = kg_to_lbs)     
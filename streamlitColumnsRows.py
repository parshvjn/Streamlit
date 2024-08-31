import streamlit as st
import numpy as np
st.set_page_config(layout = 'wide')

# col1, col2, col3 = st.columns(3, vertical_alignment = 'bottom')
# col1.subheader('First Column')
# col2.subheader('Second Column')
# col1.text_input('Enter text')
# col2.button(label = 'Click me')
# col3.line_chart(np.random.randn(10,1))
# row1, row2 = st.columns(3), st.columns(3)
# rows = row1 + row2
# # contain = rows[i].container()
# for i, col in enumerate(rows):
#     contain = rows[1].container()
#     contain.write("ABC")
    # contain.image('flowers.jpg')
    # contain[i]

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
cols = [col1, col2, col3, col4, col5, col6]
# with st.container():
#     col1.title('column 1 first image')
#     col2.write('column 2')
#     col3.write('column 3')
#     col1.image('flowers.jpg')

# with st.container():
#     col4.write('column 4')
#     col5.write('column 5')
#     col6.write('column 6')

#hw: try looping this as if there were many columns to do

for ind, col in enumerate(cols):
    with st.container():
        col.write(f'column {ind+1}')

#hw try to import different sets of images and make new repo for streamlit files
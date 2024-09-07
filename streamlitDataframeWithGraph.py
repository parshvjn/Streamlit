import streamlit as st
import pandas as pd
import numpy as np
import random

data = {
    'name': ['William', 'John', 'Sam', 'Smith', 'Parshv'],
    'url': ['https://github.com/parshvjn/Introduction-to-AI', 'https://github.com/parshvjn/EmailSpamClassification', 'https://github.com/parshvjn/DataScience-Pandas', 'https://github.com/parshvjn/Streamlit', 'https://github.com/parshvjn/Smart-Folder'],
    'chart': [[random.randint(0, 5000) for _ in range(30)] for _ in range(5)]
}

# st.dataframe(pd.DataFrame(data))
dataframe = pd.DataFrame(data)
st.dataframe(dataframe, column_config={'url': st.column_config.LinkColumn('github url', help = 'github repositories url'),
                                       'chart': st.column_config.BarChartColumn('charts')}, hide_index = True)
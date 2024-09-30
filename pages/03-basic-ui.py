import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

#버튼 클릭
button = st.button('버튼을 눌러보세요')
if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')

dataframe = pd.DataFrame({
    'first column': ['kor','eng',math','science'],
    'second column': [10, 20, 30, 40]
})
st.download_button(
    label='CSV로 성적표 다운로드',
    data=dataframe.to_csv(),
    file_name='sample.csv',
    mine='text/csv'
)

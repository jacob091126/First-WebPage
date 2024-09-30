import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

#버튼 클릭
button = st.button('버튼을 눌러보세요')
if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')
# 지정한 범위 내에서 랜덤 정수 생성 (1 이상 10 이하)
random_int = random.randint(0, 100)
print(random_int)

dataframe = pd.DataFrame({
    'first column': ['kor','eng','math','science'],
    'second column': [print(random_int), print(random_int), print(random_int), print(random_int)]
})
st.download_button(
    label='CSV로 석훈이의 성적표 다운로드',
    data=dataframe.to_csv(),
    file_name='sample.csv',
    mime='text/csv'
)

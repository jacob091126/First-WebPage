import streamlit as st
st.title("My first web service!")
name=st.text_input("이름을 입력해주세요")
menu=st.selectbox("좋아하는 음식을 선택!",['회','피자','치킨','베라'])
if st. button("인사말 생성"):
    st.write(name+"님! 당신이 좋아하는 음식은 "+menu+"이군요! 저도 좋아요!")

import streamlit as st

st.set_page_config(page_title="Skills",layout="wide")

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

.stButton>button{
width:100%;
height:50px;
font-size:18px;
border-radius:12px;
background:#00C9FF;
color:white;
}

</style>
""",unsafe_allow_html=True)

st.title("⚡ Skills")

st.subheader("Python")
st.progress(95)

st.subheader("HTML")
st.progress(90)

st.subheader("CSS")
st.progress(90)

st.subheader("JavaScript")
st.progress(85)

st.subheader("React")
st.progress(80)

st.write("")

col1,col2,col3=st.columns(3)

with col1:
    if st.button("⬅ Projects"):
        st.switch_page("pages/projects.py")

with col2:
    if st.button("🏠 Home"):
        st.switch_page("home.py")

with col3:
    if st.button("➡ Hobbies"):
        st.switch_page("pages/hobbies.py")
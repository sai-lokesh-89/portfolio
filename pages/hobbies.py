import streamlit as st

st.set_page_config(
    page_title="Hobbies",
    page_icon="🎯",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb,#06b6d4);
background-size:400% 400%;
animation:bg 15s ease infinite;
}

@keyframes bg{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.title{
text-align:center;
font-size:55px;
font-weight:800;
color:white;
margin-bottom:5px;
}

.subtitle{
text-align:center;
font-size:20px;
color:#e5e7eb;
margin-bottom:40px;
}

.card{
background:rgba(255,255,255,0.10);
backdrop-filter:blur(12px);
padding:30px;
border-radius:25px;
border:1px solid rgba(255,255,255,0.20);
box-shadow:0px 15px 35px rgba(0,0,0,.35);
transition:.4s;
height:250px;
text-align:center;
}

.card:hover{
transform:translateY(-10px) scale(1.02);
box-shadow:0px 20px 40px rgba(0,255,255,.30);
}

.icon{
font-size:55px;
margin-bottom:15px;
}

.heading{
font-size:25px;
font-weight:bold;
color:#38bdf8;
margin-bottom:10px;
}

.text{
font-size:17px;
color:#f8fafc;
line-height:1.7;
}

.stButton>button{
width:100%;
height:55px;
border:none;
border-radius:40px;
font-size:18px;
font-weight:bold;
color:white;
background:linear-gradient(90deg,#3b82f6,#06b6d4);
transition:.3s;
}

.stButton>button:hover{
background:linear-gradient(90deg,#ff512f,#dd2476);
transform:scale(1.04);
}

.footer{
text-align:center;
font-size:18px;
color:white;
margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🎯 My Hobbies</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Things I enjoy doing beyond coding.</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:

    st.markdown("""
    <div class="card">
        <div class="icon">💻</div>
        <div class="heading">Coding</div>
        <div class="text">
        I enjoy building websites, solving programming problems, and learning new technologies through hands-on projects.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="card">
        <div class="icon">📚</div>
        <div class="heading">Learning</div>
        <div class="text">
        I love exploring AI, Machine Learning, Web Development, and modern software technologies.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">
        <div class="icon">🎵</div>
        <div class="heading">Music</div>
        <div class="text">
        Listening to music helps me stay focused, relaxed, and productive while working on projects.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="card">
        <div class="icon">🎮</div>
        <div class="heading">Gaming</div>
        <div class="text">
        I enjoy playing strategy and puzzle games that improve logical thinking and decision-making.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='footer'>✨ Thanks for visiting my portfolio! ✨</div>", unsafe_allow_html=True)

st.write("")
st.write("")

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Skills"):
        st.switch_page("pages/skills.py")

with col2:
    if st.button("🏠 Home"):
        st.switch_page("home.py")
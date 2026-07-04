import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sai Lokesh | Portfolio",
    page_icon="💻",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.title{
    font-size:55px;
    font-weight:bold;
    color:#0F172A;
}

.subtitle{
    font-size:25px;
    color:#2563EB;
    font-weight:600;
}

.description{
    font-size:18px;
    color:#555;
}

.skill-box{
    background-color:#EEF4FF;
    padding:15px;
    border-radius:12px;
    text-align:center;
    font-weight:bold;
    color:#1E3A8A;
    margin-bottom:10px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:60px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------

col1, col2 = st.columns([2,1])

with col1:

    st.markdown('<p class="title">Hi 👋</p>', unsafe_allow_html=True)

    st.markdown(
        '<p class="title">I\'m Sai Lokesh</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Aspiring Data Scientist | Python Developer | AI Enthusiast</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class="description">
        Welcome to my personal portfolio website.
        I'm passionate about Data Science, Machine Learning,
        Artificial Intelligence, and Python development.
        I enjoy solving real-world problems by building intelligent applications
        and continuously learning new technologies.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.download_button(
        "📄 Download Resume",
        data="Upload your resume here later",
        file_name="Lokesh_Resume.pdf"
    )

with col2:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=260
    )

st.write("")
st.write("---")

# ---------------- ABOUT ----------------

st.header("🙋 About Me")

st.write("""
I am a Computer Science student interested in:

- Data Science
- Machine Learning
- Deep Learning
- Python Development
- Artificial Intelligence

I enjoy building projects that combine data analysis, automation,
and intelligent systems.
""")

st.write("---")

# ---------------- SKILLS ----------------

st.header("💻 Technical Skills")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="skill-box">Python</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-box">NumPy</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-box">Pandas</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="skill-box">Machine Learning</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-box">Scikit-Learn</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-box">TensorFlow</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="skill-box">SQL</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-box">MySQL</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-box">Git</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="skill-box">Streamlit</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-box">OpenCV</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-box">Power BI</div>', unsafe_allow_html=True)

st.write("---")

# ---------------- STATS ----------------

st.header("📈 Highlights")

c1, c2, c3 = st.columns(3)

c1.metric("Projects", "10+")
c2.metric("Technologies", "15+")
c3.metric("Learning", "AI & Data Science")

st.write("---")

# ---------------- CONTACT ----------------

st.header("📬 Connect With Me")

st.write("📧 Email: sailokeshvelugoti@gmail.com")
st.write("💼 LinkedIn: https://linkedin.com/in/yourprofile")
st.write("💻 GitHub: https://github.com/yourusername")

st.markdown(
    '<p class="footer">Made with ❤️ using Streamlit</p>',
    unsafe_allow_html=True
)
import streamlit as st

st.set_page_config(
    page_title="Portfolio",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(-45deg,#020617,#1e1b4b,#312e81,#0f172a);
background-size:400% 400%;
animation:gradient 12s ease infinite;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.main{

padding-top:50px;
padding-bottom:30px;

}

.name{

font-size:72px;

font-weight:900;

color:white;

text-shadow:0px 0px 20px #38bdf8;

margin-top:30px;

}

.role{

font-size:26px;

font-weight:600;

color:#38bdf8;

margin-top:-5px;

margin-bottom:25px;

}

.about{

background:rgba(255,255,255,.08);

padding:30px;

border-radius:20px;

border:1px solid rgba(255,255,255,.15);

backdrop-filter:blur(12px);

color:white;

font-size:18px;

line-height:1.9;

box-shadow:0px 10px 30px rgba(0,0,0,.25);

}
            
.metric{

background:rgba(255,255,255,.08);

padding:25px;

border-radius:20px;

text-align:center;

margin-top:20px;

border:1px solid rgba(255,255,255,.15);

transition:.4s;

}

.metric:hover{

transform:translateY(-8px);

box-shadow:0px 15px 30px rgba(59,130,246,.4);

}

.metric h1{

color:#38bdf8;

font-size:40px;

margin-bottom:5px;

}

.metric p{

color:white;

font-size:18px;

}

.nav{

background:rgba(255,255,255,.08);

padding:25px;

border-radius:20px;

text-align:center;

border:1px solid rgba(255,255,255,.15);

transition:.4s;

height:180px;

}

.nav:hover{

transform:scale(1.04);

box-shadow:0px 15px 35px rgba(6,182,212,.4);

}

.nav h2{

color:#38bdf8;

}

.nav p{

color:white;

}

.stButton>button{

width:100%;

height:50px;

border:none;

border-radius:40px;

background:linear-gradient(90deg,#3b82f6,#06b6d4);

color:white;

font-size:18px;

font-weight:bold;

}

.stButton>button:hover{

background:linear-gradient(90deg,#ff512f,#dd2476);

}

.footer{

text-align:center;

margin-top:50px;

color:#cbd5e1;

font-size:18px;

}

img{

border-radius:50%;

border:5px solid #38bdf8;

box-shadow:0px 0px 35px #38bdf8;

transition:.4s;

}

img:hover{

transform:scale(1.05);

box-shadow:0px 0px 50px #06b6d4;

}
            
</style>
""", unsafe_allow_html=True)

# ================= HERO SECTION =================

col1, col2 = st.columns([1, 2], gap="large")

with col1:

    st.image(
        "assets/image1.jpeg",
        width=280
    )

    with open("assets/resume.pdf", "rb") as pdf:
        st.download_button(
            label="📄 Download Resume",
            data=pdf,
            file_name="My_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )

with col2:

    st.markdown("""
    <div class='name'>
    SAI LOKESH
    </div>

    <div class='role'>
    🚀 Python Developer • Frontend Developer • Streamlit Enthusiast
    </div>

    <div class='about'>

    <h2>Welcome to My Portfolio </h2>

    I am a passionate <b>Computer Science Graduate</b> who loves creating
    modern web applications using <b>Python</b>, <b>Streamlit</b>,
    <b>React</b>, <b>HTML</b>, <b>CSS</b>, and <b>JavaScript</b>.

    I enjoy solving real-world problems, learning new technologies,
    and designing beautiful user interfaces with an excellent user experience.

    </div>
    """, unsafe_allow_html=True)

m1,m2,m3,m4=st.columns(4)

with m1:
    st.markdown("""
<div class="metric">
<h1>02</h1>
<p>Projects</p>
</div>
""",unsafe_allow_html=True)

with m2:
    st.markdown("""
<div class="metric">
<h1>06+</h1>
<p>Technologies</p>
</div>
""",unsafe_allow_html=True)

with m3:
    st.markdown("""
<div class="metric">
<h1>2026</h1>
<p>Graduate</p>
</div>
""",unsafe_allow_html=True)

with m4:
    st.markdown("""
<div class="metric">
<h1>∞</h1>
<p>Learning</p>
</div>
""",unsafe_allow_html=True)

st.write("")

c1,c2,c3=st.columns(3)

with c1:

    st.markdown("""
<div class="nav">

<h2>💻 Projects</h2>

<p>Explore my Machine Learning and Web Development projects.</p>

</div>
""",unsafe_allow_html=True)

    if st.button("Open Projects"):
        st.switch_page("pages/projects.py")

with c2:

    st.markdown("""
<div class="nav">

<h2>⚡ Skills</h2>

<p>Discover the technologies and programming languages I use.</p>

</div>
""",unsafe_allow_html=True)

    if st.button("Open Skills"):
        st.switch_page("pages/skills.py")

with c3:

    st.markdown("""
<div class="nav">

<h2>🎯 Hobbies</h2>

<p>Learn about my interests beyond programming.</p>

</div>
""",unsafe_allow_html=True)

    if st.button("Open Hobbies"):
        st.switch_page("pages/hobbies.py")

st.markdown("<div class='footer'>✨ Thank you for visiting my portfolio ✨</div>", unsafe_allow_html=True)
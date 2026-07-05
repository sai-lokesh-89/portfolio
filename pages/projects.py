import streamlit as st

st.set_page_config(
    page_title="Projects",
    page_icon="💻",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#1e293b,#334155);
}

/* Title */

.main-title{
text-align:center;
font-size:55px;
font-weight:700;
color:white;
margin-bottom:5px;
}

.sub-title{
text-align:center;
font-size:20px;
color:#d1d5db;
margin-bottom:40px;
}

/* Card */

.project-card{

background:rgba(255,255,255,0.08);
padding:30px;
border-radius:20px;
border:1px solid rgba(255,255,255,.15);
backdrop-filter:blur(10px);

min-height:500px;

box-shadow:0px 10px 25px rgba(0,0,0,.35);

transition:.4s;

}

.project-card:hover{

transform:translateY(-8px);

box-shadow:0px 18px 35px rgba(0,255,255,.25);

}

.project-title{

font-size:28px;
font-weight:bold;
color:#38bdf8;

}

.desc{

color:#f1f5f9;
font-size:17px;
line-height:1.7;

}

.tag{

display:inline-block;

background:#0ea5e9;

padding:8px 15px;

margin:5px;

border-radius:20px;

font-size:14px;

color:white;

font-weight:600;

}

.status{

display:inline-block;

background:#22c55e;

padding:8px 18px;

border-radius:30px;

font-weight:bold;

color:white;

margin-bottom:20px;

}

/* Button */

.stButton>button{

width:100%;
height:55px;

border-radius:40px;

font-size:18px;

font-weight:bold;

background:linear-gradient(90deg,#2563eb,#06b6d4);

color:white;

border:none;

}

.stButton>button:hover{

background:linear-gradient(90deg,#ff512f,#dd2476);

transform:scale(1.03);

}

</style>
""",unsafe_allow_html=True)

st.markdown("<div class='main-title'>💻 My Projects</div>",unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Academic & Personal Projects</div>",unsafe_allow_html=True)

left,right=st.columns(2,gap="large")

with left:

    st.markdown("""
<div class="project-card">

<div class="status">Completed</div>

<div class="project-title">
🛡 Fake Profile Identification & Bot Detection
</div>

<br>

<div class="desc">

Detects fake social media accounts and bots using Machine Learning algorithms.

<b>Key Features</b>

<ul>

<li>Fake Profile Detection</li>

<li>Bot Detection</li>

<li>Machine Learning Model</li>

<li>Data Analysis</li>

<li>Prediction Dashboard</li>

</ul>

<b>Technologies</b>

<br><br>

<span class="tag">Python</span>

<span class="tag">Machine Learning</span>

<span class="tag">Pandas</span>

<span class="tag">Scikit-Learn</span>

<span class="tag">Streamlit</span>

</div>

</div>

""",unsafe_allow_html=True)

with right:

    st.markdown("""
<div class="project-card">

<div class="status">Completed</div>

<div class="project-title">
🌦 Weather Application
</div>

<br>

<div class="desc">

A modern weather application that displays real-time weather information for any city using an API.

<b>Key Features</b>

<ul>

<li>Live Weather Updates</li>

<li>City Search</li>

<li>Temperature</li>

<li>Humidity</li>

<li>Wind Speed</li>

</ul>

<b>Technologies</b>

<br><br>

<span class="tag">Python</span>

<span class="tag">Streamlit</span>

<span class="tag">Weather API</span>

<span class="tag">HTML</span>

<span class="tag">CSS</span>

</div>

</div>

""",unsafe_allow_html=True)

st.write("")
st.write("")

col1,col2=st.columns([1,1])

with col1:
    if st.button("🏠 Home"):
        st.switch_page("home.py")

with col2:
    if st.button("⚡ Next → Skills"):
        st.switch_page("pages/skills.py")
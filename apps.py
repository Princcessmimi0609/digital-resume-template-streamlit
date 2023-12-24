from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "FaJeh.jpg"


# --- GEMERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Anna Yuen"
PAGE_ICON = ":WAVE:"
NAME = "Anna Yuen"
Description = """
Senior Data Analyst, assisting enterprises by support data-driven decision-making.
"""

EMAIL = "annayuen1990@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/c/codingisfun",
    "LinkedIn": "https://www.linkedin.com/in/anna-yuen-651862165/",
    "GitHub": "https//github.com"
}

PROJECTS = {

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(Description)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="applicaiton/octet-stream",
    )
    st.write("✉️",EMAIL)

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """

- ✔️ 7 years experience extracting actionable insights from data
- ✔️ strong hands on experience and knowledge in Python and Excel
- ✔️ Good understandning of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on task
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 🖥️ Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBI, MS Excel, Plotly
- 🗂️ Modeling: Logistic regression, linear regression, decition trees
- 📚 Databases: Postgres, MongoDB, MySQL
""" 
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("👔", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write(
    """
- ➡️ Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives,
and supplied recommendations to boost landing page conversion rate by 38%
- ➡️ Led a team of 4 analysts to brainstorm potential marketing and sales improvements,
and implemented A/B tests to generate 15% more client leads
- ➡️ Redesigned data model throught iterations that imporved predictions by 12%
    """
)


# --- PROJECTS & ACCOMPLISHMENTS ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")




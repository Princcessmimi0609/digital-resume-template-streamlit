from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume-Anna-Yuen.pdf"
profile_pic = current_dir / "assets" / "FaJeh.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Anna Yuen"
PAGE_ICON = "👋"
NAME = "Anna Yuen"
Description = """
Self-directed Learner in Low Code/No code and Data Analytics
"""
EMAIL = "annayuen1990@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCgU34DR4V78p1aMvFFu7Vgw",
    "LinkedIn": "https://www.linkedin.com/in/anna-yuen-651862165?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BGT9t6ZWvRru88reV4qHgiA%3D%3D",
    "GitHub": "https://github.com/Princcessmimi0609"
}
PROJECTS = {
    "🏆Website for Community Organisation": {
        "Link": "https://princcessmimi0609.github.io/farmabbrington/",
        "Description": "- Using HTML 5, CSS 3 and JavaScript"
    },
    
    "🏆Sales Data Analysis": {
        "Link": "https://youtu.be/AQA9vEC3u_I",
        "Description": "- Using Microsoft SQL Server Management consuming data from Dynamic 365"
    },

    "🏆Nominal Account Analysis": {
        "Link": "https://youtu.be/lvUMjgELtqo",
        "Description": "- Power BI reports built consuming data from Dynamic 365 Finance & Accounting Module"
    },

    "🏆PowerApps Company Director": {
        "Link": "https://youtu.be/Q4tD_YmrqiA",
        "Description": "- Using Power Apps built consuming data from Google Sheets"            
        }
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

- ✔️ 10 years experience extracting actionable insights from accounting data
- ✔️ Strong hands-on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team player displaying a strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 🖥️ Programming: Python (Library: pandas, Framework: Streamlit, Flask 3.0), Power Fx, DAX Query, Google Visualization API Query Language, 
      Google Apps Script, JavaScript, SQL, Big Query, HTML and CSS  
- 🖥️ Low-code/No-code: Microsoft Power Platform and Google AppSheet 
- 📊 Data Visualization: PowerBI and MS Excel
- 🗂️ Modeling: Logistic regression, linear regression and decision trees
- 📚 Databases: Dataverse, SharePoint Lists, MySQL 8.0, SQL Server 2022 and Google Sheets (as a database) 
- 📄 Administration: M365 Admin and Google Workspace Admin
""" 
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("👔", "**Accounts Assistant | MTP LTD**")
st.write("08/2023 - 07/2024")
st.write(
    """
- ➡️ Used Microsoft PowerBI and SQL Server Management Studio to redefine and track KPIs surrounding marketing initiatives,
      and supplied recommendations to boost the landing page conversion rate by 38%
- ➡️ Redesigned data model through iterations that improved predictions by 12%
- ➡️ General accounting duties & staff expenses claim
    """
)


# --- PROJECTS & ACCOMPLISHMENTS ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("""---""")
for key, value in PROJECTS.items():
    st.write(f"""
[{key}]({value['Link']})
value['Description']""")


# --- EDUCATION ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- Python (Cisco Networking Academy)
""" 
)


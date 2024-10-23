from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Anna Yuen-CV.pdf"
profile_pic = current_dir / "assets" / "FaJeh.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Anna Yuen"
PAGE_ICON = "👋"
NAME = "Anna Yuen"
Description = """
Self-directed Learner in Data Analytics, Low-code and pro-code
"""
EMAIL = "annayuen1990@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "http://www.youtube.com/@No-codeandLow-code-l2w",
    "LinkedIn": "https://www.linkedin.com/in/anna-yuen-mw",
    "GitHub": "https://github.com/Princcessmimi0609"
}

PROJECTS = {
    "👉 PowerApps for Expenses Management App": {
        "Link": "https://youtu.be/DTncc0WHYWo?si=4AFtOHiicIIfJ-D1",
        "Description": """Developed an Expenses App using Power Apps to streamline expense tracking and approval.
                        It uses AI Builder to extract data from receipts, categorizes expenses (e.g., Meals, IT Hardware),
                        and stores data in SharePoint. The app automates the approval process based on predefined thresholds,
                        sending notifications for timely reviews. A dashboard provides real-time tracking, making expense management
                        more efficient and transparent."""           
        },
    

     "👉 PowerApps for Hotel Booking System": {
          "Link": "",
         "Description": """Developed a Power Apps interface for booking and approval processes, automated notifications and approvals with Power Automate,
                        and integrated SharePoint for data storage and reporting."""  
        },

    

    "👉 Python(Django) for Attendance Record": {
        "Link": "https://github.com/Princcessmimi0609/Django",
        "Description": "Attendance Record for Church"
    },

    
    
    "👉 SQL for Sales Data Analyst": {
        "Link": "https://youtu.be/AQA9vEC3u_I",
        "Description": """This video offers a comprehensive introduction to SQL, covering essential concepts like data retrieval,
                        filtering, and aggregation using SELECT queries. Perfect for beginners, the presentation walks through
                        key SQL commands with examples, helping viewers understand how to manage and manipulate databases effectively."""
    },

    

    "👉 Power BI for Proft & Loss Analyst": {
        "Link": "https://youtu.be/lvUMjgELtqo",
        "Description": """This Power BI dashboard provides a detailed analysis of profit and loss (P&L) by GL account,
                        offering insights into revenue, expenses, and profitability. It allows users to drill down
                        into specific accounts, track performance trends, and analyze variances. With interactive visuals
                        and real-time data integration, it helps streamline financial analysis and decision-making"""
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

# --- Profile Summary ---
st.write("#")
st.subheader("Profile Summary")
st.write(
    """

Self-taught and motivated Power Apps Developer with expertise in low-code application development, automation, and data integration. 
Skilled in building custom apps using Power Apps, automating workflows with Power Automate, and enhancing user experience with AI Builder. 
Proficient in Python and experienced in leveraging tools like SharePoint, SQL, and Google BigQuery to create efficient, scalable business solutions. 
Passionate about problem-solving and streamlining business processes through innovative technology.
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("Skills")
st.write(
     """
- ▪ Power Apps: Custom app development, data integration, UI design
- ▪ Power Automate: Workflow automation, approval processes, task automation
- ▪ AI Builder: Receipt processing, automated document extraction
- ▪ Python: Data analysis, automation scripts, web development (Django)
- ▪ SharePoint: List management, data integration, process automation
- ▪ SQL & Google BigQuery: Data manipulation, reporting, querying
- ▪ Other Tools: Power BI, HTML, CSS, JavaScript, Microsoft SQL Server, MySQL
""" 
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Professional Experience")
st.write("---")

# --- JOB 1
st.write("**Accounts Assistant | Mallinson Television Productions Ltd – Scotland**")
st.write("08/2023 - 07/2024")
st.write(
    """
- ▪ Manage general accounting duties including accounts payable, staff reimbursement and credit card reconciliation.
"""
)

# --- JOB 2
st.write("**Capgemini – Power Apps Presentation Inviteed**")
st.write("26/9/2024")
st.write(
    """
- ▪ Invited to share experiences of transitioning to IT and demonstrate Power Apps solutions developed, 
    such as an Expenses Management System and AI-driven workflows.
- ▪ Showcased expertise in app development, automation with Power Automate, and AI integration using AI Builder.
    """
)


# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, details in PROJECTS.items():
    st.write(f"[{project}]({details['Link']}) - {details['Description']}")


# --- EDUCATION ---
st.write("#")
st.subheader("Education")
st.write(
    """
- ▪ Python (Cisco Networking Academy)
- ▪ Python for Beginners – Cisco Institution
- ▪ Software Development with Python – [Glasgow Clyde College]
""" 
)

# --- Additional Information ---
st.write("#")
st.subheader("Reference")
st.write(
    """
- Available upon request.
""" 
)


import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="Joyan Bhathena - Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Navigation Bar
with st.sidebar:
    selected = option_menu(
        menu_title=None,  # Leave empty to remove the title
        options=["Home", "Resume", "Projects", "Skills", "Contact"],
        icons=["house", "file-text", "list-task", "gear", "envelope"],
        menu_icon="cast",  # Icon for the navigation menu
        default_index=0,  # Default selected menu
    )

# Page Content
if selected == "Home":
    st.title("👨‍💻 Joyan Bhathena")
    st.subheader("About Me")
    st.write("""
    Hi, I'm a passionate Computer Science master's student at IU Berlin, 
    with a focus on data engineering and data analytics. 
    I thrive on learning and delivering high-quality results, as reflected in my past roles 
    as a Digital Analytics Expert and top-performing employee.
    """)

# Resume Section
elif selected == "Resume":
    st.title("Resume")
    # Summary
    st.header("Summary")
    st.write("""
    I bring a unique blend of academic rigor and real-world experience, having honed my skills during nearly 2 years of work 
    in Digital Analytics while pursuing a master's in Computer Science. My exceptional work ethic and commitment to excellence 
    enable me to contribute meaningfully to the rapidly evolving fields of data science and analytics.
    """)

    # Technical Skills
    st.header("Technical Skills")
    st.write("""
    - **Programming Languages**: Python, SQL, JavaScript  
    - **Digital Analytics Tools**: Google Analytics, Google Tag Manager, BigQuery, HubSpot, RudderStack, Matomo Analytics  
    - **Business Intelligence**: Looker Studio, Tableau, Power BI  
    """)

    # Experience
    st.header("Experience")
    st.subheader("Analytics Consultant | DataVinci Analytics Agency (08/2022 – 10/2024)")
    st.write("""
    DataVinci is a digital analytics agency providing analytics as a service.
    - Successfully managed 3 retainer projects generating $500k – $1M in monthly revenue.
    - Led ad hoc projects using tools like Google Analytics 4, GTM, RudderStack, and Google Ads.
    - Analyzed over 50 datasets monthly, delivering actionable insights for strategic decisions.
    - Developed dashboards that enhanced decision-making for stakeholders.
    """)

    # Education
    st.header("Education")
    st.write("""
    - **Master's in Computer Science** | IU International University of Applied Sciences, Berlin (06/2023 – Present)  
      - GPA: 1.3/5  
    - **Bachelor of Technology** | Walchand College of Engineering, India (08/2018 – 08/2022)  
      - CGPA: 8.76/10  
    - **Higher Secondary** | New Era High School, India (09/2014 – 06/2019)  
      - Percentage: 94.6%
    """)

    # Honors and Awards
    st.header("Honors and Awards")
    st.write("""
    - **Top Performer (FY23)**: Awarded for outstanding contributions at DataVinci.
    - **Data Maestro**: Twice named Employee of the Month at DataVinci.
    - **RudderStack Swags**: Recognized for contributions to the Data Engineering Challenge.
    - **Captain**: Former captain of the college football team, showcasing leadership on and off the field.
    """)

    # Strengths
    st.header("Strengths")
    st.write("Philomath, Critical Thinking, Work Ethic")

    # Languages
    st.header("Languages")
    st.write("""
    - **English**: Proficient (C1)  
    - **German**: Intermediate (B1)
    - **Hindi**: Advanced  
    """)

elif selected == "Projects":
    st.title("Projects")
    
    # Project 1: Unit Test Generator Web App
    st.subheader("1️⃣ Unit Test Generator Web App")
    st.write("""
    A custom-built tool for generating university-specific question papers tailored to exam formats.  
    - **Features**:
      - Upload course unit PDFs and specify chapters/pages for targeted question generation.
      - Automatically generate questions (5 MCQs, 2 six-mark, 2 ten-mark).
      - Adjusts difficulty based on provided practice papers.
      - Tracks token usage and processing time in Google Sheets.
    - **Technology Stack**:
      - Streamlit for UI development.
      - OpenAI API for natural language processing.
      - Python for backend text extraction and processing.
      - Google Sheets for performance metric logging.
    - **Challenges Addressed**:
      - Streamlined the manual process of question paper creation.
      - Enhanced cost-efficiency by processing only the first 20 pages of input PDFs.
    - **Links**:
      - [Live App](https://unit-test-generator-iu.streamlit.app/)
      - [GitHub Repository](https://github.com/Joyan9/project_software_engg)
    """)

    # Project 2: Cab Service Data Analysis Project
    st.subheader("2️⃣ Cab Service Data Analysis Project")
    st.write("""
    As a data analyst, I analyzed data from an Indian cab service provider to understand market penetration patterns across 10 cities. The project involved:
    - **Key Objectives**:
      - Identifying business vs. tourism-focused cities using trip volumes, fares, and distances.
      - Analyzing seasonal trends and weather impacts on demand.
      - Evaluating customer retention with repeat rates and satisfaction metrics.
    - **Tools Used**: Excel, Google Sheets, Looker Studio, Canva.
    - **Outcome**: Strategic recommendations for dynamic pricing, loyalty programs, and service enhancements.
    - **Key Findings**:
      - High retention doesn't always correlate with satisfaction (e.g., Surat and Lucknow had 40%+ repeat rates despite low satisfaction scores).
      - Discovered operational differences between tourist hubs and business centers.
      - Exposed inconsistencies in new vs. repeat passenger ratings (8.65 vs. 6.96).

    - **Links**:  
        -  [Dashboard](https://lookerstudio.google.com/reporting/037d8935-7ebd-4f65-a9a8-3d5a73cd2b6e/page/hcCSE)  
        -  [Presentation](https://www.youtube.com/watch?v=gpTYg58Ojyg)  

    - **Key Learnings**:  
    This project emphasized the importance of analyzing customer behavior and local dynamics for sustainable business growth.
    """)


elif selected == "Skills":
    st.title("Skills")
    st.write("""
    - **Programming**: Python, SQL, JavaScript  
    - **Tools**: Google Analytics, Google Tag Manager, BigQuery, Jupyter Notebook, Google Sheets / Excel
    - **Project Management Tools**: Slack, Notion, Monday, ClickUp, Basecamp  
    """)

elif selected == "Contact":
    st.title("Contact")
    st.write("Feel free to connect with me:")
    st.write("- [LinkedIn](https://www.linkedin.com/in/joyan-bhathena/)")
    st.write("- [GitHub](https://github.com/Joyan9)")
    st.write("- Email: joyansbhathena@gmail.com")

# Footer
st.markdown("---")
st.markdown("© 2024 Joyan Bhathena | Built with ❤️ using Streamlit")

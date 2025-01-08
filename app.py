import streamlit as st
from PIL import Image
from chatagent import chatbot
import os
from dotenv import load_dotenv
load_dotenv()

# Set the page title and layout
api_key = os.getenv("PHIDATA_API_KEY")  # Replace with your actual API key
agent = chatbot()

st.set_page_config(page_title="Your Portfolio", page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded" )

# Add a title
st.title("My Portfolio")
st.write("")
# Add a section for introduction
st.header("Hello! I'm Shashank Ravi :blue[cool] :sunglasses:")
st.write("""
        🚀 A highly skilled Backend Software Developer with mid-level expertise in building scalable Java applications using Spring Boot 
           and enhancing API performance through microservices and caching strategies. Proven track record in optimizing data integrity with 
           robust validation and quality checks, along with effective architecture of RESTful APIs. Committed to leveraging strong analytical 
           and backend development skills to drive innovation and efficiency in the backend systems of the target organization.
""")

# Add a profile image
st.image("profile-pic.png", width=400)  # Replace with your profile image path
st.markdown("""[LinkedIn](https://www.linkedin.com/in/shashankravi24/)
               [LeetCode](https://leetcode.com/u/sravi24/)""")
# Add a skills section
st.header("Skills",divider="gray")
st.write("""
- Languages: Python, Java, PHP, MySQL, NoSQL         
- Backend Development: Spring Boot, Hibernate, JPA, JDBC, Apache Kafka, Rest API, Microservices, AWS, S3, GCP.
- Machine Learning
- Orchestration Tools: Docker, Kubernetes, Git, Jira, CI/CD Pipelines.
- Platforms: Eclipse, Jupiter Notebook, Visual Studio Code.         
- Data Visualization (Matplotlib, Seaborn, Plotly)
""")
 

#Education
st.header("Education",divider="gray")
st.write("""
**LAURENTIAN UNIVERSITY**, Sudbury ON  
MSC in Computational Science — _Sep 2023 - Dec 2024_ """)

st.header("Work Experience",divider="gray")
st.write("""
**MERAGO HEALTHCARE**, Bangalore, KA, IN  
_Backend Software Developer_ — _May 2021 - May 2023_

• Hands-on development of a Microservices API architecture for service calls from API to OpenText, which will use Spring Boot, Spring JPA/Hibernate 
  to store records in Microsoft Azure Database, and Java 8 to send DEEP.IO events.  
         
• Designed and implemented secure RESTful APIs that enhanced data integrity by conducting rigorous quality checks within data pipelines, 
  resulting in a 40% reduction in erroneous transactions throughout the system.
           
• Enhanced the migration from blob storage to S3 storage, dramatically enhancing file management efficiency by 5% and reducing file retrieval 
  times by 20%; implemented expiration URLs that reduced unauthorized access incidents by 10%, significantly strengthening data security.  
         
• Integrated a third-party payment API, enabling smooth transaction flows with multiple payment options for large customers. 
  This streamlined payment processing, reduced transaction times by 20%, and improved system security and reliability through advanced 
  encryption and fraud detection measures.

         
**COGNIZANT TECHNOLOGICAL SOLUTIONS PVT**, Bangalore, KA, IN  
_Program Analyst_ — _Jan 2020 - May 2021_

• Implemented and delivered comprehensive Java code solutions, including business layers, interfaces, services, and stored procedures, 
   which improved system efficiency and reduced processing time.  
         
• Distilled functional and technical requirements, bridging stakeholder vision with clear, actionable specifications, which facilitated 
   smoother project execution and increased stakeholder satisfaction.  
         
• Utilized Agile methodologies (Scrum) to successfully deliver projects on time, achieving a 100% on-time delivery rate.
""")         



st.header("Projects",divider="gray")
st.write("Here are some of my recent projects:")

# Example of a project with a description and link

st.subheader("Project 2: Machine Learning Project: Student Math Score Prediction")
st.write("""

Implemented data ingestion and transformation processes using pandas, ensuring data quality and readiness for analysis. 
Leveraged sci-kit-learn for model training and evaluation. Build pipelines Using the Transformers library Finally, 
created an interactive web application with Flask to display results.
         """)
st.markdown("[View Project on GitHub](https://github.com/sha24Ravi/ML-Project.git)")
st.subheader("Project 1: Cloud monitoring app ")
st.write("""


- Led the development of a cloud-monitoring app in Python and containerized it using Docker.

- Employed a container registry (ECR simulated here).

- Deployed the app on Kubernetes hosted on the Google platform and accessed it through a web browser.
""")
st.markdown("[View Project on GitHub](https://github.com/your-username/project1)")



# Add a contact section
st.header("Download My Resume")
st.write("Click the button below to download my resume:")

# Provide the path to your resume file (make sure it's in the correct directory)
with open("Shashank_t_resume.pdf", "rb") as resume_file:  # Replace with the correct path to your resume
    st.download_button(
        label="Download My Resume",
        data=resume_file,
        file_name="My_Resume.pdf",  # Customize the file name for download
        mime="application/pdf"
    )


st.header("Chat with Me")

# Input for the user to ask questions
user_input=st.text_input("Ask me anything:")
if user_input:
    # Get the response from PhidataAgent
    chatbot_response = agent.get_response(user_input=user_input)
    
    # Display the agent's response
    st.write("Chatbot Response: ", chatbot_response)
else:
    st.write("Type a question above to interact with the chatbot.")

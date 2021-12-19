from nlp import preprocess
from nlp import Similarity
from Footer import Footer
import streamlit as st 
import numpy as np

Footer()

JOB_DEF= 'Paste your job description here.'
RES_DEF ='Paste your resume here.'
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.sidebar.title('Resume Match')

st.header('Match your Resume with any Job Description')

job = st.text_area('Job Description', JOB_DEF, height=350)
resume = st.text_area('Resume', RES_DEF, height=350)
# job = st.file_uploader('Upload Job Descripltion')

job = preprocess(job)
resume = preprocess(resume)

matchPercentage = np.round((Similarity(job, resume)*100),2)

if len(job) > len(JOB_DEF) and len(resume) > len(RES_DEF):
    st.sidebar.markdown(
    f'<div style="color: green; font-size: largest"> Your resume matched <h1> {matchPercentage}% </h1> with the job description. </h1></div>',
    unsafe_allow_html=True)
#         st.write("Your Resume matched", matchPercentage, '% with the job description')
    if matchPercentage >= 80:
        st.balloons()

    



import streamlit as st
import pickle
import pandas as pd

# Load model
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("AI Resume Evaluator")
st.write("Predict if a candidate should be hired or not.")

# User input
experience = st.slider("Experience (Years)", 0, 10)
ai_score = st.slider("AI Score (0-100)", 0, 100)
salary = st.slider("Salary Expectation ($)", 40000, 120000)
projects = st.slider("Projects Count", 0, 10)

# Dummy categorical input for now 
job_role = st.selectbox("Job Role", ["Data Scientist", "ML Engineer", "Analyst"])
education = st.selectbox("Education", ["Bachelor", "Master", "PhD"])
certification = st.selectbox("Certification", ["Yes", "No"])

# Create input DataFrame
input_data = pd.DataFrame({
    'Experience (Years)': [experience],
    'AI Score': [ai_score],
    'Salary Expectation': [salary],
    'Project Count': [projects],
    
    'Job Role_ML Engineer': [1 if job_role == 'ML Engineer' else 0],
    'Job Role_Analyst': [1 if job_role == 'Analyst' else 0],
    'Education_Master': [1 if education == 'Master' else 0],
    'Education_PhD': [1 if education == 'PhD' else 0],
    'Certification_Yes': [1 if certification == 'Yes' else 0],
})

# Predict
prediction = model.predict(input_data)[0]
result = "HIRE ✅" if prediction == 1 else "REJECT ❌"
st.subheader(f"Recruiter Decision: {result}")

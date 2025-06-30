# === 📦 Imports ===
import os
import re
import joblib
import fitz  # for PDF reading
import docx
import pandas as pd
import numpy as np
import streamlit as st
from dateutil import parser
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

# === 🧠 Load Trained Model and Encoder ===
model = joblib.load("resume_ranker_model.pkl")
edu_encoder = joblib.load("education_encoder.pkl")

# === 📄 Resume Reader ===
def read_resume(uploaded_file):
    ext = os.path.splitext(uploaded_file.name)[1].lower()

    if ext == ".txt":
        return uploaded_file.read().decode("utf-8")
    elif ext == ".pdf":
        text = ""
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as pdf:
            for page in pdf:
                text += page.get_text()
        return text
    elif ext == ".docx":
        document = docx.Document(uploaded_file)
        return "\n".join(p.text for p in document.paragraphs)
    else:
        return ""

# === 🧠 Extract Experience Function ===
def extract_years_from_text(text):
    text = text.lower()
    total_months = 0
    matches = re.findall(r'([a-z]{3,9})\s+(\d{4})\s*[-–]\s*([a-z]{3,9}|present|current)\s*(\d{4})?', text)
    matches = matches[:2]

    for start_month, start_year, end_month, end_year in matches:
        try:
            start_date = parser.parse(f"{start_month} {start_year}")
            if end_month in ["present", "current"] or not end_year:
                end_date = datetime.today()
            else:
                end_date = parser.parse(f"{end_month} {end_year}")
            months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
            if months > 0:
                total_months += months
        except:
            continue
    return round(total_months / 12, 1)

# === 🔍 Feature Extractor ===
def extract_features(text):
    text = text.lower()
    edu = "PhD" if "phd" in text else "Masters" if "master" in text else "Bachelors" if "bachelor" in text else "Associate" if "associate" in text else "High School"
    exp = extract_years_from_text(text)
    skills = sum(skill in text for skill in ["python", "sql", "java", "c++", "html", "css", "machine learning", "ai", "tensorflow"])
    certs = len(re.findall(r'certified|certification', text))
    gpa = float(re.search(r'(\d\.\d{1,2})', text).group(1)) if re.search(r'(\d\.\d{1,2})', text) else 3.0
    projects = len(re.findall(r'project', text))
    jobs = len(re.findall(r'internship|intern|worked at|experience at', text))
    hack = len(re.findall(r'hackathon|competition|contest', text))
    github = 1 if "github.com" in text else 0
    linkedin = 1 if re.search(r'(linkedin\.com|linkedin\.in|in/[\w-]+)', text) else 0
    email = 1 if re.search(r'\S+@\S+\.\S+', text) else 0
    prof_words = sum(w in text for w in ["developed", "led", "built", "collaborated", "managed"])

    df_feat = pd.DataFrame([{
        "Education_Level": edu_encoder.transform([edu])[0],
        "Experience_Years": exp,
        "Skills_Matched": skills,
        "Certifications": certs,
        "GPA_or_CGPA": gpa,
        "No_of_Projects": projects,
        "Job_Internship_Count": jobs,
        "Hackathons_Competitions": hack,
        "GitHub_URL_Present": github,
        "LinkedIn_URL_Present": linkedin,
        "Email_Present": email,
        "Professional_Keywords_Count": prof_words
    }])
    return df_feat, edu

# === 🎯 Streamlit UI ===
st.set_page_config(page_title="Resume Ranker", layout="centered")
st.title("📄 Resume Ranker with Suggestions")
uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    if st.button("📊 Rank My Resume"):
        try:
            resume_text = read_resume(uploaded_file)
            features, edu_label = extract_features(resume_text)
            score = model.predict(features)[0]

            st.success(f"🎯 Resume Score: {score:.2f}")
            st.markdown("### 🔍 Breakdown:")
            st.markdown(f"- *Education*: {edu_label}")
            st.markdown(f"- *Experience*: {features['Experience_Years'][0]} years")
            st.markdown(f"- *Skills Matched*: {features['Skills_Matched'][0]}")
            st.markdown(f"- *Certifications*: {features['Certifications'][0]}")
            st.markdown(f"- *Projects*: {features['No_of_Projects'][0]}")
            st.markdown(f"- *GPA*: {features['GPA_or_CGPA'][0]}")
            st.markdown(f"- *GitHub*: {'✅' if features['GitHub_URL_Present'][0] else '❌'}")
            st.markdown(f"- *LinkedIn*: {'✅' if features['LinkedIn_URL_Present'][0] else '❌'}")

            suggestions = []
            if features['Skills_Matched'][0] < 3: suggestions.append("Add more relevant technical skills.")
            if features['Certifications'][0] < 1: suggestions.append("Include relevant certifications.")
            if features['No_of_Projects'][0] < 2: suggestions.append("Add more academic or personal projects.")
            if not features['GitHub_URL_Present'][0]: suggestions.append("Include your GitHub link.")
            if not features['LinkedIn_URL_Present'][0]: suggestions.append("Include your LinkedIn profile.")
            if features['Experience_Years'][0] < 1: suggestions.append("Gain some internship or job experience.")

            if suggestions:
                st.markdown("### 💡 Suggestions to Improve:")
                for s in suggestions:
                    st.write(f"- {s}")
            else:
                st.success("✅ Great resume! No major issues found.")

        except Exception as e:
            st.error(f"❌ Error: {e}")
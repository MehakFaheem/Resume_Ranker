📄 Resume Ranker – AI-Powered Resume Scoring System

Resume Ranker is a machine learning–based web application that automatically analyzes, scores, and ranks resumes based on multiple professional and technical factors.
The goal is to reduce manual resume screening time and help recruiters shortlist candidates more efficiently and fairly.

🚀 Features

Upload resumes in PDF, DOCX, or TXT format

Automatically extracts:

Education level

Years of experience

Skills

Projects

Certifications

GPA / CGPA

GitHub & LinkedIn presence

Generates a resume score using a trained ML model

Provides personalized improvement suggestions

Simple and interactive Streamlit UI

🧠 How It Works

User uploads a resume

Resume text is extracted using file-specific parsers

Important features are extracted using NLP & regex

Features are encoded and passed to a trained ML model

The model predicts a resume score

The app displays:

Resume score

Feature breakdown

Suggestions for improvement

🛠️ Tech Stack

Python

Streamlit – frontend UI

scikit-learn – ML model

Pandas & NumPy – data processing

Joblib – model serialization

PyMuPDF (fitz) – PDF parsing

python-docx – DOCX parsing

Regex & NLP techniques

📂 Project Structure
Resume-Ranker/
│
├── app.py                     # Streamlit application
├── Resume-Ranker.ipynb        # Model training & experimentation
├── resume_ranker_model.pkl    # Trained ML model
├── education_encoder.pkl      # Encoded education levels
├── requirements.txt
└── README.md

▶️ How to Run the Project

Clone the repository

git clone https://github.com/your-username/Resume-Ranker.git
cd Resume-Ranker


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run app.py

📈 Future Improvements

Job description–based ranking

Semantic skill matching using embeddings

Bias detection & fairness scoring

ATS integration

Resume improvement suggestions powered by AI

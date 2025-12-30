## 📄 Resume Ranker – AI-Powered Resume Scoring System

Resume Ranker is a machine learning–based web application that automatically analyzes, scores, and ranks resumes based on multiple professional and technical factors.
The goal is to **reduce manual resume screening time** and help recruiters shortlist candidates more efficiently and fairly.

---

## 🚀 Features

* Upload resumes in **PDF, DOCX, or TXT** format
* Automatically extracts:

  * Education level
  * Years of experience
  * Skills
  * Projects
  * Certifications
  * GPA / CGPA
  * GitHub & LinkedIn presence
* Generates a **resume score** using a trained ML model
* Provides **personalized improvement suggestions**
* Simple and interactive **Streamlit UI**

---

## 🧠 How It Works

1. User uploads a resume
2. Resume text is extracted using file-specific parsers
3. Important features are extracted using NLP & regex
4. Features are encoded and passed to a trained ML model
5. The model predicts a **resume score**
6. The app displays:

   * Resume score
   * Feature breakdown
   * Suggestions for improvement

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – frontend UI
* **scikit-learn** – ML model
* **Pandas & NumPy** – data processing
* **Joblib** – model serialization
* **PyMuPDF (fitz)** – PDF parsing
* **python-docx** – DOCX parsing
* **Regex & NLP techniques**

---

## 📂 Project Structure

```
Resume-Ranker/
│
├── app.py                     # Streamlit application
├── Resume-Ranker.ipynb        # Model training & experimentation
├── resume_ranker_model.pkl    # Trained ML model
├── education_encoder.pkl      # Encoded education levels
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/your-username/Resume-Ranker.git
cd Resume-Ranker
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

* Job description–based ranking
* Semantic skill matching using embeddings
* Bias detection & fairness scoring
* ATS integration
* Resume improvement suggestions powered by AI

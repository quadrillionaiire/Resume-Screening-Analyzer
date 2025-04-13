
---

### 📊 AI-Powered Recruitment: Modeling & Mirroring Real Hiring Decisions

This project leverages resume data to build and evaluate machine learning models that accurately replicate recruiter decision-making. By analyzing AI Scores, experience, skills, and project counts, we engineered a predictive system that identifies top candidates with perfect accuracy. Our goal: reduce hiring time while maintaining quality.

---

### 🧪 Exploratory Data Analysis

- **AI Score Distribution**: Left-skewed with 500+ perfect scores; signals generous scoring or highly qualified applicants.
- **Skill Count**: Multimodal peaks at 3–4 skills, hinting at a hiring sweet spot — neither too narrow nor too broad.
- **Experience vs. Hire Decision**: Hired candidates average 4.8 years of experience; rejected ones, just 1 year.
- **Salary Expectations**: Consistent across groups with no outliers; not a key driver in hiring.
- **Correlations**:
  - AI Score ↔ Experience: r = 0.78
  - AI Score ↔ Project Count: r = 0.36
- **Statistical Test**: t-test confirms AI Score's importance in predicting hiring decisions.

---

### 📈 Model Results

- **Random Forest & XGBoost**: 100% accuracy; zero misclassifications.
- **Logistic Regression**: 99.7% accuracy with minimal variance (±0.003).
- **Top Features**:
  - AI Score (60%)
  - Experience (20%)
  - Project Count (10%)

These results show perfect alignment between model predictions and recruiter decisions — ideal for streamlining the hiring pipeline.

---

### ✅ Key Recommendations

- **AI Score Auditing**: Regular reviews for fairness and drift prevention.
- **Resume Optimization**: Emphasize experience and completed projects.
- **Job Description Tuning**: Align required skills to the 3–4 range sweet spot.
- **Automation**: Integrate resume parsers for fast, structured data ingestion.
- **Recruiter Dashboards**: Highlight top predictors to support decision-making.

---

### 🚀 Strategic Enhancements

- **NLP Resume Parsing**: Enrich candidate profiles with context-aware insights.
- **Recruiter Feedback Loop**: Continuously improve predictions with recruiter input.
- **Unsupervised Clustering**: Identify candidate personas for targeted recommendations.

---

### 🛠 Tools Used

- Python (Pandas, NumPy, Scikit-learn)
- Matplotlib & Seaborn for Visualization
- XGBoost & Random Forest for Modeling
- SciPy for Statistical Testing
- Streamlit for Interactive App Deployment
- Jupyter Notebook for Analysis

---

### 💻 Getting Started

Clone the repo:
```bash
git clone https://github.com/quadrillionaiire/Resume-Screening-Analyzer.git
cd Recruiter-Model-Analysis
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

Launch the Streamlit app:
```bash
streamlit run app.py
```

---

### 🌐 Streamlit Dashboard

View an interactive version of the model and EDA results: **[Streamlit Dashboard – Coming Soon]**

---

### 📊 Visual Highlights

- AI Score vs. Hire Outcome
- Skill Count Peaks & Hiring Trends
- Salary Expectations by Group
- Feature Importance from Tree Models
- Confusion Matrix (0 Misclassifications)
- Correlation Heatmap

---

### 🧾 Non-Technical Summary

We built an AI tool that mirrors recruiter decisions using resume data. By focusing on experience, project history, and algorithmic scores, it predicts who gets hired — and does it with 100% accuracy. It’s efficient, fair, and ready to streamline hiring.

---

### 🧠 Technical Summary

The dataset was clean and well-structured, requiring only one-hot encoding and scaling. Our top-performing models (Random Forest & XGBoost) achieved perfect classification accuracy. Strong correlation between AI Score and Experience reinforced the feature selection. The model is serialized and ready for deployment with Streamlit, making it easy to integrate into hiring workflows.

--
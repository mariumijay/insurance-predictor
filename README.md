# Insurance Predictor

**Insurance Predictor** is a machine learning web application that estimates insurance premium categories based on user data such as age, BMI, income, occupation, lifestyle, and city tier. The project uses a Random Forest Classifier with FastAPI as the backend API and Streamlit as the interactive frontend.

---

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Screenshots](#screenshots)
- [Concepts Covered](#concepts-covered)
- [Requirements](#requirements)
- [License](#license)

---

## Features
- Dynamic calculation of **BMI**, **age group**, **lifestyle risk**, and **city tier**.  
- Predicts insurance premium categories using **Random Forest**.  
- User-friendly interactive **Streamlit interface**.  
- **FastAPI backend** serving predictions via REST API.  
- Input validation using **Pydantic models**.  

---

## Tech Stack
- **Python 3.x**  
- **Pandas & NumPy** for data handling  
- **scikit-learn** for machine learning  
- **FastAPI** for backend API  
- **Uvicorn** as ASGI server  
- **Streamlit** for frontend  
- **Pickle** for model serialization  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/insurance-predictor.git
```
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
1. Start the FastAPI backend
```bash
uvicorn main:app --reload
```

The API will run at http://127.0.0.1:8000.

2. Start the Streamlit frontend
```bash
streamlit run app.py
```


Open your browser at the URL Streamlit provides.

Enter your details and click Predict to see the insurance category.

## API Endpoint

### POST /predict

Request Body Example:
```bash
{
  "age": 30,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 28.5,
  "smoker": true,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

Response Example:
```bash
{
  "predicted_category": "Medium"
}
```
## Screenshots

Add screenshots of the Streamlit app here (optional but recommended).

## Concepts Covered

- Data preprocessing and feature engineering (BMI, age group, lifestyle risk, city tier).

- Machine learning pipeline with scikit-learn (ColumnTransformer, OneHotEncoder, RandomForestClassifier).

- Model evaluation using accuracy_score.

- Model persistence using Pickle.

- REST API creation with FastAPI.

- Input validation with Pydantic BaseModel and computed_field.

- Interactive frontend with Streamlit.

- Frontend-backend integration using HTTP requests.

## Requirements

All dependencies are listed in requirements.txt:
```bash
pandas
numpy
scikit-learn
fastapi
uvicorn
pydantic
streamlit
requests
```
## License

This project is open-source and free to use.cd insurance-predictor


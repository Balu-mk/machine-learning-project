# Air Quality Index (AQI) Status Prediction
### Machine Learning | Python | Streamlit Deployment

---

## Project Summary
This project delivers an **end-to-end Machine Learning solution** for predicting **Air Quality Index (AQI) status categories** using environmental pollutant data.  
It covers **data preprocessing, multi-model experimentation, evaluation, model selection, and deployment** through an interactive **Streamlit web application**.

This project demonstrates **industry-relevant ML engineering and deployment skills**.

---

## Problem Statement
Air pollution is a major public health concern. Accurate AQI classification supports:
- Environmental monitoring
- Public health awareness
- Urban and policy-level decision-making

This system predicts **AQI status categories** based on air pollutant concentrations and city-level data.

---

## Dataset & Input Features

### Input Variables
- PM2.5  
- PM10  
- NO  
- NO₂  
- NOx  
- NH₃  
- CO  
- SO₂  
- O₃  
- Benzene  
- Toluene  
- Xylene  
- City (Label Encoded)

### Target Variable
- **AQI Status (Categorical)**

---

## Machine Learning Pipeline (`AQI_STATUS.ipynb`)

### 1. Data Preprocessing
- Dataset loaded using **Pandas**
- Missing values handled using **mean imputation**
- Feature filtering and cleaning
- Warning suppression for clean execution

---

### 2. Feature Engineering
- **Label Encoding** applied to:
  - AQI Status (Target variable)
  - City (Categorical feature)
- Prepared dataset for supervised learning models

---

### 3. Models Used (Experimentation Phase)

The following **classification algorithms** were implemented and evaluated:

- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Decision Tree Classifier  
- Gaussian Naive Bayes  
- Random Forest Classifier  
- AdaBoost Classifier  
- Gradient Boosting Classifier  

---

### 4. Model Evaluation
Models were evaluated using:
- Training Accuracy
- Testing Accuracy
- Classification Report
- Confusion Matrix
- Hyperparameter tuning using **GridSearchCV / RandomizedSearchCV**

A comparative analysis was performed to identify the best-performing model.

---

### 5. Final Model Selection
✅ **Random Forest Classifier** was selected as the final model due to:
- Higher and consistent test accuracy
- Better generalization performance
- Robust handling of non-linear relationships
- Reduced overfitting through ensemble learning

---

### 6. Model Serialization
Trained artifacts were saved using **Joblib**:

- `model.pkl` – Trained Random Forest model  
- `label.pkl` – Label encoder for AQI status  
- `label2.pkl` – Label encoder for city names  

---

## Deployment: Streamlit Application (`AQI.py`)

### Application Features
- City selection restricted to trained cities
- Numeric input for pollutant values
- Real-time AQI status prediction
- Interactive and user-friendly interface

### Deployment Logic
- Loads trained model and encoders using Joblib
- Encodes city input consistently with training data
- Decodes and displays AQI status prediction

---

## AQI Output Categories
- Good  
- Satisfactory  
- Moderate  
- Poor  
- Very Poor  
- Severe  

*(Categories depend on dataset encoding)*

---

## Tech Stack & Tools

### Programming & Data
- Python
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
- Classification Algorithms
- Ensemble Learning
- Model Evaluation
- Hyperparameter Tuning
- Feature Encoding

### Deployment
- Streamlit
- Joblib
- Jupyter Notebook

---

## Installation & Execution

```bash
git clone https://github.com/your-username/AQI-Status-Prediction.git
cd AQI-Status-Prediction
pip install pandas numpy scikit-learn streamlit joblib
streamlit run AQI.py
 Several features required scaling due to large value differences 

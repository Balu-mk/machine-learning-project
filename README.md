# Suicide Rate Prediction using Machine Learning

## Discription

This project predicts the suicide rate of a country based on socio-economic indicators such as GDP, population, HDI, and other features. The goal is to build a regression model that gives accurate predictions and provides insights into factors affecting suicide rates.

The project includes:
- Data cleaning and preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature engineering  
- Training and tuning multiple regression models  
- Selecting the best-performing model  
- Streamlit web app for user prediction 

## Dataset Info

The dataset contains 27,820 rows and 8 columns collected from Kaggle
I performed:
- Missing value treatment
- Data format changes
- Scaling using StandardScaler
- Label encoding for categorical columns
- Mapping for age category

## Workflow

1. Importing libraries
2. Loading dataset
3. Data cleaning & preprocessing
4. Exploratory Data Analysis (EDA)
5. Feature engineering
6. Model building
7. Hyperparameter tuning
8. Model evaluation (R2 score, RMSE)
9. Deployment using Streamlit 

## Models Used

- Linear Regression  
- Ridge Regression  
- Lasso Regression
- KNN
- Decision Tree Regressor
- Random Forest Regressor  
- Gradient Boosting Regressor
- AdaBoost 
- XGBoost

**Final model chosen**  
- Model: XGBoost  
- R² score: 0.89 
- RMSE: 6.4

## Key Insights from EDA
- Suicide rates vary significantly across **age groups** and **countries**  
- Economic factors such as **GDP per capita** have noticeable correlation  
- Population and year also show trend patterns  
- Several features required scaling due to large value differences 

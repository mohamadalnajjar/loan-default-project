# Loan Default Prediction Using Machine Learning

## Project Overview

This project aims to predict whether a borrower will default on a loan using machine learning classification models. The project follows a complete machine learning workflow including exploratory data analysis, preprocessing, model training, evaluation, interpretability analysis, and risk scoring.

---

## Dataset

Dataset used:
**Give Me Some Credit** (Kaggle)

The dataset contains borrower financial information such as:
- age
- monthly income
- debt ratio
- credit utilization
- delinquency history
- number of open loans
- number of dependents

Target variable:
- `SeriousDlqin2yrs`
    - 1 = borrower defaulted
    - 0 = borrower did not default

---

## Project Workflow

The project includes the following stages:

1. Exploratory Data Analysis (EDA)
2. Data Cleaning and Preprocessing
3. Train-Test Split
4. Logistic Regression Model
5. Balanced Logistic Regression
6. Random Forest Model
7. Model Evaluation
8. Feature Importance Analysis
9. Risk Scoring System
10. ROC Curve Analysis

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

---

## Models Used

### Logistic Regression
Used as the baseline classification model.

### Balanced Logistic Regression
Used class weighting to address class imbalance.

### Random Forest
Used as the advanced ensemble learning model for improved predictive performance.

---

## Evaluation Metrics

The models were evaluated using:
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix

---

## Key Findings

- The dataset is highly imbalanced.
- Accuracy alone was misleading for evaluating performance.
- The Random Forest model achieved the best overall performance.
- Credit utilization and delinquency history were among the most important predictors of loan default.

---

## Risk Scoring

Borrowers were categorized into:
- Low Risk
- Medium Risk
- High Risk

based on predicted default probabilities.

---

## Repository Structure

```text
loan-default-project/
│
├── figures/
├── models/
├── notebooks/
├── reports/
├── results/
├── slides/
├── README.md
├── requirements.txt
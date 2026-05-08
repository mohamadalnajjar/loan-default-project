# Loan Default Prediction Presentation

---

# Slide 1 — Title Slide

## Loan Default Prediction Using Machine Learning

Engineering Project: Classification

Team Members:
- Add names here

---

# Slide 2 — Project Objective

## Goal

Predict whether a borrower will default on a loan using machine learning classification models.

## Why It Matters

- Financial institutions face significant losses from loan defaults.
- Machine learning can improve risk assessment and support lending decisions.

---

# Slide 3 — Dataset Overview

## Dataset

Give Me Some Credit (Kaggle)

## Dataset Information

- 150,000 borrower records
- Financial and demographic features
- Binary classification problem

## Target Variable

`SeriousDlqin2yrs`
- 1 = default
- 0 = non-default

---

# Slide 4 — Exploratory Data Analysis

## Key Findings

- Dataset contains missing values
- Monthly income contains outliers
- Dataset is highly imbalanced
- Delinquency-related variables strongly correlate with default risk

## Include Figures

- Loan default distribution
- Monthly income distribution
- Correlation heatmap

---

# Slide 5 — Data Preprocessing

## Preprocessing Steps

- Removed unnecessary columns
- Handled missing values
- Applied train-test split
- Standardized features for Logistic Regression
- Addressed class imbalance

---

# Slide 6 — Machine Learning Models

## Models Used

### Logistic Regression
Baseline model

### Balanced Logistic Regression
Improved minority-class detection

### Random Forest
Advanced ensemble learning model

---

# Slide 7 — Model Evaluation Metrics

## Metrics Used

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix

## Why Accuracy Alone Was Misleading

The dataset was highly imbalanced.

---

# Slide 8 — Model Performance Comparison

## Results Table

| Model | Accuracy | Recall | ROC-AUC |
|---|---|---|---|
| Logistic Regression | 0.934 | 0.045 | 0.714 |
| Balanced Logistic Regression | 0.776 | 0.670 | 0.802 |
| Random Forest | 0.819 | 0.731 | 0.864 |

## Key Observation

Random Forest achieved the best overall balance.

---

# Slide 9 — Random Forest Confusion Matrix

## Include Figure

- Random Forest confusion matrix

## Discussion

- Improved detection of default cases
- Better recall performance
- Reduced false negatives

---

# Slide 10 — Feature Importance

## Most Important Features

- RevolvingUtilizationOfUnsecuredLines
- NumberOfTimes90DaysLate
- NumberOfTime30-59DaysPastDueNotWorse

## Include Figure

- Feature importance chart

---

# Slide 11 — Risk Scoring System

## Risk Categories

- Low Risk
- Medium Risk
- High Risk

## Business Use

The model can support:
- borrower risk assessment
- lending decisions
- financial risk management

---

# Slide 12 — ROC Curve

## Include Figure

- Random Forest ROC curve

## Key Result

ROC-AUC ≈ 0.864

---

# Slide 13 — Limitations

## Limitations

- Dataset imbalance
- Missing values
- Potential bias
- Model should not fully automate financial approvals

---

# Slide 14 — Conclusion

## Final Conclusion

- Machine learning can effectively support loan default prediction.
- Random Forest achieved the best performance.
- Delinquency history and credit utilization were the strongest predictors.

---

# Slide 15 — Questions

## Thank You

Questions?
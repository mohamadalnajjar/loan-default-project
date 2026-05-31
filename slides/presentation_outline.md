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

# Slide 12 — Graphical User Interface (GUI)

## Purpose of the GUI

The GUI was created so normal users can interact with the loan prediction system without writing code.

## Main Functions

- Allows the user to enter borrower financial information
- Sends the entered values to the trained machine learning model
- Displays a clear prediction result
- Makes the project easier to test, demonstrate, and use

## Include Figure

- Screenshot of the GUI input screen

---

# Slide 13 — GUI Prediction Output

## User-Friendly Result

Instead of showing only technical model output, the GUI displays a simple message such as:

- "You are eligible for a loan"
- "You are not eligible for a loan"
- "Manual review is recommended"

## How the Output Is Decided

- Low risk → Eligible
- Medium risk → Needs further review
- High risk → Not eligible

## Why This Is Important

The GUI turns the machine learning model into a practical application that can support real-world loan decision-making.

## Include Figure

- Screenshot of the GUI prediction/result screen

---

# Slide 14 — ROC Curve

## Include Figure

- Random Forest ROC curve

## Key Result

ROC-AUC ≈ 0.864

---

# Slide 15 — Limitations

## Limitations

- Dataset imbalance
- Missing values
- Potential bias
- Model should not fully automate financial approvals

---

# Slide 16 — Conclusion

## Final Conclusion

- Machine learning can effectively support loan default prediction.
- Random Forest achieved the best performance.
- Delinquency history and credit utilization were the strongest predictors.

---

# Slide 17 — Questions

## Thank You

Questions?
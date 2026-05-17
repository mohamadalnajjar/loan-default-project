# Loan Default Prediction Using Machine Learning

## Engineering Project: Classification

---

# Abstract

This project investigates the use of machine learning models for predicting loan default risk using the “Give Me Some Credit” dataset. The project applies a complete machine learning workflow including exploratory data analysis, preprocessing, classification modeling, evaluation, feature importance analysis, and risk scoring. Multiple classification models were trained and compared, including Logistic Regression, Balanced Logistic Regression, and Random Forest. Results showed that the Random Forest model achieved the strongest overall performance with a ROC-AUC score of approximately 0.864. The project also demonstrates how machine learning can support financial risk assessment through borrower risk categorization.

---

# 1. Introduction

Loan default prediction is an important problem in the financial industry. Financial institutions must evaluate borrower risk before approving loans in order to reduce financial losses and maintain stable lending systems.

Machine learning techniques can assist in predicting whether a borrower is likely to default on a loan by analyzing historical financial information and borrower behavior patterns.

This project aims to develop and evaluate machine learning models capable of predicting loan default risk using borrower-related financial features. The project follows a complete machine learning workflow including data preprocessing, exploratory data analysis, model training, evaluation, and interpretation.

---

# 2. Dataset Description

The dataset used in this project is the “Give Me Some Credit” dataset obtained from Kaggle.

The dataset contains 150,000 borrower records and includes financial and demographic features such as:

- age
- monthly income
- debt ratio
- revolving credit utilization
- delinquency history
- number of open loans
- number of dependents

The target variable is:

`SeriousDlqin2yrs`

Where:
- 1 = borrower defaulted
- 0 = borrower did not default

The dataset was highly imbalanced, with non-default cases significantly outnumbering default cases.

---

# 3. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to better understand the structure and characteristics of the dataset.

The following analyses were conducted:
- dataset overview
- missing value analysis
- class imbalance analysis
- feature distribution analysis
- outlier inspection
- correlation analysis

Several visualizations were generated including:
- loan default distribution
- age distribution
- monthly income distribution
- correlation heatmap
- feature importance plots

The analysis revealed that:
- the dataset contains missing values in MonthlyIncome and NumberOfDependents
- MonthlyIncome contains significant outliers
- the dataset is highly imbalanced
- delinquency-related variables are strongly correlated with loan default behavior

---

# 4. Data Preprocessing

Several preprocessing steps were applied before model training.

These included:
- removing unnecessary columns
- handling missing values using median imputation
- train-test splitting
- feature scaling for Logistic Regression models

The dataset was split into:
- 80% training data
- 20% testing data

Stratified sampling was used to preserve class distribution across both subsets.

---

# 5. Machine Learning Models

## 5.1 Logistic Regression

Logistic Regression was used as the baseline classification model.

The baseline model achieved high accuracy but poor recall performance due to the severe class imbalance.

---

## 5.2 Balanced Logistic Regression

A balanced Logistic Regression model was trained using class weighting to improve detection of minority-class default cases.

This significantly improved recall performance but reduced overall accuracy.

---

## 5.3 Random Forest

A Random Forest classifier was trained as the advanced ensemble learning model.

The Random Forest model achieved the best overall balance between:
- recall
- F1-score
- ROC-AUC

It also provided feature importance scores useful for interpretability analysis.

---

# 6. Model Evaluation

The models were evaluated using the following metrics:
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

The following table summarizes model performance:

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---|---|---|---|---|
| Logistic Regression | 0.934 | 0.581 | 0.045 | 0.083 | 0.714 |
| Balanced Logistic Regression | 0.776 | 0.182 | 0.670 | 0.286 | 0.802 |
| Random Forest | 0.819 | 0.231 | 0.731 | 0.351 | 0.864 |

The baseline Logistic Regression model produced misleadingly high accuracy due to class imbalance. In contrast, the Random Forest model achieved significantly better recall and ROC-AUC performance, making it more suitable for identifying risky borrowers.

---

# 7. Feature Importance Analysis

Feature importance analysis was performed using the Random Forest model.

The most influential features included:
- RevolvingUtilizationOfUnsecuredLines
- NumberOfTimes90DaysLate
- NumberOfTime30-59DaysPastDueNotWorse
- NumberOfTime60-89DaysPastDueNotWorse

These features are logically associated with borrower financial risk and delinquency behavior.

The analysis demonstrated that borrower repayment history plays a major role in predicting loan default risk.

---

# 8. Risk Scoring System

A simple risk scoring system was developed using predicted default probabilities.

Borrowers were categorized into:
- Low Risk
- Medium Risk
- High Risk

based on probability thresholds.

This demonstrates how machine learning predictions can support practical financial decision-making processes.

---

# 9. Business Interpretation

The developed model could assist financial institutions by:
- identifying high-risk borrowers
- reducing loan default losses
- supporting credit approval decisions
- improving risk assessment processes

However, machine learning models should support human decision-making rather than fully automate financial approvals.

---

# 10. Limitations

Several limitations exist in this project:
- the dataset contains missing values and outliers
- the dataset is highly imbalanced
- financial datasets may contain historical bias
- the model should not be used as the sole decision-maker for financial approvals

Additional tuning and feature engineering may further improve model performance.

---

# 11. Future Improvements

Potential future improvements include:
- hyperparameter optimization
- additional ensemble models
- SHAP interpretability analysis
- advanced imbalance handling techniques
- deployment as a web application

---

# 12. Conclusion

This project demonstrated the application of machine learning techniques for loan default prediction.

Among the evaluated models, the Random Forest classifier achieved the strongest overall performance and provided meaningful insights into borrower risk behavior.

The project also demonstrated the importance of:
- proper preprocessing
- handling class imbalance
- selecting appropriate evaluation metrics
- model interpretability
- risk scoring

Overall, the project highlights how machine learning can support financial risk assessment and decision-making.

---

# References

- Kaggle. “Give Me Some Credit” Dataset.
- Scikit-learn Documentation.
- Pandas Documentation.
- Seaborn Documentation.
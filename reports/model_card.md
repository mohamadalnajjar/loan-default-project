# Model Card — Loan Default Prediction Model

---

# Model Details

## Model Name
Loan Default Prediction Random Forest Classifier

## Model Type
Binary Classification

## Algorithm
Random Forest

## Framework
Scikit-learn

---

# Intended Use

This model is designed to predict the probability that a borrower will default on a loan.

The model is intended to support:
- financial risk assessment
- borrower analysis
- loan approval support systems

The model should assist human decision-making rather than fully automate financial approval processes.

---

# Dataset

Dataset Used:
- Give Me Some Credit (Kaggle)

Dataset Characteristics:
- 150,000 borrower records
- financial and demographic features
- imbalanced target classes

Target Variable:
- `SeriousDlqin2yrs`
    - 1 = default
    - 0 = non-default

---

# Features Used

The model uses borrower-related features including:
- revolving credit utilization
- age
- debt ratio
- monthly income
- delinquency history
- number of open loans
- number of dependents

---

# Performance Metrics

| Metric | Value |
|---|---|
| Accuracy | 0.819 |
| Precision | 0.231 |
| Recall | 0.731 |
| F1 Score | 0.351 |
| ROC-AUC | 0.864 |

---

# Key Findings

The most important predictors of default risk were:
- RevolvingUtilizationOfUnsecuredLines
- NumberOfTimes90DaysLate
- NumberOfTime30-59DaysPastDueNotWorse
- NumberOfTime60-89DaysPastDueNotWorse

---

# Limitations

- The dataset is highly imbalanced.
- Financial datasets may contain historical bias.
- Missing values and outliers exist within the dataset.
- The model should not be used as the sole basis for financial approval decisions.

---

# Ethical Considerations

Machine learning models in financial systems may unintentionally introduce bias or unfair treatment toward certain borrower groups.

The model should therefore:
- support human analysts
- be regularly monitored
- be evaluated for fairness
- avoid fully automated decision-making

---

# Future Improvements

Potential future improvements include:
- hyperparameter optimization
- advanced imbalance handling
- SHAP interpretability analysis
- additional ensemble models
- deployment as a web application
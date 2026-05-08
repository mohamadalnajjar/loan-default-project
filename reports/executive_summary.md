# Executive Summary

## Loan Default Prediction Using Machine Learning

This project developed a machine learning system for predicting loan default risk using borrower financial information from the “Give Me Some Credit” dataset.

The project applied a complete machine learning workflow including:
- exploratory data analysis
- preprocessing
- classification modeling
- evaluation
- feature importance analysis
- risk scoring

Three machine learning models were evaluated:
- Logistic Regression
- Balanced Logistic Regression
- Random Forest

The dataset was highly imbalanced, meaning non-default cases greatly outnumbered default cases. Because of this imbalance, accuracy alone was not sufficient for evaluating model performance.

The Random Forest model achieved the best overall results with:
- Accuracy: 0.819
- Recall: 0.731
- ROC-AUC: 0.864

The model demonstrated strong ability to distinguish between risky and non-risky borrowers.

Feature importance analysis revealed that the strongest predictors of loan default were:
- revolving credit utilization
- delinquency history
- late payment behavior

A risk scoring system was also developed to classify borrowers into:
- Low Risk
- Medium Risk
- High Risk

This project demonstrates how machine learning can support financial institutions in:
- borrower risk assessment
- credit approval support
- financial risk management

However, the model should support human decision-making rather than fully automate financial approval processes due to potential bias and dataset limitations.
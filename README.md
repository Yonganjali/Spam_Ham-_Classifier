# Spam/Ham Message Classifier

## Project Overview

This project classifies text messages as either Spam or Ham
using Natural Language Processing and Machine Learning.

## Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- TF-IDF
- LinearSVC
- Streamlit

## Machine Learning Workflow

1. Dataset collection
2. Data cleaning
3. Text preprocessing
4. Train-test split
5. TF-IDF feature extraction
6. Linear SVM classification
7. Hyperparameter tuning
8. Model evaluation
9. Model serialization
10. Streamlit deployment

## Model

The final classifier uses:

- Text preprocessing
- TF-IDF Vectorization
- Linear Support Vector Machine (LinearSVC)
## Model Performance

The final model was evaluated on the test dataset.

| Metric | Score |
|--------|-------|
| Accuracy | 98.16% |
| Precision | 98.28% |
| Recall | 87.02% |
| F1 Score | 92.31% |

The model achieved an accuracy of 98.16% on the test set.
The precision of 98.28% indicates that most messages predicted
as spam were actually spam. The recall of 87.02% indicates that
the model successfully identified most of the actual spam messages.
The F1 score of 92.31% shows a strong balance between precision
and recall.
## Deployment

The application is deployed using Streamlit Community Cloud.

## Usage

1. Enter a message.
2. Click "Classify Message".
3. The application predicts whether the message is Spam or Ham.

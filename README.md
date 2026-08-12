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
## Hyperparameter Tuning

GridSearchCV with 5-fold cross-validation was used to find the
best hyperparameters for the TF-IDF and LinearSVC components.

### Best Parameters

| Parameter | Selected Value |
|---|---|
| SVM C | 1 |
| SVM class weight | None |
| TF-IDF max features | 10,000 |
| TF-IDF min df | 1 |
| TF-IDF n-gram range | (1, 2) |

The best cross-validation F1 score was **91.58%**.

The TF-IDF vectorizer uses both unigrams and bigrams, allowing the
model to consider individual words as well as two-word combinations.
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
### Confusion Matrix

| | Predicted Ham | Predicted Spam |
|---|---:|---:|
| Actual Ham | 901 | 2 |
| Actual Spam | 17 | 114 |

The model correctly classified 901 Ham messages and 114 Spam
messages. It incorrectly classified 2 Ham messages as Spam and
17 Spam messages as Ham.

## Deployment

The application is deployed using Streamlit Community Cloud.

## Usage

1. Enter a message.
2. Click "Classify Message".
3. The application predicts whether the message is Spam or Ham.

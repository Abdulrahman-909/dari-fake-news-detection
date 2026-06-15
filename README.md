# Dari Fake News Detection using Machine Learning

## Overview

This project presents a comparative study of machine learning algorithms for detecting fake news in the Dari language. The research evaluates the effectiveness of three widely used classification models:

* Logistic Regression (LR)
* Naive Bayes (NB)
* Support Vector Machine (SVM)

The objective is to identify the most accurate and efficient model for classifying real and fake news articles written in Dari.

---

## Dataset

The dataset contains:

* 3,000 labeled news articles
* Two classes:

  * Real News
  * Fake News

The dataset was preprocessed before model training.

---

## Data Preprocessing

The following preprocessing steps were applied:

* Merging headline and content fields
* Text normalization
* Removing punctuation and special characters
* Removing unnecessary spaces
* Cleaning noisy text
* TF-IDF feature extraction

---

## Machine Learning Models

Three machine learning algorithms were trained and evaluated:

### Logistic Regression (LR)

A linear classification algorithm that achieved the best overall performance in this study.

### Naive Bayes (NB)

A probabilistic classifier with the fastest training time.

### Support Vector Machine (SVM)

A powerful classification algorithm evaluated for comparison purposes.

---

## Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Cross Validation
* Training Time
* Prediction Time

---

## Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 85.67%   |
| Naive Bayes         | 85.50%   |
| SVM                 | 83.33%   |

### Key Findings

* Logistic Regression achieved the highest overall performance.
* Naive Bayes achieved the fastest training speed.
* SVM showed acceptable performance but lower accuracy than LR and NB.
* Classical machine learning algorithms remain effective for fake news detection in low-resource languages such as Dari.

---

## Repository Structure

```text
data/           Dataset files
figures/        Generated graphs and confusion matrices
saved_model/    Trained model and TF-IDF vectorizer
app.py          Streamlit application
*.ipynb         Training and evaluation notebook
```

---

## Author

**Abdulrahman Rahimi**

Bachelor Thesis Project

Faculty of Computer Science

Balkh University

Afghanistan

---

## Research Topic

Fake News Detection in Dari Language using Machine Learning Techniques: A Comparative Study of Logistic Regression, Naive Bayes, and Support Vector Machine.

# Email Spam Classifier API

This is an email spam classifier API built using Django Ninja and a Naive Bayes machine learning model.

## Features
- Predicts whether a text message is spam or not.
- Returns the prediction label, confidence score, and a human-readable statement.

## Technologies Used
- Django
- Django Ninja
- NLTK (Natural Language Toolkit)
- Scikit-learn (for the model)
- Python

## How to Run Locally
1. Clone the repository
2. Install dependencies
3. Start the Django server

## API Endpoint
- **POST** `/api/classifier/predict`
  - **Body:** `{ "text": "your message here" }`
  - **Returns:** Prediction, confidence, and statement.

---

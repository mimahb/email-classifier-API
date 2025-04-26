import joblib
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Ensure these are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Load the model (place your .pkl in project root)
model = joblib.load('spam_classifier.pkl')
vectorizer = joblib.load('vectorizer.pkl')

stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return [word for word in tokens if word.isalpha() and word not in stop_words]

def extract_features(words):
    return {word: True for word in words}

def classify_text(text):
    tokens = preprocess(text)
    features = extract_features(tokens)
    
    prediction = model.classify(features)
    
    prob_dist = model.prob_classify(features)
    confidence = prob_dist.prob(prediction)  # probability of the predicted label

    return prediction, confidence


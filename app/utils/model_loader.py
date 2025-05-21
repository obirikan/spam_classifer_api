import joblib

vectorizer = joblib.load('./model/vectorizer.pkl')
model = joblib.load('./model/spam_model.pkl')

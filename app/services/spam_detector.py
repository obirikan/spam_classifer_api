from app.utils.model_loader import model,vectorizer

def predict_spam(text: str) -> bool:
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)
    return bool(prediction[0])
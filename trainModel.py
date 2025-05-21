import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load and preprocess
data = pd.read_csv('spam_data.tsv', sep='\t', header=None)
data.columns = ['label', 'text']
data['label_num'] = data.label.map({'ham': 0, 'spam': 1})

X_train, _, y_train, _ = train_test_split(data['text'], data['label_num'], test_size=0.2, random_state=42)

# Vectorize text
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save model and vectorizer
# joblib.dump(vectorizer, './model/vectorizer.pkl')
# joblib.dump(model, './model/spam_model.pkl')

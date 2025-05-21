import pandas as pd
import joblib

model = joblib.load('./model/spam_model.pkl')
model_old = joblib.load('./model/spam_model_old.pkl')
vectorizer = joblib.load('./model/vectorizer.pkl')

# Load new data
new_data = pd.read_csv('spam.csv', encoding='ISO-8859-1', usecols=[0, 1], names=['label', 'text'], header=None)
new_data.dropna(inplace=True)

new_data['label_num'] = new_data['label'].map({'ham': 0, 'spam': 1})


new_data.dropna(inplace=True)


X_new_vec = vectorizer.transform(new_data['text'])
y_new = new_data['label_num']


model.partial_fit(X_new_vec, y_new,classes=[0,1])


print("old Class counts before update:", model_old.class_count_)
print("New Class counts before update:", model.class_count_)
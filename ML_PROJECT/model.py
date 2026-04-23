import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data.csv")

# Cleaning
def clean(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

df['text'] = df['text'].apply(clean)
df.drop_duplicates(inplace=True)

# Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Evaluate
pred = model.predict(X)
print("Accuracy:", accuracy_score(y, pred))

# Prediction function
def predict(text):
    text = clean(text)
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]

# Test
print(predict("you are bad"))
print(predict("good job"))
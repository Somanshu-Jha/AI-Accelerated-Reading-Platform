from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

class DifficultyClassifier:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()

    def train(self, texts, labels):
        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)

    def predict(self, text):
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]
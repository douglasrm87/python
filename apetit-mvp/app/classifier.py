from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

class IntentClassifier:
    def __init__(self, training_path="training_data"):
        self.labels = []
        self.texts = []

        for file in os.listdir(training_path):
            with open(os.path.join(training_path, file), "r", encoding="utf-8") as f:
                self.labels.append(file.replace(".txt", ""))
                self.texts.append(f.read())

        self.vectorizer = TfidfVectorizer()
        self.vectors = self.vectorizer.fit_transform(self.texts)

    def classify(self, user_text):
        user_vector = self.vectorizer.transform([user_text])
        similarity = cosine_similarity(user_vector, self.vectors)
        index = similarity.argmax()
        return self.labels[index]
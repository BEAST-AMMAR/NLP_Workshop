import nltk
import random
import string
from nltk.corpus import stopwords, movie_reviews
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

# Download required NLTK data
nltk.download('movie_reviews')
nltk.download('stopwords')

# Get movie reviews data
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# Extract texts and labels
texts = [' '.join(words) for words, category in documents]
labels = [1 if category == 'pos' else 0 for words, category in documents]

# Preprocessing: convert to lowercase
texts = [text.lower() for text in texts]

# Remove punctuation marks
texts = [''.join(c for c in text if c not in string.punctuation) for text in texts]

# Remove stop words
stop_words = set(stopwords.words('english'))
texts = [' '.join(word for word in text.split() if word not in stop_words) for text in texts]

# Vectorize using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
y = labels

# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Multinomial Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy on Test Set: {accuracy:.4f}")

# Function to predict sentiment of unknown sentence
def predict_sentiment(sentence):
    # Preprocess the input sentence: lowercase, remove punctuation, remove stopwords
    sentence = sentence.lower()
    sentence = ''.join(c for c in sentence if c not in string.punctuation)
    sentence_words = [word for word in sentence.split() if word not in stop_words]
    sentence = ' '.join(sentence_words)
    # Vectorize
    sentence_vectorized = vectorizer.transform([sentence])
    # Predict
    prediction = model.predict(sentence_vectorized)
    # Return sentiment
    return "Positive" if prediction[0] == 1 else "Negative"

# Interactive prediction
print("\nSentiment Analysis for Movie Reviews")
print("Enter a sentence to predict its sentiment (type 'quit' to exit):")

while True:
    user_input = input("Your sentence: ")
    if user_input.lower() == 'quit':
        break
    sentiment = predict_sentiment(user_input)
    print(f"Predicted sentiment: {sentiment}")
    print("-" * 40)

import json

# Load the notebook
with open('NLP_Workshop_Starter.ipynb', 'r') as f:
    notebook = json.load(f)

# New cells to add
new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 10. Text Classification with Multinomial Naive Bayes"]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "from sklearn.model_selection import train_test_split\n",
            "from sklearn.naive_bayes import MultinomialNB\n",
            "from sklearn.metrics import accuracy_score\n",
            "from sklearn.feature_extraction.text import CountVectorizer\n",
            "\n",
            "import nltk\n",
            "nltk.download('movie_reviews')\n",
            "from nltk.corpus import movie_reviews\n",
            "import random\n",
            "import string\n",
            "from nltk.corpus import stopwords\n",
            "\n",
            "# Get movie reviews data\n",
            "documents = [(list(movie_reviews.words(fileid)), category)\n",
            "             for category in movie_reviews.categories()\n",
            "             for fileid in movie_reviews.fileids(category)]\n",
            "\n",
            "random.shuffle(documents)\n",
            "\n",
            "# Extract texts and labels\n",
            "texts = [' '.join(words) for words, category in documents]\n",
            "labels = [1 if category == 'pos' else 0 for words, category in documents]\n",
            "\n",
            "# Preprocessing: case fold to lowercase\n",
            "texts = [text.lower() for text in texts]\n",
            "\n",
            "# Remove punctuation marks\n",
            "texts = [''.join(c for c in text if c not in string.punctuation) for text in texts]\n",
            "\n",
            "# Remove stop words\n",
            "stop_words = set(stopwords.words('english'))\n",
            "texts = [' '.join(word for word in text.split() if word not in stop_words) for text in texts]\n",
            "\n",
            "# Vectorize\n",
            "vectorizer = CountVectorizer()\n",
            "X = vectorizer.fit_transform(texts)\n",
            "y = labels\n",
            "\n",
            "# Split data: 80% train, 20% test\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
            "\n",
            "# Train Multinomial Naive Bayes model\n",
            "model = MultinomialNB()\n",
            "model.fit(X_train, y_train)\n",
            "\n",
            "# Predict on test set\n",
            "y_pred = model.predict(X_test)\n",
            "\n",
            "# Calculate accuracy\n",
            "accuracy = accuracy_score(y_test, y_pred)\n",
            "print(f\"Model Accuracy on Test Set: {accuracy:.2f}\")\n"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Function to predict sentiment of unknown sentence\n",
            "def predict_sentiment(sentence):\n",
            "    # Preprocess and vectorize the input sentence\n",
            "    sentence_vectorized = vectorizer.transform([sentence])\n",
            "    # Predict\n",
            "    prediction = model.predict(sentence_vectorized)\n",
            "    # Return sentiment\n",
            "    return \"Positive\" if prediction[0] == 1 else \"Negative\"\n",
            "\n",
            "# Example predictions\n",
            "print(\"Prediction for 'I love this product!':\", predict_sentiment(\"I love this product!\"))\n",
            "print(\"Prediction for 'This is awful':\", predict_sentiment(\"This is awful\"))\n",
            "\n",
            "# Try your own sentence\n",
            "# user_sentence = \"Your sentence here\"\n",
            "# print(\"Prediction:\", predict_sentiment(user_sentence))\n"
        ]
    }
]

# Find the position to insert, before the "Workshop Exercises" cell
insert_index = None
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'markdown' and '## Workshop Exercises' in ''.join(cell['source']):
        insert_index = i
        break

if insert_index is not None:
    # Insert the new cells before the Workshop Exercises
    notebook['cells'][insert_index:insert_index] = new_cells
else:
    # If not found, append at the end
    notebook['cells'].extend(new_cells)

# Save the notebook
with open('NLP_Workshop_Starter.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook updated successfully with text classification section.")

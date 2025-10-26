import json

# Load the notebook
with open('NLP_Workshop_Starter.ipynb', 'r') as f:
    notebook = json.load(f)

# New cells to add
new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 9. Text Vectorization Techniques"]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### Bag of Words with CountVectorizer"]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "from sklearn.feature_extraction.text import CountVectorizer\n",
            "import pandas as pd\n",
            "\n",
            "# Sample documents\n",
            "documents = [\n",
            "    \"Natural language processing is fun\",\n",
            "    \"Machine learning helps computers learn\",\n",
            "    \"NLP and ML are related fields\",\n",
            "    \"Text processing involves tokenization\"\n",
            "]\n",
            "\n",
            "# Create CountVectorizer for Bag of Words\n",
            "vectorizer = CountVectorizer()\n",
            "# Fit and transform\n",
            "X = vectorizer.fit_transform(documents)\n",
            "# Get feature names\n",
            "feature_names = vectorizer.get_feature_names_out()\n",
            "# Convert to DataFrame\n",
            "df_bow = pd.DataFrame(X.toarray(), columns=feature_names)\n",
            "print(\"Bag of Words Representation:\")\n",
            "df_bow"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### TF-IDF Vectorization"]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "from sklearn.feature_extraction.text import TfidfVectorizer\n",
            "\n",
            "# Create TfidfVectorizer\n",
            "tfidf_vectorizer = TfidfVectorizer()\n",
            "# Fit and transform\n",
            "X_tfidf = tfidf_vectorizer.fit_transform(documents)\n",
            "# Get feature names\n",
            "tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()\n",
            "# Convert to DataFrame\n",
            "df_tfidf = pd.DataFrame(X_tfidf.toarray(), columns=tfidf_feature_names)\n",
            "print(\"TF-IDF Representation:\")\n",
            "df_tfidf"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### Count Vectorizer"]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Count Vectorizer is the same as Bag of Words\n",
            "count_vectorizer = CountVectorizer()\n",
            "X_count = count_vectorizer.fit_transform(documents)\n",
            "count_feature_names = count_vectorizer.get_feature_names_out()\n",
            "df_count = pd.DataFrame(X_count.toarray(), columns=count_feature_names)\n",
            "print(\"Count Vectorizer Representation:\")\n",
            "df_count"
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

print("Notebook updated successfully!")

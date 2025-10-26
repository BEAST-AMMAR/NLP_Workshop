#!/usr/bin/env python3
"""
NLTK Setup Script for NLP Workshop
This script downloads and sets up all necessary NLTK data
"""

try:
    import nltk
    import ssl
except ImportError:
    print("❌ NLTK is not installed!")
    print("Please install it first:")
    print("pip install nltk")
    exit(1)

def setup_nltk():
    """Download and setup NLTK data"""
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    print("Setting up NLTK data...")

    # Essential NLTK data for NLP workshop
    datasets = [
        'punkt',           # Sentence tokenizer
        'stopwords',       # Stopword lists
        'wordnet',         # Lexical database
        'averaged_perceptron_tagger',  # POS tagger
        'maxent_ne_chunker',           # Named entity chunker
        'words',           # Word lists
        'treebank',        # Treebank corpus
        'brown',           # Brown corpus
        'gutenberg',       # Project Gutenberg corpus
        'inaugural',       # Presidential inaugural addresses
        'movie_reviews',   # Movie reviews for sentiment analysis
        'product_reviews_1', # Product reviews
        'product_reviews_2', # Product reviews
        'twitter_samples', # Twitter samples
        'vader_lexicon'    # Sentiment analysis lexicon
    ]

    for dataset in datasets:
        try:
            print(f"Downloading {dataset}...")
            nltk.download(dataset, quiet=True)
            print(f"✓ {dataset} downloaded successfully")
        except Exception as e:
            print(f"✗ Error downloading {dataset}: {e}")

    print("\nNLTK setup completed!")
    print("You can now use all NLTK features in your workshop.")

if __name__ == "__main__":
    setup_nltk()

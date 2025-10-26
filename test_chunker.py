import nltk
from nltk.tokenize import word_tokenize
from nltk import RegexpParser

# Download required NLTK data if not already
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define grammar for chunking
grammar = r"""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Sample sentence for chunking
sample_sentence = "The quick brown fox jumps over the lazy dog"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sample_sentence)
pos_tags = nltk.pos_tag(tokens)

print("POS Tags:")
print(pos_tags)
print("\n" + "="*50 + "\n")

# Parse the sentence into chunks
chunked_tree = chunk_parser.parse(pos_tags)

print("Chunked Tree:")
print(chunked_tree)
print("\n" + "="*50 + "\n")

# Pretty print the tree structure
print("Tree Structure:")
chunked_tree.pretty_print()

print("Chunker test completed successfully!")

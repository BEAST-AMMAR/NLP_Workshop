import nbformat as nbf

# Load the notebook
nb = nbf.read('NLP_Workshop_Starter.ipynb', as_version=4)

# Create new cells
markdown_cell = nbf.v4.new_markdown_cell("""## 11. Chunking with Parser and Grammar

Chunking (also known as shallow parsing) is the process of grouping words into meaningful phrases or chunks, such as noun phrases (NP), verb phrases (VP), and prepositional phrases (PP). This helps in understanding the syntactic structure of sentences.

We'll use NLTK's `RegexpParser` to define grammar rules based on part-of-speech tags and apply them to parse text into chunks.

### Grammar Rules

- **NP (Noun Phrase)**: `<DT|JJ|NN.*>+` - Determiner, adjective, or noun sequences
- **PP (Prepositional Phrase)**: `<IN><NP>` - Preposition followed by noun phrase
- **VP (Verb Phrase)**: `<VB.*><NP|PP>*` - Verb followed by noun phrases or prepositional phrases
- **CLAUSE**: `<NP><VP>` - Noun phrase followed by verb phrase""")

code_cell = nbf.v4.new_code_cell("""from nltk import RegexpParser

# Define grammar for chunking
grammar = r'''
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
'''

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Sample sentence for chunking
sample_sentence = "The quick brown fox jumps over the lazy dog"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sample_sentence)
pos_tags = nltk.pos_tag(tokens)

print("POS Tags:")
print(pos_tags)
print("\\n" + "="*50 + "\\n")

# Parse the sentence into chunks
chunked_tree = chunk_parser.parse(pos_tags)

print("Chunked Tree:")
print(chunked_tree)
print("\\n" + "="*50 + "\\n")

# Pretty print the tree structure
print("Tree Structure:")
chunked_tree.pretty_print()

# Note: In a Jupyter notebook, you can also visualize with:
# chunked_tree.draw()  # This opens a GUI window
""")

explanation_cell = nbf.v4.new_markdown_cell("""### Explanation

- **NP**: Groups determiners, adjectives, and nouns (e.g., "The quick brown fox")
- **PP**: Groups prepositions with their noun phrases (e.g., "over the lazy dog")
- **VP**: Groups verbs with their arguments
- **CLAUSE**: Represents the overall sentence structure

Chunking helps in extracting meaningful phrases from text, which is useful for information extraction, question answering, and other NLP applications.""")

# Append the cells at the end
nb.cells.append(markdown_cell)
nb.cells.append(code_cell)
nb.cells.append(explanation_cell)

# Save the notebook
nbf.write(nb, 'NLP_Workshop_Starter.ipynb')

print("Chunker section added to the notebook.")

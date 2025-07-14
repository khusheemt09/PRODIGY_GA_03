**Markov Chain Text Generator** 
This project implements a Markov Chain-based text generator using Python. The program reads a large text file as input and builds a trigram language model (three-word sequences) to learn how words commonly follow each other in the text.

When given a starting phrase of three words, the generator predicts the next words probabilistically, producing coherent text by selecting likely words based on the learned trigram patterns. The generation continues until a sentence-ending punctuation mark (., !, or ?) is reached or a maximum word limit is met.

**Key Features:**
Trigram Model: Uses sequences of three words to predict the next word, which improves grammatical coherence over simpler models.

Sentence Boundary Awareness: Stops generating text at sentence-ending punctuation to create natural-sounding sentences.

User Input: Allows users to input any 3-word starting phrase existing in the source text to generate contextually relevant output.

Randomness: Randomly picks next words among possible options to produce varied and creative sentences each run.

Easy to Customize: Works with any input text file, so you can train it on books, articles, or custom datasets.


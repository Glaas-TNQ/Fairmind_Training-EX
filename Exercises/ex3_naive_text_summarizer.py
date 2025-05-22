# Exercise 3: Naive Text Summarizer using NLTK
# --------------------------------------------
# This simple NLP script extracts the first two sentences from a given text.
# As an NLP expert, you are expected to enhance the summarization strategy
# using token weighting, semantic analysis, or transformer-based models.

import nltk

class TextAnalyzer:
   def __init__(self, text):
       self.text = text
       
   def summarize(self):
       sentences = nltk.sent_tokenize(self.text)
       return ' '.join(sentences[:2])

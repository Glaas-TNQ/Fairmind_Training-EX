import nltk

class TextAnalyzer:
   def __init__(self, text):
       self.text = text
       
   def summarize(self):
       sentences = nltk.sent_tokenize(self.text)
       return ' '.join(sentences[:2])

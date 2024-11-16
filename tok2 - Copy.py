import nltk  
nltk.download('all') 
from nltk.tokenize import word_tokenize  

text1 = "This is an example sentence."  
words = word_tokenize(text1)  
print(words)  
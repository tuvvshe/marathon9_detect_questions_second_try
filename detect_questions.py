from nltk.tokenize import word_tokenize
question_words = ["what", "why","when",
                   "where", "name",
                    "is", "has", "have",
                     "whom", "whose",
                      "should", "could", "does",
                       "which", "do", "how", "are",
                       "have", "don't"]

question = input ("INPUT A SENTENCE: ")
question = question.lower()
question = word_tokenize(question)

if any(x in question[0] for x in question_words):
    print("THIS IS A QUESTION!!!")
else:
    print("THIS IS NOT A QUESTION!!!!!")
    
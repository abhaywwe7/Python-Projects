from textblob import TextBlob
wrong_words = ['joek', 'artfical intelgence']
print("The wrong words are:\n", wrong_words)
correct_words = []
for i in wrong_words:
    correct_words.append(TextBlob(i))

print("The correct words are:")
for i in correct_words:
    print(i.correct(), end="\n")

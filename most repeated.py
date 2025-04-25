text = "apple orange banana apple apple orange"
words = text.split()
most = max(words, key=words.count)
print("Most repeated word:", most)
print("Count:", words.count(most))

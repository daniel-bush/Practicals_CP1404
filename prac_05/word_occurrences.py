"""Word_occurrences.py task."""

sentence = input("Text: ").lower()
words = sentence.split(" ")
word_dict = {}

for word in words:
    frequency = word_dict.get(word, 0)
    word_dict[word] = frequency + 1

words = list(word_dict.keys())
words.sort()

max_word_length = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, max_word_length, word_dict[word]))



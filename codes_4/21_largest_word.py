def largest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

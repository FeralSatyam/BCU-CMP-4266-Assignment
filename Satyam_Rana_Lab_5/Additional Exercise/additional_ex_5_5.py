#5.5
def word_frequencies(list_a):
    freq = {}
    for word in list_a:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

print(word_frequencies(["apple", "banana", "apple", "orange", "banana", "apple"]))
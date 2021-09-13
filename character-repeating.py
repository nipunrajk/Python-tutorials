# find the most repeated character in the sentence
from pprint import pprint
sentence = 'This is a common interview question'

char_freqency = {}
for char in sentence:
    if char in char_freqency:
        char_freqency[char] += 1
    else:
        char_freqency[char] = 1

pprint(char_freqency, width=1)

char_freqency_sorted =sorted(char_freqency.items(),
                             key=lambda key:key[1],
                             reverse=True)
print(char_freqency_sorted[0])

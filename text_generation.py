import re


# Избавление от неалфавитных знаков, сплитит их в лист
def tokenize(string):
    return list(map(str, re.sub(r'[^\w]', ' ', string).split()))


#  Перевод всего в нижний регистр
def make_lowercase(word_list):
    return [string.lower() for string in word_list]


raw = str(input())
m = make_lowercase(tokenize(raw))

word_dict = {}

for word, next_word in zip(m, m[1:]):
    if word not in word_dict.keys():
        word_dict[word] = [next_word]
    else:
        word_dict[word].append(next_word)

print(word_dict)

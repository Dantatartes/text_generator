import re
from numpy.random import randint, choice


class TextGenerator:

    def __init__(self):
        self.word_dict = {}
        pass

    def fit(self, raw_text):
        m = make_lowercase(tokenize(raw_text))
        for word, next_word in zip(m, m[1:]):
            if word not in self.word_dict.keys():
                self.word_dict[word] = [next_word]
            else:
                self.word_dict[word].append(next_word)

    def generate(self, size=randint(7, 14)):
        try:
            current_word = choice(list(self.word_dict.keys()))
            sentence = f"{current_word} "
            for i in range(size):
                new_word = choice(self.word_dict[current_word])
                sentence = f"{sentence}{new_word} "
                current_word = new_word
            return sentence
        except ValueError:
            print("You haven't fitted the data to TextGenerator or it was an empty string")


# Избавление от неалфавитных знаков, сплит их в лист
def tokenize(string):
    return list(map(str, re.sub(r'[^\w]', ' ', string).split()))


#  Перевод всего в нижний регистр
def make_lowercase(word_list):
    return [string.lower() for string in word_list]


raw = str(input())
generator = TextGenerator()
generator.fit(raw)
print(generator.generate())

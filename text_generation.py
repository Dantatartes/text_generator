import re


class TextGenerator:
    word_dict = {}

    def __init__(self):
        pass

    def fit(self, raw_text):
        m = make_lowercase(tokenize(raw_text))
        for word, next_word in zip(m, m[1:]):
            if word not in self.word_dict.keys():
                self.word_dict[word] = [next_word]
            else:
                self.word_dict[word].append(next_word)

    def generate(self):
        return self.word_dict


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

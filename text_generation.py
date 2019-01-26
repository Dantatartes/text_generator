import re
from random import randint, choice


class TextGenerator:

    def __init__(self):
        self.__word_dict = {}
        pass

    def fit(self, file):
        def tokenize(string):
            return list(map(str, re.sub(r'[^a-zA-Zа-яА-Я]+', ' ', string).split()))

        def make_lowercase(word_list):
            return [string.lower() for string in word_list]
        try:
            with open(file, 'r') as f:
                m = f.read()
                f.close()
            m = make_lowercase(tokenize(m))
            for word, next_word in zip(m, m[1:]):
                if word not in self.__word_dict.keys():
                    self.__word_dict[word] = [next_word]
                else:
                    self.__word_dict[word].append(next_word)
        except FileNotFoundError as e:
            print(e)

    def generate(self, size=randint(7, 14)):
        try:
            current_word = choice(list(self.__word_dict.keys()))
            sentence = f"{current_word} "
            for i in range(size):
                new_word = choice(self.__word_dict[current_word])
                sentence = f"{sentence}{new_word} "
                current_word = new_word
            return sentence
        except (ValueError, IndexError):
            print("You haven't fitted the data to TextGenerator or it was an empty string")

    def save_model(self):
        with open("saved_model.csv", 'w') as f:
            for key in list(self.__word_dict.keys()):
                f.write(f"{key},{self.__word_dict[key]}\n")


generator = TextGenerator()
generator.fit("constitution.txt")
print(generator.generate())

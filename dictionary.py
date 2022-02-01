import copy
from finder import Finder


class Dictionary:
    def __init__(self, dict_file):
        self.words = Dictionary.get_words(dict_file)
        self.values = Dictionary.get_values(self.words)
        self.dictionary = [self.words, self.values]

    # Remove words with character from dictionary
    def exclude(self, chars: str) -> None:
        for item in copy.deepcopy(self.dictionary[0]):
            matched_list = [characters in chars for characters in item]
            if True in matched_list:
                del_index = self.dictionary[0].index(item)
                del self.dictionary[0][del_index]
                del self.dictionary[1][del_index]

    # Get words that contain character
    # index -> enforce whether character is or isn't at specified index as determined by:
    # include -> default to true

    def include(self, char: str, index: int = None, include: bool = True) -> None:
        for item in copy.deepcopy(self.dictionary[0]):
            matched_list = [characters in char for characters in item]
            if index is not None:
                if (True not in matched_list) or (matched_list[index] is not include):
                    del_index = self.dictionary[0].index(item)
                    del self.dictionary[0][del_index]
                    del self.dictionary[1][del_index]
            elif True not in matched_list:
                del_index = self.dictionary[0].index(item)
                del self.dictionary[0][del_index]
                del self.dictionary[1][del_index]

    def print(self, numbers=False):
        if numbers:
            print(self.dictionary, "\n")
        else:
            print(self.dictionary[0], "\n")

    def reset(self):
        self.dictionary = self.words

    def GetGreatestWord(self):
        return self.dictionary[0][self.dictionary[1].index(max(self.dictionary[1]))]

    # Read from dictionary file to array
    @staticmethod
    def get_words(dict_file) -> list:
        with open(dict_file, 'r') as f:
            words = []
            for line in f:
                list_l = line.strip()
                if len(list_l) == 5:
                    words.append(list_l.lower())
            return words

    @staticmethod
    def get_values(words: list) -> list[int]:
        values = []
        for word in words:
            values.append(Finder.calculate_weight(word))
        return values

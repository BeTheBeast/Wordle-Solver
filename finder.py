# Based off percentage of use in English Dictionary
weight = \
    {
        "a": 8.34,
        "b": 1.54,
        "c": 2.73,
        "d": 4.14,
        "e": 12.6,
        "f": 2.03,
        "g": 1.92,
        "h": 6.11,
        "i": 6.71,
        "j": 0.23,
        "k": 0.87,
        "l": 4.24,
        "m": 2.53,
        "n": 6.80,
        "o": 7.70,
        "p": 1.66,
        "q": 0.09,
        "r": 5.68,
        "s": 6.11,
        "t": 9.37,
        "u": 2.85,
        "v": 1.06,
        "w": 2.34,
        "x": 0.2,
        "y": 2.04,
        "z": 0.06,
    }


class Finder:
    @staticmethod
    def calculate_weight(string: str) -> int:
        string = "".join(dict.fromkeys(string))  # removes repeat characters to encourage more information gathering
        w = 0
        for character in string:
            w += weight.get(character)
        return w

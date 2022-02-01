from dictionary import Dictionary

Dict = Dictionary('dictionary.txt')
TempDict = Dictionary('dictionary.txt')

first_guess = "atone"  # highest value in dictionary 44.81 -- inversely "yucky" is the worst 5.6
guessed = set(first_guess)

"""

- = Not in : Gray Square
x = In but incorrect index : Yellow Square
X = In and correct index : Green Square

end = stops program

example Input:
    -x--X-
"""


def check_input(in_str: str) -> bool:
    for item in in_str:
        matched_list = [characters in "-xX" for characters in item]
        if False in matched_list:
            return False
        return True


def GetInput() -> str:
    while True:
        in_ = input("Enter Wordle Response: ")
        in_.replace(" ", "")
        if in_ == "end":
            return in_
        if len(in_) == 5:
            if check_input(in_):
                return in_
            print("Invalid input - character not -xX or end")
        else:
            print("Invalid Input - wrong size\n")


ex: bool = False


def main() -> None:
    Guess: str = "later"
    tries: int = 0
    global ex
    print("Guess: ", Guess, "\n")
    while True:
        if len(Dict.dictionary[0]) <= 1:
            print("final: ")
            Dict.print()
            return
        if len(Dict.dictionary[0]) <= 6 - tries:
            print("One of these is the answer: ")
            Dict.print()
            return
        in_ = GetInput()
        if in_ == "end":
            print("Current List: ")
            Dict.print()
            return

        last_dict = TempDict.dictionary
        index = 0
        for char in Guess:
            if in_[index] == "-":
                exclude(char)
            elif in_[index] == "x":
                include([char, index, False], tries)
            elif in_[index] == "X":
                include([char, index, True], tries)
            index += 1
        tries += 1
        if len(TempDict.dictionary[0]) >= 1 and not ex:
            try:
                Guess = TempDict.GetGreatestWord()
                print("Guess: ", Guess, "\n")
            except:
                print("error occurred!\n")
                TempDict.print()
        else:
            Guess = Dict.GetGreatestWord()
            print("Guess: ", Guess, "\n")
            ex = True


vowels = "aeiou"

# TODO make logic find best word based off available characters. Not Just off of percentage weight.


def exclude(char: str) -> None:
    Dict.exclude(char)
    if not ex:
        TempDict.exclude(char)


# info : (char, index, include)
def include(info: list, tries: int) -> None:
    Dict.include(info[0], info[1], info[2])
    if info[0] and not ex:
        TempDict.exclude(info[0])


if __name__ == '__main__':
    main()

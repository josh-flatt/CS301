# Day 1 - Josh Flatt
# 1/10/2023


# Helper functions
def get_english_words() -> list:
    english_dictionary_file = open("words.txt")
    return list(line.strip() for line in english_dictionary_file)


# Question 1
def sum_of_n_positive_ints(n: int) -> int:
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

# print(sum_of_n_positive_ints(10))


# Question 2
def is_english_word(my_word: str) -> bool:
    """
    Returns True if passed word is present in the english dictionary.
    Otherwise, returns False.
    """
    english_words = get_english_words()
    for word in english_words:
        if my_word == word:
            return True
    return False

# print(is_english_word("mister"))


# Question 3
def is_word_creatable(tiles: list, word: str) -> bool:
    """
    Returns True if the input word can be created
    using the letters available in the list.
    Otherwise, returns False.
    """
    temp_tiles = tiles.copy()
    for letter in word:
        if letter in temp_tiles:
            temp_tiles.remove(letter)
        elif letter not in temp_tiles:
            return False
    return True

# test = ["w", "r", "d", "o"]
# print(check_tiles_against_word(test, "word"))


# Question 4
def make_words_using_all_tiles(tiles: list) -> set:
    """
    Returns set with all possible english words that can be created
    using all of the tiles that are passed.
    """
    english_words = get_english_words()
    solutions = set()
    for word in english_words:
        if len(word) != len(tiles):
            continue
        if is_word_creatable(tiles, word):
            solutions.add(word)
    return solutions

print(make_words_using_all_tiles(["r", "e", "t", "a", "i", "n", "s"]))
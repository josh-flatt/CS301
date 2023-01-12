# Day 1 - Josh Flatt
# 1/10/2023

# Question 1
def sum_of_n_positive_ints(n: int) -> int:
    sum = 0
    for i in range(n):
        sum += i
    return sum

print(sum_of_n_positive_ints(1))


# Question 2
def is_english_word(my_word: str) -> bool:
    english_dictionary_file = open("words.txt")
    english_words = list(line.strip() for line in english_dictionary_file)
    for word in english_words:
        if my_word == word:
            return True
    return False

print(is_english_word("mister"))


# Question 3
def check_tiles_against_word(tiles: list, word: str) -> bool:
    for letter in word:
        if letter not in tiles:
            return False
    return True

test = ["w", "r", "v", "o"]
print(check_tiles_against_word(test, "word"))


# Question 4
def make_words_with_tiles(tiles: list) -> set:
    english_dictionary_file = open("words.txt")
    english_words = list(line.strip() for line in english_dictionary_file)
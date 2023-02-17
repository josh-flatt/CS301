# Day 1 - Josh Flatt
# 1/10/2023


# Helper functions
def get_english_words(filtering_letter: chr = None) -> list:
    """
    Parameters:
        filtering_letter -> specified letter that all words must contain.
                            If left blank, no filter applied.
    About:
        Pulls all English words out of a text file, and returns only what is applicable.
    Returns:
        set -> all words from text file that contain specified filtering letter.
    """
    english_dictionary = list()
    english_dictionary_file = open("words.txt")
    if filtering_letter == None:
        return list(line.strip() for line in english_dictionary_file)
    for line in english_dictionary_file:
        if filtering_letter in line:
            english_dictionary.append(line.strip())
    return english_dictionary
        

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
        else:
            return False
    return True

# test = ["w", "r", "d", "o"]
# print(is_word_creatable(test, "word"))


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

# print(make_words_using_all_tiles(["r", "e", "t", "a", "i", "n", "s"]))


# Question 5
def spelling_bee_words(center: chr, letters: list) -> set:
    """
    Parameters:
        center  -> singular letter that must appear in all words
        letters -> list of letters that are used in words, but not required
    About:
        Collects all possible English solutions to Spelling Bee game.
    Returns:
        set -> all possible English solutions to Spelling Bee game.
    """
    possible_words = set()
    english_words = get_english_words(center)
    for word in english_words:
        if is_word_valid(letters, word):
            possible_words.add(word)
    return possible_words

def is_word_valid(letters: list, word: str) -> bool:
    """
    Parameters:
        letters -> list of letters to check against word.
        word    -> English word to check against letters.
    About:
        Checks to see if the input word can be made using the input list of letters.
        Also checks to see if the input word is 5 characters or longer (Game rule).
    Returns:
        bool -> whether or not the word is a valid solution.
    """
    min_allowed_size = 5
    if len(word) < min_allowed_size:
        return False
    for letter in word:
        if letter not in letters:
            return False
    return True

def spelling_bee_score(center: chr, letters: list) -> int:
    """
    Parameters:
        center  -> singular letter that must appear in all words
        letters -> list of letters that are used in words, but not required
    About:
        Calculates the total score of all of the valid word solutions.
    Returns:
        int -> final score from game.
    """
    score = 0
    words_possible = spelling_bee_words(center, letters)
    for word in words_possible:
        score += single_word_score(letters, word)
    return score
            
def single_word_score(letters: list, word: str) -> int:
    """
    Parameters:
        letters -> list of letters to check against word.
        word    -> English word to check against letters.
    About:
        Checks to see if the input word uses all of the input letters.
        Also prints each word and associated point value.
    Returns:
        int -> score of individual word.
    """
    temp_letters = letters.copy()
    reg_score = 1
    bonus_score = 3
    for letter in word:
        if letter in temp_letters:
            temp_letters.remove(letter)
    if len(temp_letters) == 0:
        print(f"{word} (3 pts)")
        return bonus_score
    print(f"{word} (1 pt)")
    return reg_score
    
# print(spelling_bee_words("l", ["a", "b", "c", "i", "n", "r", "l"]))
# print(spelling_bee_score("l", ["a", "b", "c", "i", "n", "r", "l"]))


# Question 6
def bingo():
    english_words = get_english_words()
    applicable_words = list()
    tile_count_for_bingo = 8
    for word in english_words:
        if len(word) == tile_count_for_bingo:
           applicable_words.append(word)
    return applicable_words
# Unfinished - only filters down to the words of length 8

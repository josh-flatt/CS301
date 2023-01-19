####
####
####  Code for discussion
####
####       CS 301
####    Jan 17, 2023
####
####



####################
###              ###
###  Question 2  ###
###              ###
####################

## Version 2A  ##

def Problem2(n):
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if(word == n): 
            return True
            break
    return False

## Version 2B  ##

words = []                 # place words in list

fin = open('words.txt')    # read file
for line in fin:           # for each line in file
  word = line.strip()      # strip the line for word only
  words.append(word)

"""2.) Given a proposed word that someone wants to play, can you check that it is a valid word?"""

def isValid1(inpWord, wordList): #Built-in (probably linear search)
  if inpWord in wordList:
    return True
  else:
    return False

## Version 2C  ##

"""
NUMBER 2

The is_it_valid function takes in a string as its input and checks if the word is in the word list
"""

def is_it_valid(word):
    #for i in range(len(word_list)):
        if word.upper() in word_list:  # verifies if word is in the word list
            return True, print("This is a valid word")
        else:
            return False, print("This is not a valid word.")

# Test
#print(is_it_valid("aardvark"))
#print(is_it_valid("railcar"))

## Version 2D  ##

#Problem2
def searchForWord(word, low, high, words):# A binary search for a word. Give a word and then look through a list of most words in the english language, to see if it is a word.
    if high >= low:
        mid = (low+high)//2# Gets the midpoint of the range
        if words[mid].lower() == word.lower():# If the word matches with a word in the list at the midpoint the function returns True
            return True
        elif words[mid].lower() > word.lower():# If the word at the midpoint is greater than the given word call the function again with change of bounds
            return searchForWord(word, low, mid-1, words)
        elif words[mid].lower() < word.lower():# If the word at the midpoint is less than the given word call the function again with change of bounds
            return searchForWord(word, mid+1, high, words)
        else:# If the word is not in the list return false
            return False
    else:
        return False

####################
###              ###
###  Question 3  ###
###              ###
####################

## Version 3A  ##

#3
def checkWord(tiles, word):
    for letter in word:
        if letter not in tiles:
            return False
        else:
            tiles.remove(letter) #remove the letter from tiles in case of repeated letters
    return True

## Version 3B  ##

#############################################################################
#                     Assignment 1 : Scrabble Problems                      #
#                                                                           #
# PROGRAMMER:  XXXXXXXXXXXXXX                                               #
# DATE:        1/15/2023                                                    #
# SEMESTER:    Spring 2023                                                  #
# CLASS:       CS301-002                                                    #
# INSTRUCTOR:  Dr. Nathaniel Miller                                         #
#                                                                           #
# DESCRIPTION                                                               #
# The following program contains my initial solutions to the algorithm      #
# problems prompted by the given instructions. A main block is provided     #
# below the function definitions to test the program. Note: Tiles must be   #
# given as a list of lowercase letters, and words.txt must be in the same   #
# directory as main.py                                                      #
#                                                                           #
# COPYRIGHT:                                                                #
# This program is copyright (c)2023 XXXXXXXXXXXXX and Dr. Nathaniel Miller. #
#                                                                           #
#############################################################################

#############################################################################
# Question 3 - Given a set of tiles and a word, can you check if the word   #
# can be made from the tiles?                                               #
#############################################################################

def word_assemble(tiles, test_word):
    """Accepts a list and a string, one containing the set of tiles and the 
    other the word to spell. Recursively calls itself, removing a tile from
    the list and its letter from the word every recursion. Stops and returns
    true when the base case of an empty string is reached, or is returned false.
    """
    if test_word == "":
        return True
    elif test_word[0].lower() in tiles: # If there is a tile that matches the first letter of the word.
        tiles.remove(test_word[0].lower())         # Tile in word is removed from tileset.
        return word_assemble(tiles, test_word[1:]) # New tileset and shorter word is recursively called.
    else:
        return False

## Version 3C  ##

#Takes two arguments meant to be a list and a string
def wordFromTiles(tiles, word):
    #Compares lengths in order to save time going through the loops
    if len(tiles) != len(word):
        print("The number of tiles and the length of the word are not equal.")
        print()
        return False
    else:
        canBeMade = False
        tileTaken = False
        #Loops through the words and tiles and sees if there are any equal pairs
        for i in word:
            for j in tiles:
                if i == j:
                    tileTaken = True
                    break
            if tileTaken:
                #If a pair is found the tile will be removed from play since
                #it's been used
                tiles.remove(i)
                tileTaken = False
        if len(tiles) == 0:
            print("This word can be made with these tiles!")
            print()
            return True
        else:
            print("This word cannot be made with these tiles :(")
            print()
            return False

## Version 3D  ##

def count_letters(test_word):
    lower_test_word = test_word.lower()
    letter_count_list = list([0] * 29)
    total_letters = 0
    for char in lower_test_word:
        total_letters += 1
        char_code = ord(char) - 97
        letter_count_list[char_code] += 1
    letter_count_list[26] = total_letters
    letter_count_list[27] = lower_test_word
    return letter_count_list


def generate_letter_count_list():
    fin = open('words.txt')
    counted_list = list()
    line_count = 0
    for line in fin:
        word = line.strip()
        counted_list.append(count_letters(word))
        counted_list[line_count][28] = line_count
        line_count += 1
    return counted_list


def check_if_anagram(test_word_list, check_word_list):
    for x in range(26):
        if test_word_list[x] != check_word_list[x]:
            return False
    return True


def check_if_creatable(test_word_list, check_word_list):
    for x in range(26):
        if test_word_list[x] >= check_word_list[x]:
            return False
    return True

## Version 3E ##

"""
NUMBER 3

The check_tiles function takes in two inputs, with one representing a set of tiles and the other a word. 
This function loops through each tile and checks if it is in the word. If so, the tile is added check_word.
The function ends by checking if the original word is equal to check_word, returning
True if they are and False if they are not. 
"""

def check_tiles(tiles, word):
    word = list(word.upper())
    check_word = []
    for i in range(len(tiles)):  # Determines of the word can be made from the tiles
        if tiles[i].lower() in word or tiles[i].upper() in word:  # I could also try tiles.upper() after line 78
            check_word.append(tiles[i].upper())
            if word.count(tiles[i]) < check_word.count(tiles[i]):
                check_word.remove(tiles[i])
    word.sort()
    check_word.sort()  #both lists are now in the same order. Test by returning word, check_word
    if check_word == word:
        return True
    else:
        return False


# Test
# print(check_tiles(["S", "E", "R", "N", "T", "I", "A"], "RETINaS"))
# print(check_tiles(["S", "E", "R", "N", "T", "I", "A"], "RETINAS"))





####################
###              ###
###  Question 4  ###
###              ###
####################

## Version 4A  ##

#4
from itertools import permutations
def findWords(tiles):
  listOfWords=[]
  fin = open('words.txt')
  for line in fin:
    w = line.strip()
    if len(w)==len(tiles):
      listOfWords.append(w)

  perms = permutations(tiles)
  listTileWords =[]
  for x in list(perms):
    if len(x)==7:
      tileWords = x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]
      listTileWords.append(tileWords)
  i=0
  while i<len(listTileWords):
    if listTileWords[i] not in listOfWords:
      listTileWords.remove(listTileWords[i])
      i=i-1
    else:
      print('')
    i=i+1
  return listTileWords

findWords(['r','e','t','a','i','n','s'])

## Version 4B  ##
#Problem4
def rearange(tiles, words):# Given a set of tiles, find all the possible words that can be made from those tiles.
  tiles = tiles.lower()
  perm = ["".join(p) for p in permutations(tiles)]# Get the permutations of the tiles and make a list of all those permuations
  validWords = [word for word in perm if searchForWord(word, 0, len(words)-1, words)]# Make a list of the permutations that actually made words.
  return validWords

## Version 4C  ##
  
#4 returns all the words from the list that can be made from given tiles
def findWords(tilesStr):
    fin = open("words.txt")
    tiles= set (tilesStr)
    listOfWords=[]
    for word in fin.read().split():
        if len(word)== len(tiles):  # only add words with same length as tiles
            check = 0 not in [ c in word for c in tiles]  # all tiles are used
            if check == 1:
                    listOfWords.append(word)    # add word to wordlist if true
    return listOfWords

## Version 4D  ##


"""
NUMBER 4

The check_words function takes in two inputs, one being the set of tiles and the other being the list of english words.
The function checks if a word in the word list can be made from the tiles by calling the check_tiles function. 
If the tiles do make a word, then it adds that word to the answer list and increments the counter by 1. It then 
returns the complete list of answers and how many answer there are. 
"""

def check_words(tiles, wordlist):
    answers = []
    counter = 0
    tiles.sort()
    for word in wordlist:  # Check if each word in wordlist can be made from the letters
        if check_tiles(tiles, word) == True:
            answers.append(word)
            counter += 1
    return (print("There are " + str(counter) + " potential words. They are: " + str(answers)))


# Test
# check_words(["S", "E", "R", "N", "T", "I", "A"], word_list)





####################
###              ###
###  Question 5  ###
###              ###
####################

## Version 5A  ##

def spellingBee(outerLetters = "", innerLetter = '', wordsAsList = []): # checks if each character in each word is in the key letters
    resultWords = []
    wordWorks = True
    hasInnerLetter = False
    for each in wordsAsList:
        wordWorks = True
        hasInnerLetter = False
        for char in each:
            if (char not in outerLetters and char not in innerLetter) and wordWorks: #checks if word has letters that aren't in our key
                wordWorks = False
            if char in innerLetter: #checks if the word has the required inner letter
                hasInnerLetter = True
        if wordWorks and len(each) >= 5 and hasInnerLetter: #only adds to returned list if it only has letters in our key, has the inner letter at least once, and is 5 or longer
            resultWords.append(each)
    return resultWords

## Version 5B  ##
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

## Version 5C  ##

#Problem5
def spelling_bee(outer_letters, center_letter, words):# Function to tell you all words for a puzzle
  outer_letters = outer_letters.lower()
  center_letter = center_letter.lower()
  words = [word for word in words if len(word) >= 5 and len(word) <= 7]
  five_letters = ["".join(p) for p in product(outer_letters + center_letter, repeat = 5) if center_letter in p and searchForWord("".join(p), 0, len(words), words)]# Takes all the letters and takes the cartesian product(nested for loop), #so there can be repeated letters. 
                                                                                                                                                                   #Makes sure that the center letter is in the word, and then checks so see if it is a word.
  six_letters = ["".join(p) for p in product(outer_letters + center_letter, repeat = 6) if center_letter in p and searchForWord("".join(p), 0, len(words), words)]# The same but for six letter words.
  seven_letters = ["".join(p) for p in product(outer_letters + center_letter, repeat = 7) if center_letter in p and searchForWord("".join(p), 0, len(words), words)]# Seven letter words.
  all_words = five_letters + six_letters + seven_letters# puts all the words into one list and returns it.
  return all_words





####################
###              ###
###  Question 6  ###
###              ###
####################

## Version 6A  ##

#this one takes about 8 minutes to run, didn't formally time it
def findBingos1(wordsAsDict = {}): #gets all 8 letter words from word list, adds to a list, calls findAllWords1 with each 8 letter word, and saves best
    eightLetterWords = []
    for each in wordsAsDict:
        if (len(each) == 8):
            eightLetterWords.append(each)
    ##print(len(eightLetterWords)) #prints the total number of 8 letter words in wordList (26447)
    total8 = len(eightLetterWords)
    bestNum = 0
    bestLetters = set()
    count = 0
    for each in eightLetterWords:
        tmp = len(findBingosHelper(each, wordsAsDict)) #gets each 8 letter permutation of each that is another word, and takes the number of occurrences, this is where most time is spent
        if tmp > bestNum:
            bestLetters.clear()
            bestNum = tmp
            bestLetters.add(each)
            print(f"New best! {bestNum}, {bestLetters}") #print statement to keep track of current progress since this takes a while, can be commented out
        elif tmp == bestNum:
            bestLetters.add(each)
            print(f"Tied best! {bestNum}, {each}") #print statement to keep track of current progress since this takes a while, can be commented out
        count+=1
        if count % 1000 == 0:
            print(f"At {count} words tested. {(round((count/total8)*100, 2))}% Done."
                  + f"Current best letters: {bestLetters}") #print statement to keep track of current progress since this takes a while, can be commented out
    return bestLetters

#another iteration, that saves used items in a set, and checks before calling findBingosHelper
#not formally timed, but seems to be a little faster than findBingos1, but not as fast as expected
#this one also gets rid of the duplicate found in findBingo1
def findBingos2(wordsAsDict = {}): #gets all 8 letter words from word list, adds to a list, calls findBingosHelper with each 8 letter word if it wasn't already returned, and saves best
    eightLetterWords = []
    for each in wordsAsDict:
        if (len(each) == 8):
            eightLetterWords.append(each)
    ##print(len(eightLetterWords)) #prints the total number of 8 letter words in wordList (26447)
    total8 = len(eightLetterWords)
    bestNum = 0
    bestLetters = set()
    count = 0
    used = set() #set to save anagrams of each 8 letter word
    for each in eightLetterWords:
        if not each in used:
            tmpSet = (findBingosHelper(each, wordsAsDict)) #gets each 8 letter permutation of each that is another word, this is where most time is spent
            used = used.union(tmpSet)
            tmp = len(tmpSet)
        else:
            tmp = 0
        if tmp > bestNum:
            bestLetters.clear()
            bestNum = tmp
            bestLetters.add(each)
            print(f"New best! {bestNum}, {bestLetters}") #print statement to keep track of current progress since this takes a while, can be commented out
        elif tmp == bestNum:
            bestLetters.add(each)
            print(f"Tied best! {bestNum}, {each}") #print statement to keep track of current progress since this takes a while, can be commented out
        count+=1
        if count % 1000 == 0:
            print(f"At {count} words tested. {(round((count/total8)*100, 2))}% Done."
                  + f"Current best letters: {bestLetters}") #print statement to keep track of current progress since this takes a while, can be commented out
    return bestLetters

#only took about a second to run, multiset method
def findBingos3(wordsAsDict = {}): #gets each 8 letter word, alphabtizes their string so the same letters are equivalent, then adds them to a multiset since it keeps track of number of occurences
    eightLetterWords = []
    for each in wordsAsDict:
        if (len(each) == 8):
            eightLetterWords.append(each)#get every 8 letter word
    multisetOfWords = Multiset()#see comment on import statement for multiset library
    best = []
    bestNum = 0
    for each in eightLetterWords:
        multisetOfWords.add("".join(sorted(each)))#alphabetize strings and add to multiset
    for each in eightLetterWords:
        each = "".join(sorted(each))
        if multisetOfWords.get( element = each, default = -1) > bestNum:#check which item in the multiset has the highest multiplicity -- I couldn't find an easy way to get highest mult item without going through entire multiset
            best = each
            bestNum = multisetOfWords.get( element = each, default = -1)
    return best
    

#Bingos helper method, same as find all words, with possibility to be anything less than max length removed for faster run time      
def findBingosHelper(tiles = "", wordsAsDict = {}): #gets all permutations, gets substrings for each perm, checks if each substring is already in set, adds if it isn't
    realWords = set()
    combos = ["".join(each) for each in itertools.permutations(tiles)] #Gets a list containing every possible permutation of tiles --- this is likely the slowest line of code
    for each in combos:
        if(isValid4(each, wordsAsDict)): #uses previously created method to check validity -- uses dictionary check
            realWords.add(each)
    return realWords

## Version 6B  ##

#Problem6
def order_words(word):# Function to rearange the letters in a string into alphabetical order.
  li = []
  for letter in word:# Makes the letters of the string into a list.
    li.append(letter)
  li.sort()# Sorts the list into alphabetical order.
  return ''.join(li)# returns a string with the letter in alphabetical order.

def bingo(words):# Takes a list of the words from the text file, and finds the set(s) of eight letters that from the most possible bingos
  words_list = [order_words(word) for word in words if len(word) == 8]# Created a set of all the eight letter words from the list of words. Also calls order_words to rearange the letters in the words alphabetically.
  words_list.sort()# Sorts the list into alphabetical order.
  words_set = set(words_list)# Makes a set of the list to remove duplicates
  dict = {}
  for word in words_set:# Iterate through all elements in the set and see how many times the element appears in the list, which will be the amount of bingos that set of eight letters can make.
    if words_list.count(word) > 5:# Will add the set of eight letters to the a dictionary as a key, with the number of words it can make as its value. Will only add sets that can make more than 5 words.
      dict[word] = words_list.count(word)
  return dict






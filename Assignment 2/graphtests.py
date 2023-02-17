import time
import csv
import random

def __generate_dictionary__(length: int) -> dict:
    test_dictionary = dict()
    midpoint = (length // 2) - 1
    test_dictionary["first_key"] = "a_value"
    for i in range(length - 2):
        if(i == midpoint):
            test_dictionary["middle_key"] = "a_value"
            continue
        rand_key = random.randint(1000, 9999)
        test_dictionary[rand_key] = "arbitrary_value"
    test_dictionary["last_key"] = "a_value"
    return test_dictionary

def build_dictionaries(n: int) -> dict:
    dicts_of_dicts = dict()
    for i in range(3, n + 1):
        dicts_of_dicts[i] = __generate_dictionary__(i)
    return dicts_of_dicts
    

def time_algorithm(name: str, function_name, n: int) -> None:
    with open("data.csv", "a+") as csvfile:
        myWriter = csv.writer(csvfile, delimiter=",", lineterminator="\r")
        for i in range(2, n):
            start_time = time.time_ns()
            tmp = function_name(i)
            end_time = time.time_ns()
            myWriter.writerow([f"{name}", f"{i}", f"{end_time - start_time}"])

def time_dictionary_functions(name: str, function_name, dict_of_dicts, key, n: int) -> None:
    with open("data.csv", "a+") as csvfile:
        myWriter = csv.writer(csvfile, delimiter=",", lineterminator="\r")
        for i in range(3, n):
            current_dict = dict_of_dicts[i]
            start_time = time.time_ns()
            tmp = function_name(current_dict, key)
            end_time = time.time_ns()
            myWriter.writerow([f"{name}", f"{i}", f"{end_time - start_time}"])


# O(N)
def runtime_n(n: int) -> int:
    total = 0
    for i in range(1,n+1):
        total += i
    return total

# O(n^2)
def runtime_n_sq(n: int) -> int:
    total = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            total += j
    return total


def pop_dict_value(dictionary: dict, key):
    return dictionary.pop(key)

def add_dict_value(dictionary: dict, key):
    dictionary[key] = "bogus_value"
    return True

def find_dict_value(dictionary: dict, key):
    if key in dictionary:
        return True
    return False

def clear_dict(dictionary: dict, key):
    dictionary.clear()
    return True

def copy_dict(dictionary: dict, key):
    new_dict = dictionary.copy()
    return new_dict



if __name__ == "__main__":
    
    for i in range(1000):
        dictionaries = build_dictionaries(250)
        # time_algorithm(f"O(n)", runtime_n, 100)
        # time_algorithm(f"O(n^2)", runtime_n_sq, 100)
        time_dictionary_functions(f"dict_find_key_in", find_dict_value, dictionaries.copy(), "middle_key", 250)
        time_dictionary_functions(f"dict_find_key_out", find_dict_value, dictionaries.copy(), "not_in_dictionary", 250)
        time_dictionary_functions(f"dict_insert", add_dict_value, dictionaries.copy(), "new_key", 250)
        time_dictionary_functions(f"dict_pop", pop_dict_value, dictionaries.copy(), "middle_key", 250)
        time_dictionary_functions(f"dict_clear", clear_dict, dictionaries.copy(), "arbitraryvalue", 250)
        time_dictionary_functions(f"dict_copy", copy_dict, dictionaries.copy(), "arbitraryvalue", 250)
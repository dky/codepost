# This assignment will require you to submit 4 separate files outlined below. Each file should have the following methods:

## arrays.py

[] get_min_val(list) -> integer
Get the minimum value in an array of integers (without using the built-in min function).
Ex: [1, 2, 3, 4] -> 1
square_integers(list) -> list
Given an array of integers, replace each value with its square.
Ex: [1, 2, 3] -> [1, 4, 9]
print_ever_other_in_reverse(list) -> list
Given an array of integers, print every other element beginning from the last element.
Ex: [1, 2, 3, 4] -> 4 ... 2
evens_only(list, list) -> list
Given two arrays, return only the even elements from both arrays.
Ex: [1, 2], [3, 4] -> [2, 4]
strings_length_2(list) -> list
Given a list of random data, returns a new list of only strings that are at least length 2.
Ex: [1, 2, 'a', 4.3, 'word', True] -> ['word']
prod_of_all_others(list) -> list
Given a list of integers, return a list that contains the product of all other numbers in the array except the number at the current index.
Ex: [1, 2, 3] -> [6, 3, 2]
dictionaries.py

most_common_element(array) -> integer
Get the most common value in an array of integers (you will need to use a dictionary).
Ex: [1, 2, 3, 4] -> 3
find_elements_by_occurence(array), integer -> array
Given an array and a number K, find all the elements that appear K times.
Ex: [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5], 3 -> [2]
neg_nums_only(array) -> dictionary
Given an array of integers, fill a dictionary with counts of negative numbers only.
Ex: [-4, -3, -3, -2, -2, -2, 4, 5, 6, 7, 7] -> {-4: 1, -3: 2, -2: 3}
times_string_appears(array, string) -> integer
Given an array of strings and a target string T, return how many times T appears in the list of strings.
["paste", "rate", "template"], "te" -> 4
num_of_integers(array) -> integer
Given a mixed array, return how many of its elements are integers.
Ex: ["a", 2, 3.06, "word"] -> 1
strings.py

reverse_string(string) -> string
Given a string, return a new string in reverse order.
Ex: "facebook" -> "koobecaf"
remove_vowels(string) -> string
Given a string, return a new string that is the original string with all vowels removed.
Ex: "google" -> "ggl"

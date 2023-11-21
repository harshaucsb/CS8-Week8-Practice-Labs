## Given the stubs for the following function 
## and the main program, complete the implementation.
## Finish the assert statements to properly
## assert the result shown below (be careful 
## with the types of the variables).

## Make sure that your asserts test
## different branches/cases.


# def get_dictionary_value(options, option):
#     """
#     get_dictionary_value() takes an dict (options) and a string (option).
#     The functions check if the dictionary is empty and if yes,
#     returns -1. If the dictionary is not empty, the function
#     checks if the option is in the dictionary and if yes,
#     returns the value associated with the option. If the option is not
#     in the dictionary, the function returns the options available separated by comma and space.
#     For example: If the dictionary is {'a': 1, 'b': 2, 'c': 3} and the option is 'b',
#     the function returns 2. If the option is 'd', the function returns
#     'The available options are - a, b, c'. If the fuction is called with an empty dictionary,
#     the function returns -1. Make sure to have different assert statements to test the function
#     than the ones provided above. Note: Please refer to Zybooks 7.10 for more information on dictionaries.
#     """
#     if len(options) == 0:
#         return -1
#     elif option in options:
#         return options[option]
#     else:
#         return_str = "The available options are - "
#         for key in options:
#             return_str += key + ', '
#         return return_str[:-2]

if __name__ == "__main__":
    ### Write 3 assert statements
    ### to test the function
    # assert get_dictionary_value({}, 'a') == -1
    # assert get_dictionary_value({'a': 1, 'b': 2, 'c': 3}, 'b') == 2
    # assert get_dictionary_value({'a': 1, 'b': 2, 'c': 3}, 'd') == 'The available options are - a, b, c'
    pass
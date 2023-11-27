## Given the stubs for the following function 
## and the main program, complete the implementation.
## Finish the assert statements to properly
## assert the result shown below (be careful 
## with the types of the variables).

## Make sure that your asserts test
## different branches/cases.


def reverse_list(data):
    """
    get_dictionary_value() takes an list (data).
    The functions check if the list is empty and if yes,
    returns -1. If the list is not empty, the function
    returns the list in reverse order.
    For example: If the list is ['ax', 'by', 'cz'], then the answer is ['cz', 'by', 'ax'],
    and if the list is of even size also, its reversed properly. If the fuction is called with an empty list,
    the function returns -1. Make sure to have different assert statements to test the function
    than the ones provided above and test it with both even and odd sized lists. Note: Please refer to Zybooks CA 8.1.1 for more information on dictionaries.
    """
    if len(data) == 0:
        return -1
    else:
        for i in range(len(data)//2):
            data[i], data[len(data)-i-1] = data[len(data)-i-1], data[i]
        return data

def replace_string(data):
    """
    replace_string() takes a string (data) as input.
    The function replaces "TTYL" to "talk to you later" if there are 
    any "TTYL" appears in the input string and returns the replaced new string.
    If the input is empty, function returns -1.
    If there is no "TTYL" occurance in the data, return "Nothing to replace"
    For example: If the input string is "Gotta go. I will TTYL.", the function should return 
    "Gotta go. I will talk to you later."
    """
    if not data:
        return -1
    elif 'TTYL' not in data:
        return "Nothing to replace"
    else:
        return data.replace('TTYL', 'talk to you later')

if __name__ == "__main__":
    ### Write 3 assert statements
    ### to test the function
    assert reverse_list([]) == -1
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    assert reverse_list(['ax', 'by', 'cz', 'df']) == ['df', 'cz', 'by', 'ax']
    assert replace_string("I want to TTYL today.") == "I want to talk to you later today."
    assert replace_string("") == -1
    assert replace_string("Invalid string") == "Nothing to replace"
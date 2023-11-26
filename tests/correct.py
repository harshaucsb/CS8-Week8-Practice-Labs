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

def slice_both_ends(word): # Based off of 8.7
    """
    slice_both_ends() takes a string.
    The function checks if the string is empty and if yes,
    returns -1. If the string is not empty, the function
    returns a slice of the string with the first and last quarter
    of the string removed.
    For example: If the string is 'Tortilla' then the function returns
    'rtil'. 
    """
    # STUB
    if len(word) == 0:
        return -1
    return word[int(len(word)/4):int(3*len(word)/4)]

if __name__ == "__main__":
    ### Write 3 assert statements
    ### to test the function
    assert reverse_list([]) == -1
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    assert reverse_list(['ax', 'by', 'cz', 'df']) == ['df', 'cz', 'by', 'ax']

    # Test slice_both_ends()
    assert slice_both_ends("") == -1
    assert slice_both_ends("Tortilla") == "rtil"
    assert slice_both_ends("Pomegranate") == "megran"
    assert slice_both_ends("cat") == "ca"
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

def username(s):
    """
    username() takes an string (s).
    The following program asks user to enter a user name with lower case letter, digits, and underscore only.
    If the input includes upper case letter, convert them into lower case.
    If the input has other unexpected characters (that are, not letters or digits or underscore), convert them into underscore.
    For instance, "9876ZyWx%$#@" returns "9876zywx____".
    For instance, "$#@" returns "___".
    Note: Please refer to Zybooks CA 8.4 for more information on incremental development
    """
    s = s.lower()
    res = ""
    for char in s:
        if ('0' <= char <= '9') or ('a' <= char <= 'z'):
            res += char
        else:
            res += "_"

    return res    



if __name__ == "__main__":
    ### Write 3 assert statements
    ### to test the function
    assert reverse_list([]) == -1
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    assert reverse_list(['ax', 'by', 'cz', 'df']) == ['df', 'cz', 'by', 'ax']

    assert username("9876ZyWx%$#@") == "9876zywx____"
    assert username("$#@") == "___"
    assert username('_AbD_') == "_abd_"
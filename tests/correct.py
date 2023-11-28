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

def calculate_power_sum(base, exp1=1, exp2=2, exp3=3, exp4=4):
    """
    Calculates the sum of the base number raised to four different exponents.

    Args:
        base (int): The base number for the power calculations.
        exp1, exp2, exp3, exp4 (int, optional): The exponents to which the base is raised. Defaults are 1, 2, 3, and 4, respectively.

    Returns:
        int: The sum of the base raised to each of the four exponents (base**exp1 + base**exp2 + base**exp3 + base**exp4).
             Returns -1 if any of the arguments are not integers.

    Note:
        This function verifies that all inputs are integers. If any input is not an integer, the function returns -1. 
        For more information, refer to Zybooks 8.2 Keyword arguments and default parameter values.
    """
    for num in (base, exp1, exp2, exp3, exp4):
        if not isinstance(num, int):
            return -1
    return base**exp1 + base**exp2 + base**exp3 + base**exp4

    
if __name__ == "__main__":
    ### Write 3 assert statements
    ### to test the function
    assert reverse_list([]) == -1
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    assert reverse_list(['ax', 'by', 'cz', 'df']) == ['df', 'cz', 'by', 'ax']

    assert calculate_power_sum(base=0.5) == -1
    assert calculate_power_sum(1, 2, 3, 4.5, 5) == -1
    assert calculate_power_sum(2) == 30
    assert calculate_power_sum(2, 1, 1, 1) == 22
    assert calculate_power_sum(2, 1, 1, 1, 1) == 8
    assert calculate_power_sum(base=2, exp1=2) == 32
    assert calculate_power_sum(base=2, exp1=1, exp2=1, exp3=1, exp4=1) == 8

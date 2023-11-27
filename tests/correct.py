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


def calculate_list_statistics(numbers):
    """
    Calculate and return various statistics for a list of numbers.

    Parameters:
    numbers (list): A list of numbers (int/float).

    Returns:
    dict: A dictionary containing the sum, product, average, min, and max of the numbers.
    """

    if not numbers:
        return {"sum": 0, "product": 0, "average": None, "min": None, "max": None}

    sum_result = sum(numbers)
    product_result = 1
    for num in numbers:
        product_result *= num

    average_result = sum_result / len(numbers)
    min_result = min(numbers)
    max_result = max(numbers)

    return {
        "sum": sum_result,
        "product": product_result,
        "average": average_result,
        "min": min_result,
        "max": max_result
    }


if __name__ == "__main__":
    ### Write 3 assert statements
    ### to test the function
    assert reverse_list([]) == -1
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    assert reverse_list(['ax', 'by', 'cz', 'df']) == ['df', 'cz', 'by', 'ax']

    assert calculate_list_statistics([]) == {"sum": 0, "product": 0, "average": None, "min": None, "max": None}
    assert calculate_list_statistics([5]) == {"sum": 5, "product": 5, "average": 5.0, "min": 5, "max": 5}
    assert calculate_list_statistics([-2, -1, 0, 1, 2]) == {"sum": 0, "product": 0, "average": 0.0, "min": -2, "max": 2}

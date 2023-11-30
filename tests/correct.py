## Given the stubs for the following function 
## and the main program, complete the implementation.
## Finish the assert statements to properly
## assert the result shown below (be careful 
## with the types of the variables).

## Make sure that your asserts test
## different branches/cases.


def reverse_list(data):
    """
    reverse_list() takes an list (data).
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
        for i in range(len(data) // 2):
            data[i], data[len(data) - i - 1] = data[len(data) - i - 1], data[i]
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


def format_table_row(data_row, column_formats):
    """
    format_table_row() takes data_row (dict) and column_formats (dict)
    to format a data row of a table using columns formats.
    data_row is a dictionary with keys as column names and values
    as the data for those columns. column_formats is a dictionary
    with keys as column names and values as another dictionary
    specifying 'width', 'alignment', and 'fill_char' for that column.
    If each 'fill_char' is not a single char, return (-1, "Invalid fill_char formatting value").
    If each 'alignment' is not one of ['left', 'center', 'right'],
    return (-1, "Invalid alignment formating value"). Otherwise,
    return a formatted string representing the data row in a table.

    Example Usage:
    inputs:
    data_row = {'Name': 'Alice', 'Age': '25', 'Country': 'USA'}
    column_formats = {'Name': {'width': 10, 'alignment': 'left', 'fill_char': '-'},
                          'Age': {'width': 4, 'alignment': 'center', 'fill_char': '*'},
                          'Country': {'width': 15, 'alignment': 'right', 'fill_char': '='}}
    output:
    Alice-----*25*============USA
    """
    formatted_row = []
    for column, format_spec in column_formats.items():
        fill_char = format_spec['fill_char']
        alignment = format_spec['alignment']
        width = format_spec['width']

        if len(fill_char) != 1:
            return -1, "Invalid fill_char formatting value"
        if alignment not in ['left', 'center', 'right']:
            return -1, "Invalid alignment formatting value"

        data = str(data_row.get(column, ''))

        if alignment == 'left':
            alignment_char = '<'
        elif alignment == 'center':
            alignment_char = '^'
        else:
            alignment_char = '>'

        formatted_row.append(f'{data:{fill_char}{alignment_char}{width}}')

    return ''.join(formatted_row)

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

def determine_class_status(grades):
    '''
    determine_class_status() takes a list (grades).
    The list contains four numeric that represent the quiz grades of a student.
    If any of the quiz grades is 0, the student fails the class and the function should return "Student failed the class"
    If there are no values in the grade list, the function should return "Student failed the class"
    If the average of all the quiz grades rounded to the nearest integer is <= 75, the student fails the class
    and the function should return "Student failed the class"
    If the average of all the quiz grades rounded to the second decimal place is greater than 75 and less than 90
    the function should return "Student passed the class"
    If the average of all the quiz grades rounded to the second decimal place is greater than or equal to 90,
    the function should return "Student passed the class with honors"
    You can assume all quiz grades will between 0 and 100 inclusive.
    :param grades: list of quiz grades
    :return: string of student's class status
    '''
    if len(grades) == 0:
        return "Student failed the class"

    total = 0
    for grade in grades:
        total += grade
        if grade == 0:
            return "Student failed the class"
    total = round(total / len(grades))

    if total <= 75:
        return "Student failed the class"

    if 75 < total < 90:
        return "Student passed the class"

    if total >= 90:
        return "Student passed the class with honors"


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
    assert calculate_list_statistics([]) == {"sum": 0, "product": 0, "average": None, "min": None, "max": None}
    assert calculate_list_statistics([5]) == {"sum": 5, "product": 5, "average": 5.0, "min": 5, "max": 5}
    assert calculate_list_statistics([-2, -1, 0, 1, 2]) == {"sum": 0, "product": 0, "average": 0.0, "min": -2, "max": 2}
    assert replace_string("I want to TTYL today.") == "I want to talk to you later today."
    assert replace_string("") == -1
    assert replace_string("Invalid string") == "Nothing to replace"


    data_row_invalid_fill = {'Name': 'Bob', 'Age': '40', 'Country': 'Mexico'}
    column_formats_valid = {
        'Name': {'width': 10, 'alignment': 'left', 'fill_char': '-'},
        'Age': {'width': 5, 'alignment': 'center', 'fill_char': '*'},
        'Country': {'width': 15, 'alignment': 'right', 'fill_char': '='}
    }
    result_valid = format_table_row(data_row_invalid_fill, column_formats_valid)
    assert result_valid == 'Bob-------*40**=========Mexico'

    column_formats_invalid_fill = {
        'Name': {'width': 10, 'alignment': 'left', 'fill_char': '!!'},  # Invalid fill character '!!'
        'Age': {'width': 5, 'alignment': 'center', 'fill_char': '*'},
        'Country': {'width': 15, 'alignment': 'right', 'fill_char': '='}
    }

    result_invalid_fill = format_table_row(data_row_invalid_fill, column_formats_invalid_fill)
    assert result_invalid_fill[0] == -1

    column_formats_invalid_alignment = {
        'Name': {'width': 10, 'alignment': 'invalid', 'fill_char': '-'},
        'Age': {'width': 5, 'alignment': 'center', 'fill_char': '*'},
        'Country': {'width': 15, 'alignment': 'right', 'fill_char': '='}
    }

    result_invalid_alignment = format_table_row(data_row_invalid_fill, column_formats_invalid_alignment)
    assert result_invalid_alignment[0] == -1

    data_row = {'Name': 'Alice', 'Age': '25', 'Country': 'USA'}
    column_formats = {
        'Name': {'width': 10, 'alignment': 'left', 'fill_char': '-'},
        'Age': {'width': 4, 'alignment': 'center', 'fill_char': '*'},
        'Country': {'width': 15, 'alignment': 'center', 'fill_char': '='}
    }
    expected_output = 'Alice-----*25*======USA======'
    assert format_table_row(data_row, column_formats) == expected_output, \
        "Assertion failed: The function should return the correctly formatted string."
    
    # Test slice_both_ends()
    assert slice_both_ends("") == -1
    assert slice_both_ends("Tortilla") == "rtil"
    assert slice_both_ends("Pomegranate") == "megran"
    assert slice_both_ends("cat") == "ca"
    assert determine_class_status([0, 90, 80, 70]) == "Student failed the class"
    assert determine_class_status([75, 75, 75, 75]) == "Student failed the class"
    assert determine_class_status([80, 80, 90, 70]) == "Student passed the class"
    assert determine_class_status([90, 90, 90, 90]) == "Student passed the class with honors"
    assert determine_class_status([0]) == "Student failed the class"
    assert determine_class_status([90]) == "Student passed the class with honors"
    assert determine_class_status([]) == "Student failed the class"

    print('all asserts passed!')


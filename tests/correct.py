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
        for i in range(len(data)//2):
            data[i], data[len(data)-i-1] = data[len(data)-i-1], data[i]
        return data

if __name__ == "__main__":
    ### Write 3 assert statements
    ### to test the function
    assert reverse_list([]) == -1
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    assert reverse_list(['ax', 'by', 'cz', 'df']) == ['df', 'cz', 'by', 'ax']

    assert username("9876ZyWx%$#@") == "9876zywx____"
    assert username("$#@") == "___"
    assert username('_AbD_') == "_abd_"
    assert family_relations("John") == "John's Family:\n"
    assert family_relations("Ted", brother="Tom", mother="Alice") == "Ted's Family:\nbrother: Tom\nmother: Alice\n"
    assert family_relations("Ted", brother="Tom", sister="Sarah", father="Adam", mother="Alice") == "Ted's Family:\nbrother: Tom\nsister: Sarah\nfather: Adam\nmother: Alice\n"

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


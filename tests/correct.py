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
        for i in range(len(data) // 2):
            data[i], data[len(data) - i - 1] = data[len(data) - i - 1], data[i]
        return data


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


if __name__ == "__main__":
    ### Write 3 assert statements
    ### to test the function
    assert reverse_list([]) == -1
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    assert reverse_list(['ax', 'by', 'cz', 'df']) == ['df', 'cz', 'by', 'ax']

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

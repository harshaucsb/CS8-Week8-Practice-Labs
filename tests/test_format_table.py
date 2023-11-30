import unittest
from gradescope_utils.autograder_utils.decorators import visibility, partial_credit
from BaseClass import BaseClass

# TODO: create test parameters
data_row = {'Name': 'Alice', 'Age': '25', 'Country': 'USA'}
test_params = [
    (data_row, {
    'Name': {'width': 10, 'alignment': 'left', 'fill_char': '-'},
    'Age': {'width': 4, 'alignment': 'center', 'fill_char': '*'},
    'Country': {'width': 15, 'alignment': 'center', 'fill_char': '='}
}),
    (data_row, {
    'Name': {'width': 10, 'alignment': 'left', 'fill_char': '=='},
    'Age': {'width': 5, 'alignment': 'center', 'fill_char': '*'},
    'Country': {'width': 15, 'alignment': 'right', 'fill_char': '='}
}),
    (data_row, {
    'Name': {'width': 10, 'alignment': 'leftwards', 'fill_char': '-'},
    'Age': {'width': 5, 'alignment': 'center', 'fill_char': '*'},
    'Country': {'width': 15, 'alignment': 'right', 'fill_char': '='}
})
]

max_score = len(test_params)

function_name = "format_table_row" # TODO

# TODO:  name the class according to the function name being tested
class FormatTableRow_Test(BaseClass):
    @partial_credit(max_score)
    @visibility('visible')
    def test1(self, set_score=None):
        """format_table_row(data_row, column_formats)""" # TODO

        student_module = self.student_functions
        total_score = max_score

        for param in test_params:
            if not self.handle_test_print_return_value(param, function_name, "", student_module):
                total_score -= 1
                print("Your function output does not match what's expected\nfor the following input:\n{}".format(param))

        set_score(total_score)
        if total_score == max_score:
            print("Congratulations! You passed this test.")

if __name__ == '__main__':
    unittest.main()

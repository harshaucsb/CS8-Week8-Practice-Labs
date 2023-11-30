import unittest
from gradescope_utils.autograder_utils.decorators import visibility, partial_credit
from BaseClass import BaseClass

# TODO: create test parameters
test_params = [
    ([0, 90, 80, 70]),
    ([75, 75, 75, 75]),
    ([80, 80, 90, 70]),
    ([90, 90, 90, 90]),
    ([0]),
    ([90]),
    ([]),
]

max_score = len(test_params)

function_name = "determine_class_status" # TODO

# TODO:  name the class according to the function name being tested
class DetermineClassStatus_Test(BaseClass):
    @partial_credit(max_score)
    @visibility('visible')
    def test1(self, set_score=None):
        """determine_class_status(grades)""" # TODO

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

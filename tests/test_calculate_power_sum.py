import unittest
from gradescope_utils.autograder_utils.decorators import visibility, partial_credit
from BaseClass import BaseClass

# TODO: create test parameters
test_params = [
    ({"base": 1, "exp1": 1, "exp2": 2, "exp3": 3.5, "exp4": 4}, -1),
    ({"base": 2, "exp1": 1, "exp2": 1, "exp3": 1}, 22),
    ({"base": 2, "exp1": 1, "exp2": 1, "exp3": 1, "exp4": 1}, 8),
    ({"base": 2}, 30),
]

max_score = len(test_params)

function_name = "calculate_power_sum" # TODO

# TODO:  name the class according to the function name being tested
class GetDictionaryValue_Test(BaseClass):
    @partial_credit(max_score)
    @visibility('visible')
    def test1(self, set_score=None):
        """calculate_power_sum(base, exp1, exp2, exp3, exp4)""" # TODO

        student_module = self.student_functions
        total_score = max_score

        for param in test_params:
            if not self.handle_test_print_return_value(**param, function_name, "", student_module):
                total_score -= 1
                print("Your function output does not match what's expected\nfor the following input:\n{}".format(param))

        set_score(total_score)
        if total_score == max_score:
            print("Congratulations! You passed this test.")

if __name__ == '__main__':
    unittest.main()

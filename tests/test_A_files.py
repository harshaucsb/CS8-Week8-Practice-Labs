"""
Tests that all files from config.versions submitted
"""
import unittest
from gradescope_utils.autograder_utils.decorators import weight, partial_credit, visibility

# https://github.com/gradescope/autograder_samples/blob/master/python/src/tests/test_files.py
from gradescope_utils.autograder_utils.files import check_submitted_files

import config


class A_TestQuiz(unittest.TestCase):
#@weight(0.5)
    @partial_credit(config.num_pts_file_name)
    def test_submitted_files(self, set_score=None):
        """Check submitted files"""
        # The above docstring will be shown on Gradescope
        # score = 1 # one point for each file they need to submit; should be the same as the value in @partial_credit()
        if config.version_num != 1000:
            versions = config.current_version_files  # All files that we have received from config
            missing_files = check_submitted_files(versions)
            #if missing_files:
            if missing_files:
                self.fail(f'Check the name of your .py file: it is incorrect.'
                          f'\nWhat we see is {config.original_student_filename},'
                          f'\nIt was supposed to be named: {config.current_version_files[0]}')
            # Below print will be shown when correct
            print('All required files submitted!')
        else:
            self.fail(f'Check the name of your .py file: it is incorrect.'
                      f'\nWhat we see is {config.original_student_filename},'
                      f'\n\nPlease refer to the quiz instructions on Gauchospace'
                      f'\nfor the correct file name for your version.')


    # TODO: use this test only for quizzes with versions. Else comment it out.
    @partial_credit(config.num_pts_version_check)
    @visibility(config.version_check_test_visibility)
    def test_version_check(self, set_score=None):
        """Check if gradescope version matches canvas"""
        if config.gradescope_version == 'unknown':
            self.fail('Could not infer version from file name.\nAll tests are likely to fail now.')

        if config.version_check_test_flag:
            if not config.correct_version_flag:
                # setting score to -100 so that we know if there is a version mismatch case involved.
                # we need to reset this to 0 after checking if it was a false positive or not.
                # we can remove this line if we want to get away with the manual check and rely only on autograder.
                set_score(-100)
                self.fail('The uploaded file does not match the version assigned via canvas.\n'
                          'All tests are likely to fail now.')

            else:
                print("Awesome! Gradescope version matches with that of canvas!")
        elif config.is_version_check_needed:
            print("Version check with canvas will be done later. \n"
                  "No marks will be awarded whatsoever if the versions don't match. \n"
                  "Make sure you select the right version on canvas and name the file accordingly."
                  )


if __name__ == '__main__':
    unittest.main()

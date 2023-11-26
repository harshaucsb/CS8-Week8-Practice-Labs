"""
This file can be used to define the "global" variables
that apply to the other separate test files.
Order of other files is defined by the name of the FILE alphabetically.
"""
import os
import sys

# TURN LOGGING ON OR OFF
# 0 - OFF
# 1 - ON
autograder_logging = 1

hidden_stdout = sys.stdout

# TODO 1. Create tests from asserts
# 2. Create file-stored check with many options
# 3. Check the output
# 4. Check the docstrings


# TODO: Adapt the scores as per needed
num_pts_file_name = 1
num_pts_fn_name = 1
num_pts_docstring = 1
num_pts_global_vars = 1
num_pts_simple_test = 2
num_pts_randomized_test = 2
num_pts_whole_program_run = 1
num_pts_version_check = 0

# TODO: create a mapping between the function name expected in the student's submission vs the function name present in our correct.py file.
# Usually they are gonna be the same, but there have been scenarios in quizzes where they could differ, hence the feature.
current_fun_names = []

fun_names_dict = {
    "reverse_list": "reverse_list",
    "slice_both_ends": "slice_both_ends",
}

required_files = ['main.py', 'functions.py', 'tests.py'] # TODO: add ALL required files
# File we will be running tests on
#main_functions_file = required_files[1] #

# List all the possible files that can be in the directory
# so that when we diff it with the contents of the submission
# the file that's left is the student's .py
# TODO : add filenames of all the test files to distinguish them from the student's submission
test_files = ['__init__.py', 'requirements.txt', 'run_autograder',
              'setup.sh', 'tests', 'run_tests.py', 'results.json', "__pycache__",
              '__MACOSX', 'metadata.yml',  
             ".pytest_cache",  # this is for the purpose of local testing (not on gradescope)
              ".DS_Store",
              "BaseClass.py",
              "config.py",
              "__init__.py",
              "correct.py",
              "constants.py",
              "submission examples",
              "test_A_files.py",
              "test_B_fun_names.py",
              "test_reverse_list.py",
              "test_slice_both_ends.py",
              ]
# TODO: update the above depending on the names of the test files.
################################
all_submitted_files = set(os.listdir('.'))

# # Will be available globally to see which files were submitted by students
student_submitted_files = all_submitted_files - set(test_files)


if autograder_logging:
    print('STUDENT\'S SUBMITTED FILES:', student_submitted_files)

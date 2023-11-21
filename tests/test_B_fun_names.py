"""
Creates N testing functions for all config.fun_names
"""
import os
import unittest
from gradescope_utils.autograder_utils.decorators import weight
import importlib
import config
from ddt import ddt, data
from Base_Class import Base_Class

class Mylist(int):
    pass


def annotated(num, name, docstring):
    r = Mylist(num)
    setattr(r, "__name__", name)
    setattr(r, "__doc__", docstring)
    return r


@ddt
class B_TestFunNames(Base_Class):

        # Here there will be created exactly as many tests as function names in config.fun_names
    # For 1pt weight for each existed function
    @weight(config.num_pts_fn_name)
    @data(*[annotated(i, f"test_{config.current_fun_names[i]}",
                      f"""B{i}. Is '{config.current_fun_names[i]}' defined?""")
            for i in range(len(config.current_fun_names))])
    def test(self, q_num):
        fun_name = config.current_fun_names[q_num]
        dir_list = set(dir(self.student))
        if fun_name not in dir_list:
            self.fail(f"Did you correctly define {fun_name}?")
        print(f"Function '{fun_name}' is defined")

    @weight(config.num_pts_docstring)
    def test_doc_strings_in_funs(self):
        """B2. Docstring presence"""
        fun_names = config.current_fun_names
        no_doc_string = []
        for name in fun_names:
            try:
                function = getattr(self.student, name)
            except:
                no_doc_string.append(name)
                continue
            if not function.__doc__:
                no_doc_string.append(name)
        if no_doc_string:
            s = "You do not have docstrings (or the whole function)\nfor the following functions:\n"
            for name in no_doc_string:
                s += "- " + name + "\n"
            s += "\nDid you create a proper doc string with \"\"\" or '''\n" \
                 "and place it directly underneath the function signature?\n" \
                 "Docstrings is nice code practice and will be required in \n" \
                 "your final project!"
            self.fail(s)
        else:
            print("You do have a docstrings for each function! Documentation is a great habit!")

    @weight(config.num_pts_global_vars)
    def test_e(self):
        """B3. Variables outside the if-name-main"""
        file = config.student_filename
        if file[-3:] != ".py":
            self.fail("Wrong file extension")
        file = file[:-3]

        try:
            student = importlib.import_module(file)
        except ModuleNotFoundError:
            student = "Cannot find your file. Is it named correctly?"
        except Exception as e:
            student = "Syntax error in the file"

        if type(student) == str:
            self.fail(student)

        vars = [i for i in dir(student) if "__" not in i and i != "math"]
        for fun in config.current_fun_names:
            if fun not in vars:
                self.fail(f"No {fun} functions")
            vars.pop(vars.index(fun))

        new_vars = []
        for var in vars:
            if not hasattr(getattr(student, var), "__call__"):
                new_vars.append(var)
        vars = new_vars
        if vars:
            s = "You have following "
            for var in vars:
                s += f"- {var}\n"
            s += "in global scope. It is a bad sign!"
            self.fail(s)

        print("No variables defined in global scope! Well done!")

if __name__ == '__main__':
    unittest.main()


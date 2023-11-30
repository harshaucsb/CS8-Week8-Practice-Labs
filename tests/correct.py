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
        
def family_relations(name, **relations):
    """
    family_relations takes a person's name as a string (name) and their family relations
    and a variable amount of keyword arguments as a dictionary (**relations)
    and returns a string containing all of the family relations of the person whose name and
    family relations are passed into the function, separated by a newline.  For example: If the function is called with just a name,
    family_relations("John") it returns the string "John's Family:\n".  If the function is called with more arguments for more family members
    like family_relations("Ted", brother="Tom", mother="Alice"), it returns the string "Ted's Family:\nbrother: Tom\nmother: Alice\n".
    Make sure to have different assert statements to test the function than the ones provided above and test it with variable amounts of arguments,
    including testing it with no extra arguments and just the name being passed in.  Note: Please refer to Zybooks section 8.3 for more information on lists
    with an arbitrary amount of arguments.
    """
    family_tree = name + "'s Family:\n"
    for relation, member in relations.items():
        family_tree += f"{relation}: {member}\n"
    return family_tree

if __name__ == "__main__":
    ### Write 3 assert statements
    ### to test the function
    assert reverse_list([]) == -1
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    assert reverse_list(['ax', 'by', 'cz', 'df']) == ['df', 'cz', 'by', 'ax']
    assert(family_relations("John")) == "John's Family:\n"
    assert(family_relations("Ted", brother="Tom", mother="Alice")) == "Ted's Family:\nbrother: Tom\nmother: Alice\n"
    assert(family_relations("Ted", brother="Tom", sister="Sarah", father="Adam", mother="Alice")) == "Ted's Family:\nbrother: Tom\nsister: Sarah\nfather: Adam\nmother: Alice\n"

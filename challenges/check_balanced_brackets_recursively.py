"""Problem statement:  the function "balanced_brackets" which takes a string as its argument. 
    It checks if the round brackets, or parentheses, within the string are balanced. 
    That is, for each opening bracket ( there should be a closing bracket ), 
    and all pairs of brackets should be matched in order, i.e. the bracket pairs must not be crossed.
    """


def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True

    # iterate until you reach an opening brace
    if my_string[0] in ['(', '[']:
        # if the last character is a closing brace - check for match
        if my_string[-1] in [')', ']']:
            if (my_string[0] == '(' and my_string[-1] == ')') or (my_string[0] == '[' and my_string[-1] == ']'):
                # strip off the matched brace and continue
                return balanced_brackets(my_string[1:-1])

            # if the last character is a closing brace but NOT a match - the braces are mismatched
            else:
                return False
        # iterate from the back until you reach a closing brace
        else:
            if len(my_string) == 1:
                return False
            else:
                return balanced_brackets(my_string[:-1])
    elif my_string[0] in [']', ')']:
        return False
    else:
        return balanced_brackets(my_string[1:])


if __name__ == "__main__":
    # should print True
    print(balanced_brackets("(((())))"))
    print(balanced_brackets("([([])])"))
    print(balanced_brackets(
        "this is just testing prefix stripping(python version [3.7]) please use this one!"))

    # should print False
    print(balanced_brackets("("))
    print(balanced_brackets("("))
    print(balanced_brackets("("))
    print(balanced_brackets("(python is the best programming language ever))"))
    print(balanced_brackets("(()"))

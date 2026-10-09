# I made a simple module!!!
# float(input('string ')) -> type_input('string ', float)
# I am confused about this!!!
#
# typeinput(string, type_val) > type_val(input(string))
# intinput(string) > int(input(string))
# floatinput(string) > float(input(string))
# boolinput(string) > bool_set(inp)

import typing

# define type_input, intinput, floatinput, boolinput
def type_input(
    prompt : str,
    type_val : type
) -> typing.Any:
    return type_val(input(prompt))

def intinput(prompt : str) -> int:
    return int(input(prompt))

def floatinput(prompt : str) -> float:
    return float(input(prompt))

def boolinput(prompt : str) -> bool | None:
    inp = input(prompt)
    bool_set = {
        'True' : True,
        'False' : False,
        'None' : None
    }
    if inp not in bool_set:
        raise ValueError(
            f'type name \'{inp}\' is not defined\nboolinput\'s input must be \'True\' or \'False\' or \'None\''
        )
    return bool_set[inp]
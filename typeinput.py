# I made a simple module!!!

# float(input('string ')) -> type_input('string ', float)
# I am confused about this!!!

# define type_input, intinput, floatinput, boolinput
def type_input(string, type_val):
    return type_val(input(string))

def intinput(string):
    return int(input(string))

def floatinput(string):
    return float(input(string))

def boolinput(string):
    inp = input(string)
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

# if it is runned without import
if __name__ == '__main__':
    import keyboard as kb, dynamicprint as dp
    dp.two_down('ok, I show this module\'s information.')
    print('type input(string, type_val)')
    print('intinput(string)')
    print('floatinput(string)')
    dp.two_down('boolinput(string)')
    print('press \'esc\', and it will close')
    kb.wait('esc')
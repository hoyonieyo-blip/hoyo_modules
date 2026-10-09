'''
scdecd
unnormal module!

import
    keyboard (only Windows)
    pygame (not in phone)
    sys
    types
    typing

class
    NoInputError(Exception)

function
    sinput
        prompt : str
        tp : type | None = str
        return -> (Any | str)

    pf
        inp : object
        return -> (None | object)
    
    printv
        vn : str
        por : int | None = 0
        return -> (None | typing.Any)

    ecd

    check_debug

variable
    debug
        bool
'''

import keyboard # only Windows
import pygame # not in phone
import sys
import types
import typing

pygame.init()

# make class
class NoInputError(Exception):
    pass

# define function
def sinput(
    prompt : str,
    tp : type = str
) -> typing.Any:
    '''
    showinput
    for Python CodePad in iOS

    prompt
        str
        input(str)
    
    tp
        type
        None = str
        tp(input)

    return
        tp(input(prompt))

    others
        print input
    '''

    try:
        v = input(prompt)
        if not v:
            raise NoInputError('No input value')
        # print(v) # only Python CodePad
        r = tp(v)

    except EOFError:
        # print() # only PythonvCodePad
        raise EOFError('No or weird input value')

    except ValueError:
        r = v

    return r

def pf(
    inp : typing.Any = None
) -> typing.Any:
    '''
    pass function
    do nothing

    inp
        return
    '''

    return inp

def printv(
    vn : str,
) -> None:
    '''
    print value
    print 'vn' value
    
    vn
        value name
        str
    
    print
        'vn' value
    '''

    rv = 0
    
    try:
        # set type
        iterators = (filter, map, range, zip)
        v = globals()[vn]
        t = type(v)

        if t in iterators:
            rv = 1

        if t in (type, types.FunctionType):
            x = v.__name__
        elif t in iterators:
            x = list(v)
        else:
            x = v

        r = f'{vn}: {x}'

    except KeyError:
        r = f'unknown {vn}'

    if rv:
        if t == range:
            globals()[vn] = range(x[0], x[-1] + 1)
        else:
            globals()[vn] = t(pf, x)

    print(r)

def ezf(
    num : int,
    zv : int = 0
) -> str:
    '''
    easy zfill
    str(num).zfill(zv) == ezf(num, zv)

    num
        int
        default number

    zv
        int
        zfill value
    '''

    return str(num).zfill(zv)

# ECD
def ecd():
    pygame.quit() # not in phone
    
    if debug:
        e = sinput('\nerror code\n> ', int)
        if type(e) == str: e = 1
    else: e = 0

    print('\npress \'esc\' to quit program...', end=''); keyboard.wait('esc') # only Windows
    sys.exit(e)

# debug mode
# if se.debug: printv(vn)
debug = False
def check_debug() -> None:
    global debug

    di = sinput('debug mode? y/n\n> ')

    debug = False
    if di not in ('y', 'n'): pass
    elif di == 'y':
        debug = True
    del di

    print()
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
    showinput\n
    for Python CodePad in iOS

    ---

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
    pass function\n
    do nothing

    ---

    inp
        return
    '''

    return inp

def printv(
    vn : str,
) -> None:
    '''
    print value\n
    print `vn` value
    
    ---

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
    easy zfill\n
    `str(num).zfill(zv) == ezf(num, zv)`

    ---
    
    num
        int
        default number

    zv
        int
        zfill value
    '''

    return str(num).zfill(zv)

def ete(
    exception : BaseException
) -> str:
    '''
    easy try-except

    ---

    exception
        BaseException

    return
        `f'{type(exception).__name__}: {exception}'`
    '''

    return f'{type(exception).__name__}: {exception}'

# ECD
def ecd(
    ec : int = 0
) -> None:
    '''
    end code data

    ---

    ec
        int
        error code

    raises
        SystemExit
            `sys.exit(e)`
    '''

    pygame.quit() # not in phone

    if debug and (not ec):
        e = sinput('\nerror code\n> ', int)
        if type(e) == str: e = 1
    else: e = ec

    print('\npress \'esc\' to quit program...', end='') # only Windows
    keyboard.wait('esc') # only Windows
    sys.exit(e)

# debug mode
# idpv(str)
debug = False

def check_debug() -> None:
    '''
    check debug

    ---

    debug
        return value
        if 'y' : debug = True
        if 'n' : debug = False
    '''

    global debug

    di = sinput('debug mode? y/n\n> ')

    debug = False
    if di not in ('y', 'n'): pass
    elif di == 'y':
        debug = True

    del di

def idpv(*values : str) -> None:
    '''
    if debug print value\n
    ...

    ---

    *values
        str
    '''

    if debug:
        for value in values:
            printv(value)
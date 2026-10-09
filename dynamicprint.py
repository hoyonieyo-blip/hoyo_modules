# dynamicprint.py
# made by hoyo
#
# no_end(*val, sep=' ', file=None, flush=None)
# space_end(*val, sep=' ', file=None, flush=None)
# two_down(*val, sep=' ', file=None, flush=None)
# vs_sep(*val, end='\n', file=None, flush=None)
# down_sep(*val, end='\n\n', file=None, flush=None)

import typing

# print with no end, space end, or something
def no_end(
    *val : object,
    sep : str = ' ',
    file : typing.TextIO = None,
    flush : bool = None
) -> None:
    '''
    no end

    end
        ''
    '''

    print(*val, sep=sep, end='', file=file, flush=flush)

def space_end(
    *val : object,
    sep : str = ' ',
    file : typing.TextIO = None,
    flush : bool = None
) -> None:
    '''
    space end
    
    end
        ' '
    '''

    print(*val, sep=sep, end=' ', file=file, flush=flush)

def two_down(
    *val : object,
    sep : str = ' ',
    file : typing.TextIO = None,
    flush : bool = None
) -> None:
    '''
    two down end

    end
        '\\n\\n'
    '''

    print(*val, sep=sep, end='\n\n', file=file, flush=flush)

def vs_sep(
    *val : object,
    end = '\n',
    file : typing.TextIO = None,
    flush : bool = None
) -> None:
    '''
    vs sep
    
    sep
        ' vs '
    '''

    print(*val, sep=' vs ', end=end, file=file, flush=flush)

def down_sep(
    *val : object,
    end = '\n\n', # sep : \n, so 'sep' and 'end' can be confused
    file : typing.TextIO = None,
    flush : bool = None
) -> None:
    '''
    down sep
    
    sep
        '\\n'
    
    end
        str
        '\\n\\n'
    '''

    print(*val, sep='\n', end=end, file=file, flush=flush)

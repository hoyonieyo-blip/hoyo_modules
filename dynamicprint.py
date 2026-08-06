# dynamicprint.py
# made by hoyo
#
# no_end(*val, sep=' ', file=None, flush=None)
# space_end(*val, sep=' ', file=None, flush=None)
# two_down(*val, sep=' ', file=None, flush=None)
# vs_sep(*val, end='\n', file=None, flush=None)
# down_sep(*val, end='\n\n', file=None, flush=None)

# print with no end, space end, or something
def no_end(
    *val : object,
    sep : str | None = ' ',
    file = None,
    flush = None
):
    print(*val, sep=sep, end='', file=file, flush=flush)

def space_end(
    *val : object,
    sep : str | None = ' ',
    file = None,
    flush = None
):
    print(*val, sep=sep, end=' ', file=file, flush=flush)

def two_down(
    *val : object,
    sep : str | None = ' ',
    file = None,
    flush = None
):
    print(*val, sep=sep, end='\n\n', file=file, flush=flush)

def vs_sep(
    *val : object,
    end = '\n',
    file = None,
    flush = None
):
    print(*val, sep=' vs ', end=end, file=file, flush=flush)

def down_sep(
    *val : object,
    end = '\n\n', # sep : \n, so 'sep' and 'end' can be confused
    file = None,
    flush = None
):
    print(*val, sep='\n', end=end, file=file, flush=flush)

# if it is runned without import
if __name__ == '__main__':
    import keyboard as kb
    two_down('ok, I show this module\'s information.')
    print('no_end() (end = \'\')')
    print('space_end() (end = \' \')')
    print('two_down() (end = \'\\n\\n\')')
    print('vs_sep() (sep = \' vs \')')
    two_down('down_sep() (sep = \'\\n\', end = \'\\n\\n\' or not)')
    print('press \'esc\', and it will close')
    kb.wait('esc')
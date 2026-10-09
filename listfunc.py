# listfunc.py
# 
# I made many thing with 2D list.
# I define them every times.
# 'Make a module! And you can make file more easy.'
# made by hoyo
#
# print_list(list_var)
# print_list_zfill(list_var, zfill_value)
# make_list_size(list_var, save_value, size)
# make_list_xy(list_var, save_value, x, y)
# wrap_list(index, size) > index % size
# block_index(index, size) > index(edited)

import typing

# print list
def print_list(
    list_var : list[list[typing.Any]]
) -> None:
    '''
    print list(2d)
    if you want to print 1d, use this: ' '.join(l)
    if you want to print 3d, use this: for l2 in l: print_list(l2); print()

    list_var
        list[list[typing.Any]]
        list to print

    return
        None
    '''

    for row in list_var:
        for value in row:
            print(value, end = ' ')
        print()

def print_list_zfill(
    list_var : list[list[typing.Any]],
    zfill_value : int
) -> None:
    '''
    print list(2d)
    if you want to print 1d, use this: ' '.join(l)
    if you want to print 3d, use this: for l2 in l: print_list_zfill(l2); print()

    list_var
        list[list[typing.Any]]
        list to print
    
    zfill_value
        int
        str.zfill(var)
        WHY DO WE'VE TO USE ZFILL AT ONLY STRING??...

    return
        None
    '''

    for row in list_var:
        for value in row:
            print(str(value).zfill(zfill_value), end = ' ')
        print()

# make list
def make_list_size(
    list_var : list,
    save_value : typing.Any,
    size : int
) -> None:
    '''
    make list (x == y)
    edit list_var

    list_var
        list

    save_value
        Any
        default value([[0,0,0],[0,0,0],[0,0,0]] like this)
    
    size
        int
        list size(example: 3)
    '''
    
    for r in range(size):
        row_list = []
        for v in range(size):
            row_list.append(save_value)
        list_var.append(row_list)

def make_list_xy(
    list_var : list,
    save_value : typing.Any,
    x : int,
    y : int
) -> None:
    '''
    make list (x != y)
        edit list_var
    
        list_var
            list
    
        save_value
            Any
            default value([[0,0,0],[0,0,0]] like this)
        
        x, y
            int
            list size(example: 2, 3)
    '''

    for r in range(y):
        row_list = []
        for v in range(x):
            row_list.append(save_value)
        list_var.append(row_list)

# fix out index(wrap)
def wrap_index(
    index : int,
    size : int
) -> int:
    '''
    wrap index

    index
        int
        input(now)
    
    size
        int
        list size
    
    return
        int
        wrap
    '''
    
    return index % size

# fix out index(block)
def block_index(
    index : int,
    size : int
) -> int:
    '''
    block index
    return to max value

    index
        int
        value's index
    
    size
        int
        max index value
    
    return
        int
        blocked
    '''

    if index >= size:
        index = size - 1
    elif index < 0:
        index = 0
    else: pass
    return index

# fix out index(none)
def none_index(
    index : int,
    size : int
) -> (None | int):
    '''
    none index

    index
        int
        value's index

    size
        int
        max index value
    
    return
        None | int
    '''
    
    if not 0 <= index < size:
        return None
    return index

# replace values
def convert(
    old : typing.Any,
    new : typing.Any,
    x : int,
    y : int,
    list_var : list[list[typing.Any]]
) -> None:
    '''
    convert
    or... paste?

    old
        typing.Any
        old value in list_var[y][x]
    
    new
        typing.Any
        new value in list_var[y][x]
    '''
    
    if list_var[y][x] == old:
        list_var[y][x] = new

# make neighbor list
def neighbors_size(
    x : int,
    y : int,
    list_var : list[list[typing.Any]],
    size : int = 0,
) -> list[list[typing.Any]]:
    '''
    neighbors list (size)
    for conway's game of life
    
    n = neighbors_size(x, y, board, len(board)).count(1)

    size
        int
        board size

    return
        list
        neighbor list
    '''

    if size <= 0: size = len(list_var)

    return [
        list_var[wrap_index(y + dy, size)][wrap_index(x + dx, size)]
        for dy in range(-1, 2)
        for dx in range(-1, 2)
        if dy or dx
    ]
    
def neighbors_xy(
    x : int,
    y : int,
    list_var : list[list[typing.Any]],
    size_x : int,
    size_y : int
) -> list:
    '''
    neighbors list (xy)
    for conway's game of life

    size_x, size_y
        int
        board size

    return
        list
        neighbor list
    '''
    
    return [
        list_var[wrap_index(y + dy, size_y)][wrap_index(x + dx, size_x)]
        for dy in range(-1, 2)
        for dx in range(-1, 2)
        if dy or dx
    ]
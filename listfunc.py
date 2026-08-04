# I made many thing with 2D list.
# I define them every times.
# 'Make a module! And you can make file more easy.'
import typing as ti

# print list
def print_list(list_var : list[list[ti.Any]]):
    for row in list_var:
        for value in row:
            print(value, end = ' ')
        print()
def print_list_zfill(list_var : list[list[ti.Any]], zfill_value : int):
    for row in list_var:
        for value in row:
            print(str(value).zfill(zfill_value), end = ' ')
        print()

# make list
def make_list_size(
    list_var : list,
    save_value : ti.Any,
    size : int
):
    for row in range(size):
        row_list = []
        for value in range(size):
            row_list.append(save_value)
        list_var.append(row_list)
def make_list_xy(
    list_var : list,
    save_value : ti.Any,
    x : int,
    y : int
):
    for row in range(y):
        row_list = []
        for value in range(x):
            row_list.append(save_value)
        list_var.append(row_list)

# fix out index(wrap)
def wrap_index(
    index : int,
    size : int
):
    return index % size

# fix out index(block)
def block_index(
    index : int,
    size : int
):
    while index >= size:
        index -= 1
    while index < 0:
        index = 0
    return index

# fix out index(none)
def none_index(
    index : int,
    size : int
):
    if not 0 <= index < size:
        return -1
    return index

# replace values
def convert(
    old : object,
    new : object,
    x : int,
    y : int,
    list_var : list[list[ti.Any]]
):
    if list_var[y][x] == old:
        list_var[y][x] = new

# make neighbor list
def neighbors_size(
    x : int,
    y : int,
    list_var : list[list[ti.Any]],
    size : int,
):
    return [
        list_var[wrap_index(y + dy, size)][wrap_index(x + dx, size)]
        for dy in range(-1, 2)
        for dx in range(-1, 2)
        if dy or dx
    ]
    
def neighbors_xy(
    x : int,
    y : int,
    list_var : list[list[ti.Any]],
    size_x : int,
    size_y : int
):
    return [
        list_var[wrap_index(y + dy, size_y)][wrap_index(x + dx, size_x)]
        for dy in range(-1, 2)
        for dx in range(-1, 2)
        if dy or dx
    ]
# writed in paper(note)
# from snake to swam...

# comments
# coding in Python
import typeinput as ti, keyboard as kb, listfunc as lf # add

# store various information
swam = []
size = ti.intinput('size : ') # edit
x, y = 0, 0 # edit
zfill_var = ti.intinput('zfill for : ') # add

# This part is emptied too
# Two spaces for a tab

# fill swam
lf.make_list_size(swam, 0, size)

# Now comes the real challenge
# First, define a function
# sav(start, end, mode)
def sav(
    orig : int,
    max : int,
    mode : str
):
    x = globals()['x']
    y = globals()['y']
    var = globals()['swam']

    # The downside of handwriting code:
    # sore hands, no interpreter (→ calculate * 100)
    # THINK, PLEASE

    if mode.lower() == 'plus':
        m = 1
    elif mode.lower() == 'minus':
        m = -1
    else:
        raise NameError(
            f'name \'{mode}\' is not defined'
        )

    # Ah, how do I make a for loop?
    for val in range(orig, max):
        var[lf.wrap_index(y, size)][lf.wrap_index(x, size)] = val
        x += m
    y += 1
    x -= m # add
    # Swap x and y for vertical

    # Apply the changes again
    globals()['x'] = x
    globals()['y'] = y
    globals()['swam'] = var

for orig in range(1, size**2+1, size):
# next page
    # y is even: plus
    # otherwise (= odd): minus
    if y % 2 == 0:
        sav(orig, orig+size, 'plus')
    else:
        sav(orig, orig+size, 'minus')

# I think we're done!!
# Nope, we still have to print it
lf.print_list_zfill(swam, zfill_var)

# For when running this in another terminal - add
print('\nPress esc to exit...')
kb.wait('esc')
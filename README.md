# hoyo_modules 

> **Note for English speakers**
>
> I'm Korean, and my English isn't very good.
> Some parts of this README were translated using Naver Papago or ChatGPT.
> So there may be awkward expressions.
> Sorry!

This repository contains Python modules created by Hoyo.

이 저장소에는 호요가 만든 파이썬 모듈들이 있습니다.

---

## colorformat.py

글자에 색상이나 스타일을 적용할 수 있습니다.
`colorama`는 자동으로 `ca`라는 이름으로 가져옵니다.

Add colors and text styles to terminal output.
`colorama` is automatically imported as `ca`.

```python
import colorformat as cf

print(cf.custom_style('1;31') + 'hello' + cf.RESET_STYLE)

# or

print(cf.RED + cf.BOLD + 'hello' + cf.RESET_STYLE)
```

---

## dynamicprint.py

`print()`를 다양한 방식으로 사용할 수 있습니다.

Provides several convenient versions of `print()`.

Examples:

* `end='\n\n'`
* `end=''`
* `sep=' vs '`

```python
import dynamicprint as dp

dp.space_end('hello')
dp.no_end('there!')
```

---

## listfunc.py

리스트(배열)를 생성하거나 출력하고, 특정 `(x, y)` 주변의 값을 가져올 수 있습니다.

Create and print lists (arrays), or get the neighboring values around a position `(x, y)`.

```python
import listfunc as lf
import random as rd

var = []
size = 10

lf.make_list_size(var, '00', size)

rr = lambda v: rd.randrange(0, v)

for i in range(50):
    x, y = rr(size), rr(size)
    var[y][x] = str(rr(100)).zfill(2)

lf.print_list(var)
for i in range(10):
    print(lf.neighbors_size(rr(10), rr(10), var, size))
```

---

## typeinput.py

자료형에 맞는 입력을 받을 수 있습니다.

Receive user input according to the specified type.

```python
import typeinput as ti
from colorformat import BOLD, RESET_STYLE

ti.type_input('input(int): ', int)
ti.intinput('intinput: ')
ti.boolinput(f'boolinput({BOLD}T{RESET_STYLE}rue, {BOLD}F{RESET_STYLE}alse): ')
```

---

## PyPI

아직 PyPI에 배포하는 방법을 배우지 못했습니다.

I don't know how to publish this project to PyPI yet.

For now, please place these modules directly into your Python `Lib` directory.

---

## How to use

This is a Minesweeper program that uses the modules I made.
I think you can use them like this.

제가 만든 저 모듈들을 쓴 지뢰찾기 코드입니다.
이런 식으로 쓰면 될 거 같아요.

```python
# 지뢰찾기 (Minesweeper)
# 불러오기 (Imports)
import colorformat as cf, keyboard as kb, listfunc as lf, random as rd, typeinput as ti, typing as ty

# 지뢰 찾았을 때 (When a mine is found)
class ThereIsMine(Exception):
    def __init__(self, message = 'There is mine!'):
        self.error = message

    def __str__(self):
        return self.error

# 지뢰, 깃발 등 스타일 지정 (Styles for mines, flags, etc.)
MINE = cf.custom_style('1;31') + 'M' + cf.RESET_STYLE
FLAG = cf.custom_style('1;93') + 'F' + cf.RESET_STYLE
NUMBER_CONVERT = {
    0 : f'{cf.GRAY}0{cf.RESET_STYLE}',
    1 : f'{cf.SKY_BLUE}1{cf.RESET_STYLE}',
    2 : f'{cf.LIME}2{cf.RESET_STYLE}',
    3 : f'{cf.RED}3{cf.RESET_STYLE}',
    4 : f'{cf.BLUE}4{cf.RESET_STYLE}',
    5 : f'{cf.MAGENTA}5{cf.RESET_STYLE}',
    6 : f'{cf.CYAN}6{cf.RESET_STYLE}',
    7 : f'{cf.GRAY}7{cf.RESET_STYLE}',
    8 : f'{cf.BRIGHT_WHITE}8{cf.RESET_STYLE}'
}

# 칸 열기 (Open a cell)
def show(
    x : int,
    y : int,
    list_seeing : list[list[ty.Any]],
    list_all : list[list[ty.Any]]
):
    list_seeing[lf.wrap_index(y, size_y)][lf.wrap_index(x, size_x)] = \
    list_all[lf.wrap_index(y, size_y)][lf.wrap_index(x, size_x)]
    if list_seeing[lf.wrap_index(y, size_y)][lf.wrap_index(x, size_x)] == MINE:
        raise ThereIsMine()

# 깃발 꽂기 (Place a flag)
def flag(
    x : int,
    y : int,
    list_seeing : list[list[ty.Any]]
):
    x = lf.wrap_index(x, size_x)
    y = lf.wrap_index(y, size_y)
    int_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    if list_seeing[y][x] == FLAG:
        list_seeing[y][x] = '-'
    elif list_seeing[y][x] in int_tuple:
        pass
    else:
        list_seeing[y][x] = FLAG

# 게임 끝내기 (End the game)
def end():
    print('finish!')
    lf.print_list(show_board)
    print('-' * size_x * 2)
    lf.print_list(show_minesweeper)
    print(
        'press '
        "'esc' "
        'to continue...'
    )
    kb.wait('esc')
    print()
    return True

# 0 나왔을 때 주변 열기 (Open surrounding cells when 0 appears)
def zero(
    x : int,
    y : int,
    list_seeing : list[list[ty.Any]],
    list_all : list[list[ty.Any]],
    not_zero : bool | None = False
):
    x, y = lf.wrap_index(x, size_x), lf.wrap_index(y, size_y)
    check = 0
    if list_seeing[y][x] == 0 or not_zero:
        for y_in_func in range(-1, 2):
            for x_in_func in range(-1, 2):
                value = list_seeing[lf.wrap_index(y+y_in_func, size_y)][lf.wrap_index(x+x_in_func, size_x)]
                if (
                    value == '-' and
                    (x_in_func or y_in_func)
                ):
                    show(lf.wrap_index(x+x_in_func, size_x), lf.wrap_index(y+y_in_func, size_y), list_seeing, list_all)
                    check += 1

    if check != 0:
        return True

# 보여주기용 리스트 만들기 (Create a list for display)
def make_showboard(
    list_var : list[list[ty.Any]],
    dict_var : dict
):
    ret = []
    for y in range(size_y):
        row_list = []
        for x in range(size_x):
            value = list_var[y][x]
            row_list.append(dict_var.get(value, value))
        ret.append(row_list)
    return ret

while True:
    try:
        # 온갖 변수 만들기 (Create various variables)
        minesweeper = []
        MODE = ti.intinput(
            'mode\n'
            '1 : easy - 9 * 9, 10 mines\n'
            '2 : medium - 16 * 16, 40 mines\n'
            '3 : hard - 30 * 16, 99 mines\n'
            '4 : custom - you can edit!\n'
            '5 : end this program\n'
            '> '
        )
        x, y = 0, 0

        # MODE 자세히 정하기 (Set the mode details)
        if MODE == 1:
            size_x = size_y = 9
            mines = 10
        elif MODE == 2:
            size_x = size_y = 16
            mines = 40
        elif MODE == 3:
            size_x, size_y = 30, 16
            mines = 99
        elif MODE == 4:
            size_x = ti.intinput('size x : ')
            size_y = ti.intinput('size y : ')
            mines = ti.intinput('mines : ')
            if mines >= size_x * size_y:
                raise ValueError(
                    'Too many mines!'
                )
        elif MODE == 5:
            break
        else:
            raise ValueError(
                'mode %s is not defined' % MODE
            )
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        continue
    
    lf.make_list_xy(minesweeper, 0, size_x, size_y)

    
    HARDCORE = input(
        f'{cf.RED}'
        'HARDCORE MODE? '
        'y/n : '
        f'{cf.RESET_STYLE}'
    ).lower() == 'y'
    
    # lf.print_list(minesweeper)
    
    # 랜덤한 곳에 지뢰 깔기 (Place mines randomly)
    count = 0
    while count < mines:
        rx = rd.randrange(0, size_x)
        ry = rd.randrange(0, size_y)
        orig = minesweeper[lf.wrap_index(ry, size_y)][lf.wrap_index(rx, size_x)]
        if orig == MINE:
            continue
        minesweeper[lf.wrap_index(ry, size_y)][lf.wrap_index(rx, size_x)] = MINE
        count += 1

    for y in range(size_y):
        for x in range(size_x):
            neighbor_mines_count = lf.neighbors_xy(x, y, minesweeper, size_x, size_y).count(MINE)
            if minesweeper[y][x] != MINE:
                minesweeper[y][x] = neighbor_mines_count
    # lf.print_list(minesweeper)

    # 시작 위치 지정 (Set the starting position)
    value = 1 # 처음에 반복문을 들어가기는 해야 되기 때문에 (The loop needs to run at least once initially)
    while value:
        rx = rd.randrange(0, size_x)
        ry = rd.randrange(0, size_y)
        value = minesweeper[ry][rx]

    # 새 리스트 (New list)
    board = []
    lf.make_list_xy(board, '-', size_x, size_y)
    board[ry][rx] = 0
    
    # 게임 시작 (Start the game)
    while True:
        try:
            # 0 체크 (Check for 0s)
            bool_var = True
            while bool_var:
                check = 0
                for y in range(size_y):
                    for x in range(size_x):
                        if board[y][x] == 0:
                            if zero(x, y, board, minesweeper):
                                check += 1
                if check == 0:
                    bool_var = False

            # 리스트 저장 (Store the lists)
            show_board = make_showboard(board, NUMBER_CONVERT)
            show_minesweeper = make_showboard(minesweeper, NUMBER_CONVERT)
            
            # 게임이 끝났는지 체크 (Check whether the game is over)
            board_value = [
                board[y_for][x_for]
                for y_for in range(size_y)
                for x_for in range(size_x)
            ]
            if (
                not '-' in board_value
            ) or (
                board_value.count('-') == mines - board_value.count(FLAG) - board_value.count(MINE)
            ):
                print('Looks end!')
                bk = end()
                if bk:
                    break

            lf.print_list(show_board) # 출력 (Display)

            # 명령어 입력받기 (Get a command)
            input_value = input(
                'show x y\n'
                'flag x y\n'
                'end\n'
                'quickshow\n'
                'help\n'
                '> '
            )
            cmd = input_value.strip().split()
            if not cmd:
                continue
            func = cmd[0]
            
            # 칸 열기 (Open a cell)
            if func == 'show':
                if len(cmd) != 3:
                    print(
                        'use by :\n'
                        'show x y\n'
                        'not index'
                    )
                    continue
                show(int(cmd[1]) - 1, int(cmd[2]) - 1, board, minesweeper)

            # 깃발 꽂기 (Place a flag)
            elif func == 'flag':
                if len(cmd) != 3:
                    print(
                        'use by :\n'
                        'flag x y\n'
                        'not index'
                    )
                    continue
                flag(int(cmd[1]) - 1, int(cmd[2]) - 1, board)

            # 끝내기 (End the game)
            elif func == 'end':
                bk = end()
                if bk:
                    break

            # 빠르게 열고 싶을 때 (When you want to open cells quickly)
            elif func == 'quickshow':
                if len(cmd) != 3:
                    print(
                        'use by :\n'
                        'quickshow x y\n'
                        'not index'
                    )
                    continue
                zero(int(cmd[1]) - 1, int(cmd[2]) - 1, board, minesweeper, True)

            # 규칙 설명 (Explain the rules)
            elif func == 'help':
                print(
                    '\nshow x y\n'
                    'open cell in x y\n\n'
                    'flag x y\n'
                    'put flag in x y\n\n'
                    'end\n'
                    'finish minesweeper\n\n'
                    'quickshow x y\n'
                    'shows like you opened zero cell\n\n'
                    'help\n'
                    'print this\n\n'
                    'press \'esc\' to continue...'
                )
                kb.wait('esc')
                print(
                    '\nall sides are wrapped\n'
                    'if you want to reload board, '
                    'write nothing\n\n'
                    'in easy mode,\n'
                    '1 1 : left side upside\n'
                    '1 9 : right side upside\n'
                    '9 1 : left low part\n'
                    '9 9 : right low part\n\n'
                    'first zero\'s position : '
                    f'{rx+1} {ry+1}\n\n'
                    'press \'esc\' to continue...'
                )
                kb.wait('esc')

            # 다른거라면 (If it is something else)
            else:
                raise ValueError(
                    'command \'%s\' is not defined' % func
                )

        # 지뢰일 때 (When a mine is hit)
        except ThereIsMine as error:
            print(f'{type(error).__name__}: {error}')
            if HARDCORE:
                end()
                break

        # 오류나 실패 잡기 (Catch errors or failures)
        except Exception as error:
            print(f'{type(error).__name__}: {error}')

print(
    'finish!\n'
    'press \'esc\' to continue...'
)
kb.wait('esc')
```
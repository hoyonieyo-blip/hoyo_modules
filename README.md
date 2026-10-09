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
Add colors and text styles to terminal output.

`colorama` 모듈이 필요하고, `ca`라는 이름으로 가져와집니다.
Requires `colorama` module, and it is imported as `ca`.

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

## scdecd.py

파일의 시작과 끝을 만들어뒀습니다.
모듈 이름의 유래가 **S**tart **C**ode **D**ata, **E**nd ... 이거예요.

It defines the start and end of a file.
The module name comes from **S**tart **C**ode **D**ata, **E**nd ...

`keyboard`, `pygame` 모듈이 필요합니다.
가능한 경우 직접 `pygame` 모듈을 사용하는 부분을 전부 주석 처리한 뒤 사용하셔도 됩니다.

Requires `keyboard`, `pygame` module.
If possible, you can use it after deleting or commenting `pygame` parts.

```python
# HowToUse/english_point.py
import scdecd as se

engchar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# encode
s = se.sinput('string to encode\n> ').upper()
l = map(engchar.find, list(s))
if se.debug: se.printv('s'); se.printv('l')

# print
p = ' '.join(map(str, l))
print(p)

se.ecd()
```

---

## PyPI

아직 PyPI에 배포하는 방법을 배우지 못했습니다.

I don't know how to publish this project to PyPI yet.

For now, please place these modules directly into your Python `Lib` directory.

---

## How to use

I put the `minesweeper.py`, `swam_array.py`, and `english_point.py` files in the `HowToUse` folder.
I think you can use them like this.

`minesweeper.py`와 `swam_array.py`, `english_point.py` 파일을 `HowToUse` 폴더에 저장해뒀습니다.
이런 식으로 쓰면 될 거 같아요.
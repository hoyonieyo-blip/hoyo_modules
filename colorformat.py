# colorformat.py
# use colorama, and '\033[31m'
# made by hoyo
#
# custom_style(v) > f'\033[{v}m'
#
# RESET_STYLE
# BOLD
# DIM
# ITALIC
# UNDERLINE
# BLINK
# REVERSE
# HIDDEN
# STRIKETHROUGH
# 
# BLACK
# RED
# GREEN
# YELLOW
# BLUE
# MAGENTA
# CYAN
# WHITE
# 
# BACK_BLACK
# BACK_RED
# BACK_GREEN
# BACK_YELLOW
# BACK_BLUE
# BACK_MAGENTA
# BACK_CYAN
# BACK_WHITE
# 
# GRAY
# SCARLET
# LIME
# LEMON_YELLOW
# SKY_BLUE
# FUCHSIA
# AQUA
# BRIGHT_WHITE
# 
# BACK_DARK_GRAY
# BACK_SCARLET
# BACK_LIME
# BACK_LEMON_YELLOW
# BACK_SKY_BLUE
# BACK_FUCHSIA
# BACK_AQUA
# BACK_BRIGHT_WHITE

import colorama as ca
ca.init()

# set custom style
# 사용자 지정 글꼴 스타일을 정합니다
def custom_style(v : str):
    return f'\033[{v}m'

cs = custom_style # used in only this module 이 모듈에서만 사용합니다

# font style
RESET_STYLE = cs(0) # 모든 스타일 초기화 (reset all style)
BOLD = cs(1) # 굵게 (Bold)
DIM = cs(2) # 흐리게 (Dim)
ITALIC = cs(3) # 기울임 (Italic)
UNDERLINE = cs(4) # 밑줄 (Underline)
BLINK = cs(5) # 깜빡임 (Blink)
REVERSE = cs(7) # 반전 (Reverse: 글자/배경 반전)
HIDDEN = cs(8) # 숨김 (Hidden)
STRIKETHROUGH = cs(9) # 취소선 (Strikethrough)

# color
BLACK = cs(30) # 검정 (black)
RED = cs(31) # 빨강 (red)
GREEN = cs(32) # 초록 (green)
YELLOW = cs(33) # 노랑 (yellow)
BLUE = cs(34) # 파랑 (blue)
MAGENTA = cs(35) # 자홍 (Magenta)
CYAN = cs(36) # 청록 (Cyan)
WHITE = cs(37) # 흰색 (White)

# background
BACK_BLACK = cs(40) # 검정 배경 (Black)
BACK_RED = cs(41) # 빨강 배경 (Red)
BACK_GREEN = cs(42) # 초록 배경 (Green)
BACK_YELLOW = cs(43) # 노랑 배경 (Yellow)
BACK_BLUE = cs(44) # 파랑 배경 (Blue)
BACK_MAGENTA = cs(45) # 자홍 배경 (Magenta)
BACK_CYAN = cs(46) # 청록 배경 (Cyan)
BACK_WHITE = cs(47) # 흰색 배경 (White)

# color 2
# look var's name
GRAY = cs(90) # 밝은 검정
SCARLET = cs(91) # 밝은 빨강
LIME = cs(92) # 밝은 초록
LEMON_YELLOW = cs(93) # 밝은 노랑
SKY_BLUE = cs(94) # 밝은 파랑
FUCHSIA = cs(95) # 밝은 자홍
AQUA = cs(96) # 밝은 청록
BRIGHT_WHITE = cs(97) # 밝은 흰색

# background 2
BACK_DARK_GRAY = cs(100) # 밝은 검정 배경
BACK_SCARLET = cs(101) # 밝은 빨강 배경
BACK_LIME = cs(102) # 밝은 초록 배경
BACK_LEMON_YELLOW = cs(103) # 밝은 노랑 배경
BACK_SKY_BLUE = cs(104) # 밝은 파랑 배경
BACK_FUCHSIA = cs(105) # 밝은 자홍 배경
BACK_AQUA = cs(106) # 밝은 청록 배경
BACK_BRIGHT_WHITE = cs(107) # 밝은 흰색 배경

del cs
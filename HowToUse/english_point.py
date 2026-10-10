from scdecd import *

def main():
    engchar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # encode
    s = sinput('string to encode\n> ').upper()
    l = map(engchar.find, list(s))
    idpv('s', 'l')

    # print
    p = ' '.join(map(str, l))
    print(p)

    ecd()

while True:
    try: main()
    except BaseException as e:
        print(ete(e))
        x = 1
    else: x = 0

    agn = sinput('again? y/n\n> ').lower() == 'y'
    if not agn: ecd(x)

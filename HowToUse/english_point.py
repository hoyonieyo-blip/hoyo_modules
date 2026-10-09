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
cunitl = []
templ = []

msg = input('Digite o texto: ')

print('''
Escolha a ordem de codificação:
(Ex.: 1324 ou 43)
[ 1 ] Ascii
[ 2 ] Hex
[ 3 ] Binary
[ 4 ] Reverser
[ 5 ] Unicode
[ 6 ] Caesar
[ 7 ] ROT-13
[ 8 ] Base 64
[ 9 ] Upper Case''')

while True:
    cunit = input('\nInsira a ordem de codificação: ')
    if cunit.isnumeric() is True:
        for c in cunit:
            cunitl.append(int(c))
        for c in cunit:
            if int(c) not in templ:
                templ.append(int(c))
            else:
                break
        if templ[:] == cunitl[:]:
            templ.clear()
            break
    print('\033[4;31mValor Inválido. Tente Novamente\033[m')
    templ.clear()
    cunitl.clear()

codec = msg

for p, c in enumerate(cunitl):
    if c == 1:
        ord(codec)
    elif c == 2:
        hex(codec)
    elif c == 3:
        bin(codec)
    elif c == 4:
        reversed(codec)
    '''elif c == 5:

    elif c == 6:

    elif c == 7:

    elif c == 8:
        
    elif c == 9:
        codec.upper()'''

print(codec)

cunit = ''
cunitl = []
templ = []

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
[ 9 ] Upper or Lower Case (9+: Upper | 9-: Lower)''')

while True:
    cunit = input('\nInsira a ordem: ')
    if cunit.isnumeric() is True:
        for c in cunit:
            cunitl.append(c)
        for c in cunit:
            if c not in templ:
                templ.append(c)
            else:
                break
        if templ == cunitl:
            break
    print('\033[4;31mValor Inválido. Tente Novamente\033[m')



print(cunitl)

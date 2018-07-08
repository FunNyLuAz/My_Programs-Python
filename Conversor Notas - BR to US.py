nb = []
nu = []
m = []
qm = me = ' '
ct = 0
ma = ['Arte', 'Ciências', 'Educação Física', 'Ensino Religioso', 'Geografia',
      'História', 'Língua Portuguesa', 'Matemática', 'Empreendedorismo e Educ.Financeira', 'Filosofia',
      'Lem - Espanhol', 'Lem - Inglês', 'Literatura e Redação']

while True:
    qm = input('Quantas matérias você quer? [All = Todas]: ').upper().strip()
    if qm == 'ALL':
        qm = 13
        m = ma[:]
        break
    if (qm.isnumeric() is True) and ((int(qm) in range(1, 14)) is True):
        for c in range(0, 13):
            print(f'''[ {c} ]: {ma[c]}''')
        while ct != qm:
            qm = int(qm)
            print('')
            m.append(ma[int(input('Digite quais matérias você quer [Número respectivo]: '))])
            ct += 1
        break
print('')
for c in range(0, qm):
    nb.append(float(input(f'Digite a nota de {m[c]}: ')))

print(f'''\n{" < Conversor Notas - BR to US > ":=^50}
> Notas - BR:
{"Matérias ":.<25}{" Nota":.>25}''')
for p, c in enumerate(m):
    print(f'-{c:.<40}{nb[p]:.>9.2f}')

for c in nb:
    nu.append((c/20)-1)

print(f'''\n> Notas - US:
{"Matérias ":.<25}{" Nota (0 - 4)":.>25}{" Nota (A - F)":.>16}''')
for p, c in enumerate(m):
    if 3.7 < nu[p] <= 4.0:
        na = "A"
    elif 3.3 < nu[p] <= 3.7:
        na = "A-"
    elif 3.0 < nu[p] <= 3.3:
        na = "B+"
    elif 2.7 < nu[p] <= 3.0:
        na = "B"
    elif 2.3 < nu[p] <= 2.7:
        na = "B-"
    elif 2.0 < nu[p] <= 2.3:
        na = "C+"
    elif 1.7 < nu[p] <= 2.0:
        na = "C"
    elif 1.3 < nu[p] <= 1.7:
        na = "C-"
    elif 1.0 < nu[p] <= 1.3:
        na = "D+"
    elif 0.7 < nu[p] <= 1.0:
        na = "D"
    elif 0.0 <= nu[p] <= 0.7:
        na = "D-"
    elif 0.0 <= nu[p] <= 0.7:
        na = "F"
    if len(na) == 2:
        print(f'-{c:.<38}{nu[p]:.>10.2f}{na:.>17}')
    else:
        print(f'-{c:.<38}{nu[p]:.>10.2f}{na:.>16}')

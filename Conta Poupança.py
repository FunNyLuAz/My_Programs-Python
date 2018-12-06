from time import sleep

msgerror = "\033[31;4mValor inválido. Digite novamente\033[m\n"
v_tax = q_mouth = count = 1
v_mouth = []

while True:
    try:
        value = float(input("> Digite o capital inicial: "))
        v_value = value
        break
    except ValueError:
        print(msgerror)

while True:
    try:
        tax = float((input("""> Digite a taxa para reajuste do valor
(Sem porcentagem, "%" | Ex.: 34% -> 34): """)))
        break
    except ValueError:
        print(msgerror)

while True:
    r_expo = input('> Digite se você gostaria de adicionar um valor mensal a quantia ["Sim"/"Não"]: ').upper().strip()
    if r_expo == 'SIM':
        expo = float(input("> Digite o valor a ser adicionado mensalmente: "))
        break
    elif r_expo == 'NÃO' or 'NAO':
        expo = 0
        break
    else:
        print(msgerror)

while True:
    try:
        mouth = int(input("> Digite o número de meses planejados: "))
        break
    except ValueError:
        print(msgerror)

while True:
    r_mouth = input('> Digite se você gostaria de ter um relatório a cada determinado período de meses '
                    '["Sim"/"Não"]: ').upper().strip()
    if r_mouth == "SIM":
        while True:
            try:
                q_mouth = int(input("> Digite a quantidade de meses entre os intervalos para o relatório: "))
                break
            except ValueError or q_mouth >= mouth:
                print(msgerror)
        break
    elif r_mouth == "NÃO" or "NAO":
        break
    else:
        print(msgerror)

for count in range(1, mouth):
    v_value = v_value*((tax/100)+1) + expo
    v_tax = tax - (count*value) - (count*expo)
    if count // q_mouth == 0:
        v_mouth.append(value)

v_expo = mouth*expo

print("\nAGUARDE...")
sleep(0.6)

print("""\nRESULTADO:

 -Acumulado pela taxa de reajuste do valor: R${0:<20}
 -Acumulado pelos acrescimos mensais: R${1}""".format(v_tax, v_expo))

if r_mouth == "SIM":
    print(" -Relatório:")
    for c in v_mouth:
            print("  {}º Mês: R${:.2f}".format((v_mouth.index(c)*q_mouth), c))

print("\n -O valor que você consiguirá retirar em {0} mês(eses) será de aproximadamente: R${1:.2f}".format(mouth, v_value))
print(v_mouth)

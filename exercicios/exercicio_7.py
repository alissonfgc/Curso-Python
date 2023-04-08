permanecer = 's'

while permanecer == 's':
    # n1 captura + validação
    print(20 * '-')
    n1 = input('Digite o pimeiro número: ')
    confere_n1 = not n1.isdigit()
    if confere_n1:
        print('O valor digitado é invalido, digite apenas números.')
        continue
    print(20 * '-')
    # n2 captura + validação
    n2 = input('Digite o segundo número: ')
    confere_n2 = not n2.isdigit()
    if confere_n2:
        print('O valor digitado é invalido, digite apenas números.')
        continue
    print(20 * '-')
    # operação captura + validação
    op = input('Qual operação deseja fazer? [*][/][+][-]: ')
    confere_op = False
    if (op == '*') or (op == '/') or (op == '+') or (op == '-'):
        confere_op = True
    
    if not confere_op:
        print('O valor digitado é invalido, digite apenas [*][/][+][-].')
        continue

    if op == '*':
        resultado = float(n1) * float(n2)
    elif op == '/':
        resultado = float(n1) / float(n2)
    elif op == '+':
        resultado = float(n1) + float(n2)
    elif op == '-':
        resultado = float(n1) - float(n2)
    else:
        print('Erro')
    print(20 * '-')
    print(f'O resultado da operação é: {resultado}')
    print(20 * '-')

    permanecer = input('Deseja permanecer? [S] ou [N] ')
    permanecer = permanecer.lower()
    
    ### Correção:

    """ Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

# Avalidação de numeros, e de operador é mais eficiente usando o "in",
#  e sempre usar uma nova variavel para converter os numeros.
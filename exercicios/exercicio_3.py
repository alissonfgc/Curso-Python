v1 = input('Digite o primeiro valor: ')
v2 = input('Digite o segundo valor: ')

if v1 > v2:
    print(f'O primeiro valor ({v1}) é maior que o segundo valor ({v2})')
elif v2 > v1:
    print(f'O segundo valor ({v2}) é maior que o primeiro valor ({v1})')
else:
    print(f'Os valores: ({v1}) e ({v2}) são iguais')
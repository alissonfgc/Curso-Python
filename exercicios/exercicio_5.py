"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
### ex 1

# n = input('Digite um número inteiro: ')

# try:
#     n = int(n)
#     resto = n % 2
#     if resto == 0:
#         print('O número digitado é: par')
#     else:
#         print('O número digitado é: ímpar')
# except:
#     print('Erro: O número digitado não é um número inteiro!')

### ex 2

# hora = input('Digite a hora (apenas números inteiros de 0 a 23) ')

# try:
#     hora = int(hora)
#     if hora >= 0 and hora <= 11:
#         print('Bom dia!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!')
#     else:
#         print('Erro: O valor digitado é invalido')
# except:
#     print('Erro: O valor digitado é invalido')

### ex 3

nome = input('Digite seu primeiro nome: ')
cont_nome = len(nome)

if cont_nome <= 4:
    print('Seu nome é curto')
elif cont_nome >= 5 and cont_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
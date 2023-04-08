# nome = 'Alisson Fernandes'
# i = 1

# while i <= len(nome):
#     cont_1 = i - 1
#     print(f'*{nome[cont_1:i]}*')
#     i += 1

# nome = 'Alisson Fernandes'
# novo_nome = ''
# i = 1

# while i <= len(nome):
#     cont_1 = i - 1
#     novo_nome = '*' + nome[cont_1:i] + '*' 
#     print(f'*{nome[cont_1:i]}*')
#     i += 1
# print(novo_nome)

# Forma correta: 

nome = 'Alisson Fernandes'
novo_nome = ''
i = 0

while i < len(nome):
    letra = nome[i]
    novo_nome += f'*{letra}'
    i += 1

novo_nome += '*'
print(novo_nome)
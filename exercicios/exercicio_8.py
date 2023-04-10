# código que conta e exibe qual letra aperece mais vezes
# frase = input('Digite a frase: ').lower().replace(' ', '')

# print(30 * '-')

# i = 0
# cont_letra = 0
# letra_mais = ''

# while i < len(frase):
#     letra_atual = frase[i]
#     cont_letra_atual = frase.count(letra_atual)

#     if cont_letra < cont_letra_atual:
#         letra_mais = letra_atual
#         cont_letra = cont_letra_atual

#     i += 1

# print(f'A letra mais repetida é: "{letra_mais}", que aparece {cont_letra}x vezes') #print alterado adicionando a quantidade de vezes em que a letra aparece
# print(30 * '-')

### Solução do professor

# frase = 'aaaooo'

# i = 0
# qtd_apareceu_mais_vezes = 0
# letra_apareceu_mais_vezes = ''

# while i < len(frase):
#     letra_atual = frase[i]

#     if letra_atual == ' ':
#         i += 1
#         continue

#     qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

#     if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
#         qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
#         letra_apareceu_mais_vezes = letra_atual

#     i += 1

# print(
#     'A letra que apareceu mais vezes foi '
#     f'"{letra_apareceu_mais_vezes}" que apareceu '
#     f'{qtd_apareceu_mais_vezes}x'
# )

### versão dp chat GPT

frase = input('Digite a frase: ').lower().replace(' ', '')
letra_mais = max(set(frase), key=frase.count)
print(f'A letra mais repetida é: "{letra_mais}", que aparece {frase.count(letra_mais)}x vezes')

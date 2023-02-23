'''Operador de atribuição
= atribuição
+= soma
-= subtração
*= multiplicação
/= divisão
//= divisão inteira
**= potenciação
%= resto da divisão
'''

nome = 'Vinicius Niceto'
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

tam_nome = 0
novo_nome = ''

while tam_nome < tamanho_nome :
    letra = nome[tam_nome]
    novo_nome += f'*{letra}'
    print(f'{letra}')

    tam_nome += 1

print(novo_nome)



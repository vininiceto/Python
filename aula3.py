#    Interpolação De Strings:
'''
%s - String
%d e %i - int
%f - float
%x e %X - hexadecimal 
'''
# nome = 'Vinicius'
# preco = 1000.95897643
# variavel = '%s, o preço é R$%.2f' % (nome, preco)
# print(variavel)
# print('O valor %d, possui o hexadecimal de: %04X' % (1500, 1500))

#     FORMATAÇÃO COM F-STRING

nome = input('Digite seu nome: ')
valor = input('Digite o valor para deposito: ')
value = float(valor)
# > (Esquerda) /// < (direita) ///// ^ (centro) /// tem como preencher com o que quiser na esquerda ou na direita colocando o nome:0>10 ou nome:0<10
#Exemplo print(f'{nome: >10}') ou print(f'{nome: <10}')
#Com números você pode colocar - e + na frente
print(f'{nome} o valor depositado foi: \n{value:+.2f}')
# def duplicar(x):
#     return x * 2

# def multiplicar(x):
#     return x * 3

# def quadriplicar(x):
#     return x * 4

# n1 = input('Digite um número: ')

# dup = duplicar(int(n1))
# trip = multiplicar(int(n1))
# quad = quadriplicar(int(n1))
# print(f'O número {n1} duplicado é: {dup}, o número {n1} triplicado é: {trip} e o número {n1} quadruplicado é: {quad}')
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

multiplicador = input('Você deseja duplicar, triplicar ou quadruplicar? ')

if multiplicador == 'duplicar':
    num = input('Digite um número para ser duplicado :')
    duplicar = criar_multiplicador(2)
    print(duplicar(int(num)))

if multiplicador == 'triplicar':
    num = input('Digite um número para ser duplicado :')
    triplicar = criar_multiplicador(3)
    print(triplicar(int(num)))
    
if multiplicador == 'quadruplicar':
    num = input('Digite um número para ser duplicado :')
    quadruplicar = criar_multiplicador(4)
    print(quadruplicar(int(num)))



#Para checar tamanho de uma string usar o len: Exemplo print(len(variavel)) ele ira retornar o tamanho da string variavel
#Para fatiar uma frase usar [i(inicio):f(fim):p (de quanto em quanto ele vai pulando)]: Exemplo print(variavel[4:8:2])

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços ')
    else: 
        print('Seu nome não contem espaços')
    print(f'Seu nome contem {len(nome)}')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios.')



# def multplicacao (x, y):
#     total = x * y
#     return total

# def number (numero):
#     if numero % 2 == 0:
#         print(f'{numero} é par.')
#     else:
#         print(f'{numero} é impar.')
    
# number(multplicacao(int(input('Digite um número: ')), int(input('Digite outro número: '))))

#simluador de dado
import random
import os

class SimuladorDeDado:
    def __init__(self):
        self.valor_Minimo = 1
        self.valor_Maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.gerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                os.system('cls')
                print('Agradecemos a sua participação!')
            else:
                os.system('cls')
                print('Favor digitar sim ou não')
        except:
            os.system('cls')
            print('Ocorreu um erro ao receber sua resposta')


    def gerarValorDoDado(self):
        print(random.randint(self.valor_Minimo, self.valor_Maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()


import os

lista = []

while True:
    opcao = input('Selecione uma opção: [i]nserir, [a]pagar, [l]istar, [s]air: ')

    if opcao == 'i':
        os.system('cls')
        inserir = input('Digite o produto que quer inserir na lista: \n')
        lista.append(inserir)
        os.system('cls')

    elif opcao == 'a':
        apagar = input('Digite o indice que deseja apagar: ')
        try:
            indice = int(apagar)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Nenhum item para listar.')

        for i, inserir in enumerate(lista):
            print(i, inserir)  

    elif opcao == 's' :
        print('Finalizando Sistema!!!')
        break  

    else:
        print('Por favor, escolha [i], [a] , [l], [s].')








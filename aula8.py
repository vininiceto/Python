while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um dos operadores (+-*/): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except Exception :
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos.')
        continue

    operadores_permitidos = '+-*/'
    soma = num_1_float + num_2_float
    subtracao = num_1_float - num_2_float
    divisao = num_1_float / num_2_float
    multiplicacao = num_1_float * num_2_float

    if operador not in operadores_permitidos or len(operador) > 1:
        print('O operador digitado não é permitido, digite apenas um operador válido.')
        continue

    print('Realizando o calculo desejado: ')
    if operador == '+' :
        print(f'{numero_1} + {numero_2} = {soma:.0f}')
    elif operador == '-':
        print(f'{numero_1} - {numero_2} = {subtracao:.0f}')
    elif operador == '*':
        print(f'{numero_1} * {numero_2} = {multiplicacao:.0f}')
    elif operador == '/':
        print(f'{numero_1} / {numero_2} = {divisao:.0f}')
        
    else:
        print('Nunca deveria chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
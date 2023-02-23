# num = float(input('Digite um número para verificar se é impar ou par: '))

# num_par = num / 2 == 1

# if num_par : 
#     print(f'O número {num} é par')

# else:
#     print(f'O número {num} é impar')
# try:
#     horario = float(input('Digite o horário atual: '))
#     bom_dia = horario >= 0 and horario <= 11
#     boa_tarde = horario >= 12 and horario <= 17
#     boa_noite = horario >= 18 and horario <= 23

#     if bom_dia:
#         print('Bom Dia')

#     elif boa_tarde:
#         print('Boa Tarde')

#     elif boa_noite:
#         print('Boa noite')
# except:
#         print('O horário digitado não está correto')

nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)
nome_curto = tamanho_nome >= 1 and tamanho_nome == 4
nome_normal = tamanho_nome > 4 and tamanho_nome <= 6
nome_grande = tamanho_nome > 7

if nome_curto :
    print('Seu nome é curto')

elif nome_normal :
    print('Seu nome é normal')

elif nome_grande :
    print('Seu nome é muito grande')

if tamanho_nome == 0:
    print('Por favor, digite um nome')

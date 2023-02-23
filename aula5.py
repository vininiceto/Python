

velocidade = 62
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro = velocidade > RADAR_1
passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
multa_radar_1 = velocidade_carro and passou_radar_1

if velocidade_carro:
    print('Você está acima da velocidade')

if passou_radar_1 :
    print('Um carro passou no radar 1')

if multa_radar_1 :
    print('Você levou uma multa')
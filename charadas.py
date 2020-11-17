import requests

print('#' * 40)
print('## PRONTO PARA UMA CHARADA? VAMOS LÁ!')
print('#' * 40)
headers = {'content-type': 'application/json; charset=utf-8','Accept': 'application/json'}

while 1==1:
    print()
    piada = requests.get('https://us-central1-kivson.cloudfunctions.net/charada-aleatoria',headers=headers)
    piada_dict = piada.json()
    print(piada_dict['pergunta'])
    print(' ')
    input('Aperte ENTER para ver a resposta... ')
    print('-' * 40)
    print(piada_dict['resposta'])
    print(' ')
    outraPiada = str(input('HA-HA... quer tentar outra? Sim (S) / Não (N) '))

    if outraPiada.upper() == 'N':
        exit()
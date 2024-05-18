import random
import time
from messages import display_messages

print('Iniciando o Projeto')
time.sleep(3)

while True:
    resposta = input('Deseja Receber um conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()

import random
#import sys
#import time

def mas_cartas():
    print("El jugador recibe: ",deck[0])
    mano_jugador

    return

deck = [1,2,3,4,5,6,7,8,9,10,11]    
pack = ["picas", "treboles", "diamantes", "corazones"]

random.shuffle(deck)
random.shuffle(pack)

mano_jugador = deck [0]    

print('El jugador recibe:',deck[0], 'de', pack[0])

random.shuffle(deck)
random.shuffle(pack)

mano_jugador += deck[2]

print('El jugador recibe:',deck[2], 'de', pack[2])
print("Total de la mano del jugador: ",mano_jugador)

print("¿El jugador quiere otra carta? Si/No", input())
if input() == "Si":
    random.shuffle(deck)
    mas_cartas() 


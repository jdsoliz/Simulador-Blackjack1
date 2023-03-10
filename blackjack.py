import random
#import sys
#import time

""" def mas_cartas():
    print("¿El jugador quiere otra carta? Si/No", input())
    if input() == "Si":
        random.shuffle(deck)
        print("El jugador recibe: ",deck[0])
        mano_jugador 

    return """

deck = [1,2,3,4,5,6,7,8,9,10,11]    

pack = ["picas", "treboles", "diamantes", "corazones"]
random.shuffle(deck)
random.shuffle(pack)
mano_jugador = deck [0]    
print("El jugador recibe: ",deck[0] + pack)

random.shuffle(deck)
random.shuffle(pack)
mano_jugador += deck[2]

print("El jugador recibe: ",deck[2] + pack)
print("Total de la mano del jugador: ",mano_jugador)

#mas_cartas()
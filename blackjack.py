import random
#import sys
import time
# <>
def mas_cartas():
    global mano_jugador
    random.shuffle(deck)
    random.shuffle(pack)
    mano_jugador += deck[0]
    print('El jugador recibe:',deck[0], 'de', pack[0])
    print("Total de la mano del jugador: ",mano_jugador)

    if mano_jugador > 21:
       random.shuffle(deck)
       random.shuffle(pack)
       print("El jugador ha sobrepasado 21")
       print("El jugador pierde")
    elif mano_jugador <= 21:
        pedir_carta = input("¿El jugador quiere otra carta? si/no: ")
        if pedir_carta == "si":
            mano_jugador += deck[1]
        print('El jugador recibe:',deck[1], 'de', pack[0])
        print("Total de la mano del jugador: ",mano_jugador)
    return

def mas_croupier():
    global mano_croupier
    random.shuffle(deck)
    random.shuffle(pack)

    time.sleep(1)
    mano_croupier += deck[0]
    print('El croupier recibe:',deck[0], 'de', pack[0])
    print("Total de la mano del crouìer: ",mano_croupier)

    while mano_croupier < 17:
        random.shuffle(deck)
        random.shuffle(pack)
        mano_croupier += deck[0]
        time.sleep(1)
        print('El croupier recibe:',deck[0], 'de', pack[0])
        print("Total de la mano del croupier: ",mano_croupier)
    if mano_croupier > 21:
        time.sleep(1)
        print("El croupier ha sobrepasado 21, el jugador gana")
        exit
    return

def comparar():
    global mano_jugador
    global mano_croupier

    if mano_jugador > mano_croupier:
        time.sleep(1)
        print("La mano del jugador es más alta, el jugador gana")
    elif mano_jugador == mano_croupier:
        time.sleep(1)
        print("La mano del jugador es igual a la del croupier, empate")
    else:
        time.sleep(1)
        print("La mano del croupier es más alta, el jugador pierde")
    return

deck = [1,2,3,4,5,6,7,8,9,10,11]    
pack = ["picas", "treboles", "diamantes", "corazones"]

random.shuffle(deck)
random.shuffle(pack)

mano_jugador = deck [0]    
print('El jugador recibe:',deck[0], 'de', pack[0])

mano_croupier = deck[1]
print('El croupier recibe:',deck[1], 'de', pack[1])

mano_jugador += deck[2]
print('El jugador recibe:',deck[2], 'de', pack[2])
print("Total de la mano del jugador: ", mano_jugador)

pedir_carta = input("¿El jugador quiere otra carta? si/no: ")
if pedir_carta == "si":
    mas_cartas() 

mas_croupier()

comparar()


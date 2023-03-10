import random
import sys
import time

#<>

def pedir_pj(a):

    a = pj
    
    if pedir_carta == "pedir":
    # random.shuffle(deck)
        while a < 21:
            random.shuffle(deck)

            print("El jugador pide otra carta")
            time.sleep(1)
            print("La carta nueva es: ", deck[0])
            a = a + deck[0]
            time.sleep(1)
            print("Total del jugador: ", a)
            #time.sleep(1)

            if a >21:
                print("El jugador ha superado 21")
                time.sleep(1)
                print("El jugador pierde")
                sys.exit()
            
            print("¿El jugador quiere otra carta?")
            time.sleep(1)

            mas_cartas = input("¿si o no?: ")
            #time.sleep(1)

            if mas_cartas == "no":
                break

            else:
                continue

    return a

def pedir_cr(b):
    b = cr
    while b < 17:
        random.shuffle(deck)
        print("El croupier pide otra carta")
        time.sleep(1)
        print("La carta nueva del croupier es: ", deck[0])
        b = b + deck[0]
        time.sleep(1)
        print("Total del croupier: ", b)

        if b >21:
                print("El croupier ha superado 21")
                time.sleep(1)
                print("El croupier pierde")
                sys.exit()

    return b

def comparar(c, d):

    c = pedir_pj(pj)
    d = pedir_cr(cr)
    
    print("Total del jugador: ", c)
    time.sleep(1)
    print("Total del croupier: ", d)

    if c <= 21 and c >= d:
        print("Total del jugador: ", c)
        time.sleep(1)
        print("El jugador gana")

    else:
        print("Total del jugador: ", c)
        time.sleep(1)
        print("El jugador pierde")

def dividir():
    mano1 = pj/2 
    mano2 = pj/2
    pedir_pj(mano1)
    pedir_pj(mano2)
    return 

As = 11
J = Q = K = 10

# J = 'J'
# Q = 'Q'
# K = 'K'

deck = [2, 3, 4, 5, 6, 7, 8, 9, J, Q, K, As]
random.shuffle(deck)

carta1 = deck[0]
random.shuffle(deck)
carta2 = deck[2]
pj = carta1 + carta2
random.shuffle(deck)
cr = (deck[1])

print("El jugador recibe las cartas" , carta1, "y", carta2)
print("El jugador recibe: ",pj)
time.sleep(1)
print("El croupier recibe: ",cr)
time.sleep(1)

if carta1 == carta2:
    dividir_mano = input("¿El jugador quiere dividir la mano?(si o no): ")
    if dividir_mano == "si":
        dividir()


print("El jugador decide: pedir o plantarse")
pedir_carta = input("¿Qué decide el jugador?: ")

comparar(pj, cr)
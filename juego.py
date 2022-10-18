print("Bienvenido a la isla. Tu misión será encontrar el tesoro")
a = input("¿Derecha o Izquierda?: ")
if a.upper() == "DERECHA":
    print("Caiste en un agujero- GAME OVER")
elif a.upper() == "IZQUIERDA":
    b = input("¿Nadar o esperar?: ")
    if b.upper() == "NADAR":
        print("Atacado por una tribu- GAME OVER")
    elif b.upper() == "ESPERAR":
        c = input("Elige una puerta Amarilla | Azul | Roja: ")
        if c.upper() == "AMARILLA": 
            print("¡HAZ GANADO!")
        elif c.upper() == "AZUL": 
            print("Devorado por bestias - GAME OVER")
        elif c.upper() == "ROJA":
            c = input("Consigues una persona, ¿Hablar o correr: ")
            if c.upper() == "HABLAR":
                print("Eres quemado- GAME OVER")
            elif c.upper() == "CORRER":
                c = input("Consigues una puerta amarilla, ¿Entrar o esperar?: ")
                if c.upper() == "ESPERAR":
                    print("Te alcanzan y eres quemado- GAME OVER") 
                elif c.upper() == "ENTRAR":
                    print("¡HAZ GANADO!")
        else: print("GAME OVER")
else: print("Escoge una de las dos opciones")


"""Start of the game"""
print("Bienvenido a la isla. Tu misión será encontrar el tesoro")
"""Conditional #1"""
a = input("¿Derecha o Izquierda?: ")
if a.upper() == "DERECHA":
    print("Caiste en un agujero- GAME OVER")
elif a.upper() == "IZQUIERDA":
    """Conditional #2"""
    a = input("¿Nadar o esperar?: ")
    if a.upper() == "NADAR":
        print("Atacado por una tribu- GAME OVER")
    elif a.upper() == "ESPERAR":
        """Conditional #3"""
        a = input("Elige una puerta Amarilla | Azul | Roja: ")
        if a.upper() == "AMARILLA": 
            print("¡HAZ GANADO!")
        elif a.upper() == "AZUL": 
            print("Devorado por bestias - GAME OVER")
        elif a.upper() == "ROJA":
            """Conditional #4"""
            a = input("Consigues una persona, ¿Hablar o correr: ")
            if a.upper() == "HABLAR":
                print("Eres quemado- GAME OVER")
            elif a.upper() == "CORRER":
                """Conditional #5"""
                a = input("Consigues una puerta amarilla, ¿Entrar o esperar?: ")
                if a.upper() == "ESPERAR":
                    print("Te alcanzan y eres quemado- GAME OVER") 
                elif a.upper() == "ENTRAR":
                    print("¡HAZ GANADO!")
            """User enters an invalid option"""
        else: print("GAME OVER")
    """User enters an invalid option"""        
else: print("Escoge una de las dos opciones")


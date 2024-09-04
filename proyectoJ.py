import random

def crearTablero(tamano):
    return [["~" for _ in range(tamano)] for _ in range(tamano)]

def mostrarTableros(tableroDisparosJugador, tableroDisparosOponente):
    print("Tu tablero de disparos:")
    for fila in tableroDisparosJugador:
        print(" ".join(fila))
        
    print("Tablero de disparos del oponente:")
    for fila in tableroDisparosOponente:
        print(" ".join(fila))
        
def colocarBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado = False
        while not colocado:
            if jugador == "jugador":
                print(f"Colocando un barco {barco['nombre']} de tamano {barco['tamano']}")
                fila= int(input("Ingrese la fila: ")) 
                columna= int(input("Ingrese la columna: ")) 
                orientacion= input("Ingresar la orientación (h para horizontal, v para vertical): ").lower()
            else:
                fila = random.randint(0, len(tablero)-1)
                columna = random.randint(0, len(tablero)-1)
                orientacion = random.choice(['h','v'])   
            if validarColocacion(tablero, fila, columna, barco['tamano'],orientacion):
                colocarBarco(tablero, fila, columna, barco['tamano'],orientacion)
                colocado = True
            elif jugador=="jugador":
                print("Colocación inválida. ¡Inténtelo de nuevo!")
            
def validarColocacion(tablero, fila, columna, tamano, orientacion):
    if orientacion == 'h':
        if columna+tamano > len(tablero):
            return False
        for i in range (tamano):
            if tablero[fila][columna+i]!= "~":
                return False
    else:
        if fila + tamano > len (tablero):
            return False
        for i in range (tamano):
            if tablero[fila+i][columna]!= "~":
               return False
            
    return True

def colocarBarco(tablero, fila, columna, tamano, orientacion):
    if orientacion == 'h':
        for i in range(tamano):
            tablero[fila][columna + i] = "B"
    else:
        for i in range(tamano):
            tablero[fila + i][columna] = "B"

def realizarDisparo(tableroOculto, tableroDisparos, fila, columna):
    if tableroOculto[fila][columna] == "B":
        tableroDisparos[fila][columna] = "X"
        tableroOculto[fila][columna] = "H"  # Marcar como hundido
        return "Impacto"
    elif tableroDisparos[fila][columna] == "~":
        tableroDisparos[fila][columna] = "O"
        return "Agua"
    return "Ya disparaste aquí"

def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:  # Si hay algún barco no hundido
            return False
    return True


def jugarContraComputador():
    tamano=5
    tableroJugador=crearTablero(tamano)
    tableroComputadora=crearTablero(tamano)
    tableroDisparosJugador=crearTablero(tamano)
    tableroDisparosComputadora=crearTablero(tamano)
    
    barcos = [
        {"nombre": "portaaviones", "tamano": 3},
        {"nombre": "submarino", "tamano": 2}
    ]
    
    print("Coloca tus barcos")
    colocarBarcos(tableroJugador,barcos,"jugador")
    colocarBarcos(tableroComputadora,barcos,"computadora")
    
    turnoJugador=True
    
    while True:
        if turnoJugador:
            print("Tu turno")
            mostrarTableros(tableroDisparosJugador,tableroDisparosComputadora)
            fila= int (input("Ingresa la fila de disparo: "))
            columna= int (input("Ingresa columna de disparo: "))
            resultado= realizarDisparo(tableroComputadora,tableroDisparosJugador,fila,columna)
            print(resultado)
            if verificarVictoria (tableroComputadora):
                print ("¡Ganaste!")
                return "jugador"
        
        else:
            print("Turno de la computadora")
            fila=random.randint(0,tamano-1)
            columna=random.randint(0,tamano-1)
            resultado=realizarDisparo(tableroJugador,tableroDisparosComputadora,fila,columna)
            print (f"la computadora disparó en ({fila},{columna}):{resultado}")
            if verificarVictoria(tableroJugador):
                print("la computadora Ganó")
                return "computadora"
         
        turnoJugador= not turnoJugador
        
def jugarDosJugadores():
    tamano = 5
    tableroJugador1=crearTablero(tamano)
    tableroJugador2=crearTablero(tamano)
    tableroDisparosJugador1=crearTablero(tamano)
    tableroDisparosJugador2=crearTablero(tamano)
    
    barcos=[
          {"nombre": "portaaviones", "tamano": 3},
          {"nombre": "submarino", "tamano": 2}
    ]     
    print ("Jugador 1 coloca sus barcos: ")
    colocarBarcos(tableroJugador1,barcos,"jugador")
    print ("Jugador 2 coloca sus barcos: ")
    colocarBarcos(tableroJugador2,barcos,"jugador") 
    
    turnoJugador1=True  
    
    while True:
            if turnoJugador1:
                print("Turno del jugador 1")
                mostrarTableros(tableroDisparosJugador1, tableroDisparosJugador2)
                fila=int(input("Ingresa la fila del disparo: "))
                columna=int(input("Ingresa la columna del disparo: "))
                resultado=realizarDisparo(tableroDisparosJugador2,tableroDisparosJugador1,fila,columna)
                print (resultado)
                if verificarVictoria(tableroJugador2):
                    print("!Jugador 1 Ganó!")
                    return "jugador1"
            else:
                print("Turno del jugador2")
                mostrarTableros(tableroDisparosJugador2,tableroDisparosJugador1)
                fila=int(input("Ingresa la fila del disparo"))
                columna=int(input("Ingresa la columna del disparo"))
                resultado=realizarDisparo(tableroJugador1,tableroJugador2,fila,columna)
                print (resultado)
                if verificarVictoria(tableroJugador1):
                    print("¡Jugador 2 Ganó")
                    return "jugador2"
            turnoJugador1=not turnoJugador1
            
def mostrarMenu():
    print("Bienvenido al juego Batalla Naval")
    print("1. Instrucciones")
    print("2. Juega contra la computadora")
    print("3. Dos jugadores")
    print("4. salir")
def iniciarJuego():
    while True:
        mostrarMenu()
        modo= input("Elige una opción: ")
        
        if  modo =="1":
            print("Objetivo del Juego: Hundir todos los barcos de tu oponente antes de que él hunda los tuyos.")
            print("Instrucciones:")
            print("Cada jugador tiene un tablero de 5x5.")
            print("1. Coloca tus barcos (portaaviones de tamaño 3 y submarino de tamaño 2) en el tablero")
            print("2. Asegúrate de que los barcos no se salgan del tablero ni se superpongan.")
            print("3. Gana el jugador que primero hunda todos los barcos del oponente")
            print() #para que deje un espacio y no se junte con el menú 
            continue
        elif modo =="2":
            ganador = jugarContraComputador()
        elif modo =="3":
            ganador = jugarDosJugadores()
        elif modo =="4":
            print("Gracias por jugar. ¡Hasta pronto!")
            break
        else:
            print("La opción seleccionada no es válida, elige una opción entre 1 y 3.")
            continue
        print(f"El ganador es {ganador}.")
        
        jugarDeNuevo = input("¿Quiere jugar de nuevo? (s/n): ").lower()
        if jugarDeNuevo!= "s":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break


iniciarJuego()

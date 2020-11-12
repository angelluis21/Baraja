import baraja

class Baraja():

    def __init__(self, palos, numeros):
        self.palos = palos
        self.numeros = numeros
        self.mazacote = baraja.crearBaraja(palos, numeros)


    def barajar(self):
        baraja.barajar(self.mazacote)
    

    def repartir(self, num_jugadores, num_cartas):
        jugadores = []
        for i in range(num_jugadores):
            jugadores.append([])
        

        for jugador in range(num_jugadores):
            for carta in range(num_cartas):
                jugadores[jugador].append(self.mazacote.pop(0)) # en esta línea dice: añademe en jugadores[jugador] lo que quites de self.mazacote 
        return jugadores



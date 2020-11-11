palos = ['o', 'c', 'e', 'b']
numeros = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']


def creaBaraja():
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo)
    return baraja     


def intercambio(primer_valor, segundo_valor):
    aux = primer_valor
    primer_valor = segundo_valor
    segundo_valor = aux
    return primer_valor, segundo_valor

def barajar(lista_de_naipes):
    for i in range(len(lista_de_naipes))
        nuevas_pos = random.randrange(len(lista_de_naipes))
        '''
        intercambio de cartas, (tecnica de vaso vacio)
        '''
        aux = lista_de_naipes[nuevas_pos]
        lista_de_naipes[nuevas_pos] = lista_de_naipes[i]
        lista_de_naipes[i] = aux



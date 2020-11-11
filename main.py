import barajaC

palos = ['corazones', 'picas', 'diamantes', 'treboles']
numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

miBaraja = barajaC.Baraja(palos, numeros)

print(miBaraja.mazacote)
miBaraja.barajar()
print(miBaraja.mazacote)
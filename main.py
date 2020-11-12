import barajaC

palos = ['o','c','e','b']
numeros = ['A','2','3','4','5','6','7','S','C','R']

miBaraja = barajaC.Baraja(palos, numeros)

print(miBaraja.mazacote)
miBaraja.barajar()
print(miBaraja.mazacote)

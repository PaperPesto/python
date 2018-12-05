import diceManager

print("Ho importato il modulo diceManager")
print("Utilizzo il modulo diceManager")
print("Lancio 10 dadi da 20 facce")

risultati = diceManager.roll(20, 10)
print(risultati)

print("Il terzo risultato è " + str(risultati[2]))
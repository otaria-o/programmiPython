
g = int(input("Inserisci il moltiplicando: "))
t = int(input("Inserisci il moltiplicatore: "))

cont  = 0
somma = g

oneToT = range(1,t)
for count in oneToT:
        somma = somma + g

print("Il risultato della moltiplicazione tra", g, "e", t, "fa", somma)




dividendo = int(input("Dammi un dividendo: "))
divisore = int(input("Dammi un divisore: "))

resto = dividendo
risultato = 0

if divisore != 0 :
    while resto >= divisore :
        resto = resto - divisore
        risultato = risultato + 1
else :
    risultato = "infinito"
    resto = 0

print(f"Il risultato della divisione è {risultato}, con il resto di {resto}")

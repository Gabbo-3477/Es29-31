reddito = float(input("Inserisci reddito:"))

limiti = [10000,30000,60000,80000,1000000000000]

quota = [23,27,38,41,43]

if reddito <= 1000000000000 and reddito > 80000:

    imposta = 10000*23/100 + 13000*27/100 + 27000*38/100 + 20000*41/100 + (reddito - 80000)*43/100
    reddito_tassato = reddito - imposta
    print("Il reddito tassato è di ",reddito_tassato," euro.")
elif reddito <= 80000 and reddito > 60000:
    imposta = 10000*23/100 + 13000*27/100 + 27000*38/100 + (reddito - 60000)*41/100
    reddito_tassato = reddito - imposta
    print("Il reddito tassato è di ",reddito_tassato," euro.")
elif reddito <= 60000 and reddito > 30000:
    imposta =  10000*23/100 + 13000*27/100 + (reddito - 30000)*38/100
    reddito_tassato = reddito - imposta
    print("Il reddito tassato è di ",reddito_tassato," euro.")    
elif reddito <= 30000 and reddito > 10000:
    imposta = 10000*23/100 + (reddito - 10000)*27/100
    reddito_tassato = reddito - imposta
    print("Il reddito tassato è di ",reddito_tassato," euro.")    
elif reddito <= 10000:
    imposta = reddito*23/100
    reddito_tassato = reddito - imposta
    print("Il reddito tassato è di ",reddito_tassato," euro.")
else:
    print("Il reddito inserito non è scritto correttamente.")
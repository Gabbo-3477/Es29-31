Nord = int(input("Inserire il fatturato del nord Italia (euro):"))
Centro = int(input("Inserire il fatturato del centro Italia (euro):"))
Sud = int(input("Inserire in euro il fatturato del sud Italia (euro):"))
Isole = int(input("Inserire il fatturato delle isole dell'Italia (euro):"))
fatt = {'Nord':Nord,
'Centro': Centro,
'Sud ': Sud,
'Isole':Isole}
totale = Nord + Centro + Sud + Isole 
perc_Nord = Nord/totale*100
perc_Centro = Centro/totale*100
perc_Sud = Sud/totale*100
perc_Isole = Isole/totale*100

perc_fatt = {'Nord':perc_Nord,
'Centro': perc_Centro,
'Sud ': perc_Sud,
'Isole':perc_Isole}
print("Il fatturato totale è di ",totale," euro")
print("Il fatturato inserito è questo:")
print(fatt)
print("Ed è diviso in percentuale in questo modo:")
print(perc_fatt)
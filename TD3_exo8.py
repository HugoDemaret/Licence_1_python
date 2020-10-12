#Demaret Hugo

rice_mass = float(758000000000) #masse de riz en gramme
n = float(2**63) #nombre total de grain de riz
i = 1 #initialisation à 1
while rice_mass < ((n)*0.0025): #tant que la production annuelle de grain de riz n'atteint pas la masse totale
    i +=1
    rice_mass += 758000000000 #on additionne l'équivalent de chaque année
print(i) #on affiche le nombre d'années nécéssaires


#Note importante: on peut résoudre ce problème à l'aide d'une simple division.

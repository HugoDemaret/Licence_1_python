#Exercice 2 question 8:
#DEMARET Hugo
#attention: on traite ici du type "float" (réel) et non "int" (entier relatif)
m = float(input("Entrez le n-ième terme que vous souhaitez calculer:"))
n = 1. #initialisation de n
un_minus = 4.
while n != m: #tant que n est inégal à m (dans ce cas inférieur car initialisé à 1
    sequence_u_n = float(un_minus - (un_minus / ((2*n+1) ** 2))) #Definition de la suite Un
    sequence_v_n = float(un_minus/(1+(1/(2*n+1))))  #Definition de la suite Vn
    n += 1 #Incrément n de 1
    un_minus = sequence_u_n #Reaffectation de la variable: permet d'établir la récurrence
print("La limite de U(n) à la borne plus l'infinie est environ égale à: "+ str(sequence_u_n)) #Affichage de Vn+1
print("La limite de V(n) à la borne plus l'infinie est environ égale à: "+ str(sequence_v_n)) #Affichage de Un+1

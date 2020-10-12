#Demaret Hugo
#Dans ce défi-exemple, vous devez coder un algorithme qui pour une "graine" donnée (nous l'appellerons pas la suite "seed", graine en anglais), calcule la suite de Collatz
# de cette seed (voir problème 3n+1), et s'arrête de calculer quand la boucle '4,2,1' arrive (donc s'arrête quand la valeur est 1). L'algorithme doit nous donnner la durée de vol
#de la suite pour une seed donnée.
#Définition:
#La suite de collatz est définie comme telle:
#Un+1= {Si Un est pair, Un+1= Un/ 2 | Si Un est impair, Un+1 = 3Un+1
#La conjecture de Collatz affirme que peut importe la seed entrée, la suite terminera toujours par la boucle "4,2,1".
#Cette conjecture n'a toujours pas démontrée
#On appel "vol" le nombre de terme de la suite pour une seed donnée, le nombre d'étape avant que la boucle soit atteinte.
#Je vous encourage à vous renseigner sur cette suite, sur les diverses méthodes que les mathématiciens ont développés pour tenter d'y répondre,
#ainsi que les diverses approches utilisées, toutes plus intéressantes et élégantes les unes que les autres!

#Voici le code de cet exemple:
#Algorithme de calcul de la suite de Collatz en fonction d'une seed rentrée par l'utilisateur:

integer_1 = int(input("Rentrez la valeur de la graine"))
i = 0
while integer_1 != 1:
    i += 1
    if integer_1 % 2 == 0:                                  #Test la parité de Un ( "a%b" nous donne le reste de la division euclidienne de a par b)
        integer_1 = integer_1 // 2                          #Un+1 = Un/2, attention ici à bien mettre un "//" afin d'avoir une division entière !
    else:                                                   #Si un nombre entier n'est pas pair, il est impair, donc on peut mettre une condition else
        integer_1 = (3 * integer_1) + 1                     #Un+1 = 3Un+1
    print("Le terme " + str(i) + " de la suite est égal à " + str(integer_1))
print("Votre graine a un temps de vol de " + str(i))

#Note: on pourrait optimiser cet algorithme pour qu'il élimine d'entrée de jeu les puissances de 2

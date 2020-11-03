#Félicitation à Max Maiche qui remporte ce premier défi! Voici la correction du défi, ainsi que la réponse de Max.
#La solution de Max est équivalente à la mienne, aussi je vous laisse ses explications! Certaines choses diffèrent dans le code, mais globalement celui-ci fait la même chose:

#####################################CORRECTION##################################################
from math import sqrt

PointNumber = int(input('Entrez le nombre de points:'))
InCircle = 0

for i in range(PointNumber):
	y = random()
	x = random()
	radius = sqrt(x**2+y**2)
	if radius <= 1:
		InCircle = InCircle + 1

Pi = 4 * InCircle / PointNumber

print("Pi est environ égal à: ", Pi)
#################################################################################################
##########################Sujet de Max Maiche:###################################################

# Je vais calculer la probabilité qu'un point random sur un carré de 1 de longueur, soit dans un quart de cercle de rayon 1 et de centre (0,0)
import random
from math import*


iteration= int(input("Combien d'itérations voulez vous ?\n"))


reussite=0 # Init compteur de réussite
for i in range(1,iteration+1):
    x,y= abs(random.uniform(-1,1)), abs(random.uniform(-1,1))
    if y <= sqrt(1-(x)**2): # Je regarde si l'image de y par rapport à x est bien dans le quart de cercle (Pythagore)
        reussite+=1           # Si c'est une réussite je rajoute un au compteur

    
print("La valeur de pi est environ",(reussite/iteration)*4) # Pour la formule je dois trouver l'air du quart de cercle.
                                                            # C'est la moyenne de réussite par rapport au nombre d'essais.
                                                            # Puis pour avoir celui d'un cercle entier je fais fois 4 car l'air d'un cerlce de rayon 1 est pi.

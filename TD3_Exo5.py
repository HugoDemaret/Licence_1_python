#Demaret Hugo

init_number = int(input("Entrez le premier nombre"))
card = 2
sum = 0
while init_number !=0: #tant que le nombre rentré n'est pas 0
    sum += init_number #fait la somme avec les nombres précédent
    init_number = int(input("Entrez le " +str(card) + "nombre")) #rentre le n-ième nombre
    card += 1
print("La somme des entiers saisis vaut:", sum) #affiche la somme totale

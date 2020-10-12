init_number = int(input("Entrez le premier nombre"))
card = 2
sum = 0
while init_number !=0:
    sum += init_number
    init_number = int(input("Entrez le " +str(card) + "nombre"))
    card += 1
print("La somme des entiers saisis vaut:", sum)

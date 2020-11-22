
def convert(liste):
    liste2 = []
    for i in liste:             #parcourt la liste afin de traiter chaque string qu'elle contient
        if i == '':
            print("Erreur: votre liste contient une chaine vide!\n")
            break
        else:
            sum = ''
            for j in i:
                number = str(ord(j)) #décompose la string en char, prend la valeur ASCII du char, et fait une concaténation avec les chars précédents
                sum += str(number)
            liste2.append(int(sum))
            print(liste2)
    return liste2

def quicksort(liste):
    if len(liste) < 1:
        return liste
    else:
        pivot = liste.pop() #selectionne le pivot, en l'occurence le dernier élément de la liste

    greater_than = []
    lower_than = []

    for item in liste:
        if item > pivot:
            greater_than.append(item)

        else:
            lower_than.append(item)

    return quicksort(lower_than) + [pivot] + quicksort(greater_than) #récursivité pour les sous-listes


def main():
    liste = ['1', 'a', 'chat', 'Chiens', 'arbre', '47884abed', 'fr-FR', '5.1', '7', '9', '-15', '157', '011001', '3', '3', 'b', 'a', 'EC2EAC']
    liste2 = convert(liste)
    print("QuickSort: ", quicksort(liste2))

main()

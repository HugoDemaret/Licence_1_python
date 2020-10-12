init_number = int(input("Entrez le premier nombre"))
win = 0
if init_number == 42:
    win = 1
card = 2
i = 0
while i<4:
    i += 1
    init_number = int(input("Entrez le " +str(card) + "nombre"))
    if init_number == 42:
        win = 1
    card += 1
if win == 1:
    print("Gagné")
else:
    print("Perdu")

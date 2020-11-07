#correction exercice 2 TD6

def fibonacci():
    fib_zero = 0
    fib_un = 1
    terme = int(input("Entrez le nombre de termes à calculer: "))
    if terme > 0:
        for i in range(1, terme):
            sum = fib_zero + fib_un
            fib_zero = fib_un
            fib_un = sum
        print(sum)
fibonacci()

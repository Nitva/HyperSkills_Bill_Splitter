# write your code here
nombres = []
aRepartir = 1
friends=int(input("Enter the number of friends joining (including you):\n"))

if friends > 0:
    print("Enter the name of every friend (including you), each on a new line:")

    for _ in range(friends):
        nombres.append(input())

    total_bill = float(input("Enter the total bill value:\n"))
    aRepartir = round(total_bill / friends, 2)

    people = {nombre: aRepartir for nombre in nombres}

    print(people)
else:
    print("No one is joining for the party")

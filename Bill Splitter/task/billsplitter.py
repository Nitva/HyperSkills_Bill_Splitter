# write your code here

nombres = []
friends=input("Enter the number of friends joining (including you):")
if friends > "0":
    for friends in range(int(friends)):
        nombres.append(input())

    people = {nombre: 0 for nombre in nombres}

    print(people)
else:
    print("No one is joining for the party")
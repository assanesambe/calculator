continuer = True

def calculator(num1, num2):
    z = input("Choisissez l'opération à effectuer :(+, -, *, /): ")
    if z == "+":
        print(num1 + num2)
    elif z == "-":
        print(num1 - num2)
    elif z == "*":
        print(num1 * num2)
    elif z == "/" and num2 != 0:
        print(num1 / num2)
    else:
        print("Entrer le bon opérateur")

while continuer:
    while True:
        try:
            x = int(input("Veuillez entrer le premier nombre: "))
            break
        except ValueError:
            print("Ce n'est pas un entier valide. Veuillez réessayer.")
    
    while True:
        try:
            y = int(input("Veuillez entrer le deuxième nombre: "))
            break
        except ValueError:
            print("Ce n'est pas un entier valide. Veuillez réessayer.")
    
    calculator(x, y)
    
    n = input("Tapez 'y' pour continuer ou 'q' pour quitter: ")
    if n == 'y':
        continuer = True
    else:
        continuer = False

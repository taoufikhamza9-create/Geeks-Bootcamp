                       
                       #Exercice 1



mois = int(input("Entrez un mois (1 à 12) : "))
if 3 <= mois <= 5:
    print("Printemps")
elif 6 <= mois <= 8:
    print("Été")
elif 9 <= mois <= 11:
    print("Automne")
else:
    print("Hiver")





                   #Exercice 2

#    Part 1

for number in range(1, 21):
    print(number)

#    Part 2

# La question m'a parru ambiguë, donc j'ai fait deux interprétations possibles :)

# Interpretation 1: print the even numbers (2, 4, 6,,.. 20)

for number in range(1, 21):
    if number % 2 == 0:
        print(number)


# Interpretation 2: print the elements at an even index (positions 0, 2, 4...)

# In range(1, 21), the number 1 is at index 0, 2 at index 1, etc.

numbers = range(1, 21)
for index in range(len(numbers)):
    if index % 2 == 0:
        print(numbers[index])





          #Exercice 3

Mon_nom = "TAOUFIK"
user_name = input("Entrez votre nom : ")
while user_name != Mon_nom:
    user_name = input("Entrez votre nom : ")    




        #Exercice 4


names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("Quelle est votre nom ? : ")

#J'utilise index() parce qu'il renvoie directement la position de la première fois  où le nom apparaît
if name in names:
    print(names.index(name))






        #Exercice 5

#On peut utiliser la fonction max() pour trouver le plus grand nombre parmi les trois entrés par l'utilisateur mais je ne pense pas que c'est le but de l'exercice

first_number = int(input("Entrez un premier nombre : "))
second_number = int(input("Entrez un deuxième nombre : "))      
tirth_number = int(input("Entrez un troisième nombre : "))      

if first_number >= second_number and first_number >= tirth_number:
    print(f"Le plus grand nombre est : {first_number}")
elif second_number >= first_number and second_number >= tirth_number:  
    print(f"Le plus grand nombre est : {second_number}")
else:
    print(f"Le plus grand nombre est : {tirth_number}") 




               #Exercice 6

import random     #module random qui contient des fonctions pour le hasard

# compteurs pour resultat final
wins = 0
losses = 0

# la boucle tourne tant que le joueur ne tape pas 'q'
while True:
    answer = input("Guess my number from 1 to 9 (or 'q' to quit): ")

    # on vérifie le q avant de convertir en int sinon erreur 
    if answer == "q":
        break

    guess = int(answer)
    secret = random.randint(1, 9)  # nouveau nombre aleatoire à chaque partie 

    if guess == secret:
        print("Winner")
        wins = wins + 1
    else:
        print("Better luck next time.")
        losses = losses + 1

# s'affiche une seule fois quand on quitte
print("Games won:", wins)
print("Games lost:", losses)



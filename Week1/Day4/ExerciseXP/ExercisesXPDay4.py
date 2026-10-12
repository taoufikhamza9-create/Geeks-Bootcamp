  #Exercice 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result= {a:b for a,b in zip(keys, values )} # j'ai utiliser le dict compreenssion pour créer le dictionnaire à partir de deux listes
print(result) #Sa nous sort l'expected out put 

#Exercice 2

# une fonction pour ne pas réécrire la boucle deux fois pour le bonus
def calcul_prix(family):
    tot_cost = 0   
    for name, age in family.items():   # items() donne le nom et l'âge en même temps
        if age < 3:
            prix = 0
        elif age <= 12:  
            prix = 10
        else:
            prix = 15
        tot_cost += prix
        print(f"{name} has to pay ${prix}")
    print(f"Total cost: ${tot_cost}")

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
calcul_prix(family)   # total attendu : 50

# l'utilisateur remplit lui-même la famille
new_family={}
while True:
    nom=input("Enter the family member (or 'q' to quit): ")
    if nom=="q":   # on vérifie le q avant de demander l'âge
        break
    age=int(input("Enter the age of the family member: "))   # int() sinon age < 3 plante
    new_family[nom]=age

print(new_family)
calcul_prix(new_family)


#Exercice 3


brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": ["blue"], "Spain": ["red"], "US": ["pink", "green"]}
}

brand["number_stores"] = 2
 
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}") #', '.join(...) colle les éléments de la liste avec une virgule et un espace
 
brand["country_creation"] = "Spain"
 
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
 
del brand["creation_date"]
 
print(brand["international_competitors"][-1])   # -1 l'indice pour  le dernier
 
print(brand["major_color"]["US"])
 
print(len(brand))
 
print(brand.keys()) # affiche les clés du dictionnaire
 
more_on_zara = {"creation_date": 1975, "number_stores": 10000}
 
brand.update(more_on_zara) #ajoute les clés et valeurs du dictionnaire more_on_zara au dictionnaire brand , si une clé existe déjà sa valeur est remplacée par la nouvelle valeur
 
print(brand["number_stores"])   # 10000 : update() a remplacé l'ancienne valeur 2



   #Exercice 4

def describe_city(city, country="Morocco"): # Morocco  si on donne pas de pays
    print(f"{city} is in {country}")
 
describe_city("Reykjavik", "Iceland")
describe_city("Casablanca") # pas de pays donc il prend Morocco


    #Exercice 5

import random
def guess_num(number):
    random_number = random.randint(1, 100)
    if number == random_number:
        print("Success!")
    else:
        print(f"Fail! your number: {number}, random number: {random_number}")
 
guess_num(int(input("Enter a number between 1 and 100: ")))
 


    #Exercice 6



def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")
 
make_shirt()
make_shirt("medium")
make_shirt("small", "Hello")
make_shirt(size="XL", text="Hamzaa")   # bonus


    #Exercice 7 

#J'ai deja importer random dans l'exercice 5 pas besoind e le refaire
#Fonction qui renvoie une température aléatoire selon la saison donnée

def random_temp(season):
    if season == "winter":
        return random.randint(-10, 16)
    elif season == "spring":
        return random.randint(0, 23)
    elif season == "summer":
        return random.randint(16, 40)
    else:
        return random.randint(0, 23)

#J'ai bien tester la fonction random_temp() elle donne l'output attendu


def main():
    season = input("Enter a season (summer, autumn, winter, spring): ")
    temp = random_temp(season) #J'appel ma fonction
    print(f"The temperature right now is {temp} degrees Celsius.")
 
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif temp < 16:
        print("Quite chilly! Don't forget your coat")
    elif temp < 24:
        print("Nice weather today")
    elif temp < 32:
        print("It's warm, wear a t-shirt")
    else:
        print("It's really hot! Drink some water")
 
main() #J'execute ma fonction main() 


     #Exercice 8

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def test():
    correct = 0
    incorrect = 0
    wrong_answers = []
    for q in data:    # pose chaque question une par une
      answer = input(q["question"] + " ")
      if answer.lower() == q["answer"].lower(): #Les deux côtés passent en minuscules avant d’être comparés donc nom Nom et NOM sont accepter
        correct += 1
      else:
        incorrect += 1
        wrong_answers.append([q["question"], answer, q["answer"]]) # question, sa réponse, la bonne réponse
    return correct, incorrect, wrong_answers
 
def resultas(correct, incorrect, wrong_answers):
    print(f"Correct: {correct}, Incorrect: {incorrect}")
    for w in wrong_answers:   # bonus on affiche les erreurs
        print(f"{w[0]} your answer: {w[1]}, correct answer: {w[2]}")
 
correct, incorrect, wrong_answers = test()
resultas(correct, incorrect, wrong_answers)
 
if incorrect > 3:   # bonus plus de 3 fautes donc on rejoue
    print("More than 3 wrong answers, play again!")
    correct, incorrect, wrong_answers = test()
    resultas(correct, incorrect, wrong_answers)
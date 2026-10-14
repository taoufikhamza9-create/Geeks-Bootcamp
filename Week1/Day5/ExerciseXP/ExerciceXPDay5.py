#Exercice 1


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# on crée 3 chats
cat1 = Cat("MIMI", 3)
cat2 = Cat("MINOU", 5)
cat3 = Cat("MOUSTACHE", 2)

# renvoie le chat le plus vieux (l'objet entier)
# l'énoncé dit rien sur les égalités, donc on part du principe que les chats ont des âges différents

def old_cat(cat1, cat2, cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        return cat2
    else:
        return cat3


oldest_cat_age = old_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat_age.name}, and is {oldest_cat_age.age} years old.")

                 #Exercicre 2

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):          
        print(f"{self.name} goes woof!")
    
    def jump(self):
        x=self.height * 2
        print(f"{self.name} jumps {x} cm high!")



davids_dog = Dog("Rex", 50)
print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()       

saras_dog = Dog("Teacup", 20)
print(f"{saras_dog.name} is {saras_dog.height} cm tall.")
saras_dog.bark()
saras_dog.jump()    

# on compare la taille des deux chiens
# pareil, l'énoncé précise pas le cas où ils font la même taille, on suppose qu'elles sont différente

if davids_dog.height > saras_dog.height:
    print(f"{davids_dog.name} is bigger than {saras_dog.name}.")
else:
    print(f"{saras_dog.name} is bigger than {davids_dog.name}.")


                    #Exercice 3

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # affiche chaque ligne de la chanson, une par ligne  
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()   

#output:
#There’s a lady who's sure  
#all that glitters is gold
#and she’s buying a stairway to heaven
                    


                    #Exercice 4

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    # on ajoute que si l'animal est pas déjà là
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    # on vérifie qu'il existe avant de le retirer, sinon remove plante
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    # trie puis range les animaux par première lettre
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)
        return grouped_animals

    def get_groups(self):
        # on passe par sort_animals pour avoir les groupes dans l'ordre
        grouped_animals = self.sort_animals()
        for letter, animals in grouped_animals.items():
            print(f"{letter}: {', '.join(animals)}")


# le gardien du zoo utilise la classe
new_york_zoo = Zoo("New York Zoo")

# on ajoute des animaux jusqu'à ce qu'il tape rien
new_animal = input("Which animal should we add to the zoo : ")
while new_animal != "":
    new_york_zoo.add_animal(new_animal)
    new_animal = input("Which animal should we add to the zoo (Entrée pour arrêter) : ")

print("Animals in the zoo:")
new_york_zoo.get_animals()

animal_sold = input("Which animal should we sell : ")
new_york_zoo.sell_animal(animal_sold)

print("Animals in the zoo after the sale: ")
new_york_zoo.get_animals()

print(new_york_zoo.sort_animals())
new_york_zoo.get_groups()
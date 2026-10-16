                                   #Exercice 4

from ExerciceXPWeek2Day1 import Dog   # on importe Dog depuis le fichier de l'exercice Dogs d'hier
import random


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)   # le parent s'occupe de name, age et weight
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):   # args = tous les noms qu'on donne rangés dans un tupe
        names = self.name
        for dog_name in args:
            names += ", " + dog_name
        print(f"{names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))   # choice() prend un élément au hasard dans la liste
        else:
            print(f"{self.name} is not trained yet")


my_dog = PetDog("Rex", 5, 30)

my_dog.do_a_trick()
my_dog.train()
my_dog.do_a_trick()
my_dog.play("Max", "Rocky")

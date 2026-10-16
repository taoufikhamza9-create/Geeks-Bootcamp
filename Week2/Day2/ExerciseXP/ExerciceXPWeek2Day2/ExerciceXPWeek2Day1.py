                         #Exercice 1
 
class Pets:
    def __init__(self, animals):
        self.animals = animals
 
    def walk(self):
        for animal in self.animals:   # polymorphisme : chaque chat a une méthode walk(), peu importe sa race
            print(animal.walk())
 
 
class Cat:
    is_lazy = True   # attribut de classe, partagé par tous les chats
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def walk(self):
        return f"{self.name} is just walking around"
 
 
class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"
 
 
class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"
 
 
class Siamese(Cat):   # hérite de Cat donc il a déjà name age et walk()
    def sing(self, sounds):
        return f"{sounds}"
 
 
all_cats = [Bengal("Tigrou", 3), Chartreux("Minou", 5), Siamese("Luna", 2)]
 
sara_pets = Pets(all_cats)
sara_pets.walk()
 
 
                           #Exercice 2
 
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
 
    def bark(self):
        return f"{self.name} is barking"
 
    def run_speed(self):
        return self.weight / self.age * 10
 
    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} won the fight"
        else:
            return f"{other_dog.name} won the fight"
 
 
dog1 = Dog("Rex", 5, 30)
dog2 = Dog("Max", 3, 20)
dog3 = Dog("Rocky", 8, 40)
 
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
print(dog3.fight(dog1))
 
 
                       #Exercice 3
 
class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members
 
    def born(self, **kwargs):   # kwargs = un dico avec toutes les infos du bébé
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family for the birth of {kwargs['name']}!")
 
    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
        return False   # si on trouve pas le nom
 
    def family_presentation(self):
        print(f"Family: {self.last_name}")
        for member in self.members:
            print(member)
 
 
members = [
    {"name": "Michael", "age": 35, "gender": "Male", "is_child": False},
    {"name": "Sarah", "age": 32, "gender": "Female", "is_child": False}
]
 
my_family = Family("Hamza", members)
my_family.born(name="Adam", age=0, gender="Male", is_child=True)
print(my_family.is_18("Michael"))
print(my_family.is_18("Adam"))
my_family.family_presentation()
 
 
                              #Exercice 4
 
class TheIncredibles(Family):   # hérite de Family donc born, is_18 et family_presentation sont déjà là
    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if self.is_18(name):   # on réutilise la méthode héritée du parent
                    print(f"{name} uses his power: {member['power']}")
                else:
                    print(f"{name} is not old enough to use his power")
 
    def incredible_presentation(self):
        print("Here is our powerful family")
        super().family_presentation()   # super() appelle la méthode de la classe parent
 
 
incredible_members = [
    {"name": "Michael", "age": 35, "gender": "Male", "is_child": False, "power": "fly", "incredible_name": "MikeFly"},
    {"name": "Sarah", "age": 32, "gender": "Female", "is_child": False, "power": "read minds", "incredible_name": "SuperWoman"}
]
 
incredibles = TheIncredibles("Incredibles", incredible_members)
incredibles.incredible_presentation()
 
incredibles.born(name="Jack", age=0, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")
 
incredibles.use_power("Michael")
incredibles.use_power("Jack")
 
incredibles.incredible_presentation()
 
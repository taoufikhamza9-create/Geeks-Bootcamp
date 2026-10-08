                  #EXERCICE 1


print("Hello world\n"*4) 




                  #EXERCICE 2

print((99**3)*8)

                  
                  
                  #EXERCICE 3


name = "TAOUFIK"    
username = input("Enter your name: ")
if username == name:
    print("Oh we have the same !")
else:
    print("Glad to meet you " + username + " !")


                  #EXERCICE 4


hight=int(input("Enter your hight: "))
if hight > 145:
    print("Allow to ride ")
else:
    print("need to grow some more to ride.")    


                  #EXERCICE 5

my_fav_numbers=[7, 11, 13, 17, 19]
my_fav_numbers.append(23)
my_fav_numbers.append(29)
my_fav_numbers.remove(29)
friend_fav_numbers=[2, 3, 5, 7, 11]
our_fav_numbers=my_fav_numbers + friend_fav_numbers
print(our_fav_numbers)

                  #EXERCICE 6


#Non un tuple est n'est pas modifiable simplement  : on ne peut pas lui ajouter d'éléments (pas comme une liste avec append) ni lui retirer d'éléments (pas comme une liste avec remove).
#On peut seulement créer un nouveau tuple en lui ajoutant un autre tuple au premier avec la concatenation
 



                  #EXERCICE 7


basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
n = 0
for fruit in basket :
    
    if fruit == "Apples":
        n+=1
print(n)    
#Apres recherche dans la documentation je peu aussi utiliser simplement count() : print(basket.count("Apples"))   
basket.clear()
print(basket)



                   #EXERCICE 8


sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches = []
while sandwich_orders: 
    sandwich= sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
for sandwich in finished_sandwiches:
    print("I made your " + sandwich)

    




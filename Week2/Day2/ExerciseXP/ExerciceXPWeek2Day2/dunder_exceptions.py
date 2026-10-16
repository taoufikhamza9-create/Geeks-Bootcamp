                               #Exercice 1

class PrintList():

    def __init__(self, my_list):
        self.my_list = my_list

    def __repr__(self):
        return str(self.my_list)


print_list_instance = PrintList(["a", "b", "c"])
print(print_list_instance.__repr__())

# Output : ['a', 'b', 'c']
# __repr__ renvoie str(self.my_list)la liste transformée en texte


                                       #Exercice 2

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        try:
            total += number
        except TypeError:   # si c'est un str on peut pas l'additionner donc on l'ignore
            print(f"'{number}' is not a number, skipped")
    return total


my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]
print(sum_numbers(my_list))


                     #Challenge1


number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

multiples = []

for i in range(1, length + 1):

    multiples.append(number * i)

print(multiples)




                   #Challenge2

mot = input("Entrer un mot : ")
nv_mot = ""
for lettre in mot:
    
    if nv_mot == "" or lettre != nv_mot[-1]:
        nv_mot = nv_mot + lettre

print(nv_mot)
             #Daily Challenge : Dictionaries
 
word = input("Enter a word: ")
 
letters = {}
for i in range(len(word)):   # Je parcours le mot avec range(len(word)) pour avoir l'index de chaque lettre.
    letter = word[i]
    if letter not in letters: # Si la lettre est pas encore dans le dico, je crée une liste vide pour elle,
        letters[letter] = []  
    letters[letter].append(i) # j'ajoute l'index dans sa liste. Comme ça une lettre qui revient garde tous ses index dans la même liste
 
print(letters)
 

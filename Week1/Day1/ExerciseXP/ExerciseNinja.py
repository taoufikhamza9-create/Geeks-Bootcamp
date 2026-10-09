             #Exercice 1


>>> 3 <= 3 < 9   #True

>>> 3 == 3 == 3    #True

>>> bool(0)   #False

>>> bool(5 == "5")   #False

>>> bool(4 == 4) == bool("4" == "4")   #True

>>> bool(bool(None)) #False

x = (1 == True) 
y = (1 == False) 
a = True + 4 
b = False + 10 

print("x is", x)   # x vaut True
print("y is", y)   # y vaut False
print("a:", a)   # True vaut 1, donc a vaut 5
print("b:", b)  # False vaut 0, donc b vaut 10



           #Exercice 2
    taille = 0

while True:
    phrase = input("Enter the longest sentence you can without the letter 'A' (or 'q' to stop): ")

    # on vérifie le q en premier pour ne pas le compter comme une phrase
    if phrase == "q":
        break


    #Je prend en compte le majuscule et minuscule 
    if "A" in phrase or "a" in phrase: 
        print("You used the letter 'A' in your sentence.")
    elif len(phrase) > taille:
        taille = len(phrase)
        print(f"Good job! New record: {taille} characters.")
    else:
        print(f"Not longer than your record ({taille} characters), better luck next time!")



            #exercice 3

paragraph = """Learning to code is a lot like learning a new language. At first, every word feels strange and every rule seems hard to remember. 
But with practice, the strange words become familiar, and the rules start to make sense.
Some days you will write code that works on the first try; other days, a single missing letter will break everything! That is normal. 
Every developer, even the best ones, spends a lot of time reading errors and fixing small mistakes. 
What matters is not to never fail, but to keep trying, step by step, until the program finally runs."""

# Au départ j'allais tout coder à la main (parcourir le texte caractère par caractère
# pour découper les mots, enlever les doublons, etc.), mais en cherchant dans la doc
# Python je suis tombé sur split(), set() et join(). Ça fait la même chose en beaucoup
# plus court, c'est plus lisible et c'est aussi plus rapide, donc je suis parti là-dessus.
taille = len(paragraph)
print(f"The paragraph has {taille} characters.")

# phrases :
phrase = 0
for i in range(taille):
    if paragraph[i] in ".!?":
        if i == taille - 1 or paragraph[i + 1] == " " or paragraph[i + 1] == "\n":
            if paragraph[i - 1] != ".":
                phrase += 1
print(f"The paragraph has {phrase} sentences.")

# mots : split() découpe aux espaces et retours à la ligne
mots = paragraph.split()
print(f"The paragraph has {len(mots)} words.")

# mots uniques : minuscules + sans ponctuation, puis set() pour enlever les doublons
texte = paragraph.lower()
for signe in ".,!?;:":
    texte = texte.replace(signe, "")
mots_uniques = set(texte.split())
print(f"The paragraph has {len(mots_uniques)} unique words.")

# bonus : caractères hors espaces = on colle tous les mots avec join()  et on mesure
non_espace = len("".join(mots))
print(f"The paragraph has {non_espace} non-whitespace characters.")

# bonus : moyenne de mots par phrase 
# .1f pour 1 chiffre après la virgule
print(f"There are on average {len(mots) / phrase:.1f} words per sentence.")

# bonus : mot non uniques = total des mot - mot différent
print(f"The paragraph has {len(mots) - len(mots_uniques)} non-unique words.")

#Resulta attendu , (trace de l'algorithme ): 
#The paragraph has 556 characters.
#The paragraph has 7 sentences.
#The paragraph has 99 words.
#The paragraph has 72 unique words.
#The paragraph has 455 non-whitespace characters.
#There are on average 14.1 words per sentence.
#The paragraph has 27 non-unique words.
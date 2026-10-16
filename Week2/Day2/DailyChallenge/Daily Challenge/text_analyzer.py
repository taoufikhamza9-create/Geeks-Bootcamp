                             #Daily Challenge : Text Analysis

class TextAnalyzer:
    def __init__(self, text):
        if text == "":
            raise Exception("The text can't be empty")
        self.text = text

    def __str__(self):   # appelé quand on fait print(analyzer)
        return f"TextAnalyzer object with {self.word_count()} words"

    def __len__(self):   # appelé quand on fait len(analyzer)
        return len(self.text)

    def word_count(self):
        return len(self.text.split())   # J'ai chercher j'ai trouver split() qui coupe le texte à chaque espace et donne une liste de mots
                            
    def count_word(self, word):
        if word == "":
            raise Exception("The word can't be empty")
        count = 0
        for w in self.text.split():
            if w == word:
                count += 1
        return count

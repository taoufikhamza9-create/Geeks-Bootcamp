                   #Daily Challenge : Text Analysis

from text_analyzer import TextAnalyzer

text = "Python is fun and Python is powerful"
analyzer = TextAnalyzer(text)

print(analyzer)
print(len(analyzer))
print(analyzer.word_count())
print(analyzer.count_word("Python"))

analyzer2 = TextAnalyzer("Python")
print(analyzer2)
print(len(analyzer2))
print(analyzer2.count_word("Java"))

# le try/except évite que le programme s'arrête au premier test
try:
    empty_analyzer = TextAnalyzer("")
except Exception as error:   # error contient le message qu'on a mis dans le raise
    print(f"Error: {error}")

try:
    analyzer.count_word("")
except Exception as error:
    print(f"Error: {error}")

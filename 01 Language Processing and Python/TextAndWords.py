import nltk
from nltk.book import *

print(text1)
print(text2)

# Searching Text

## .concordance() : shows us every occurence of a given word

print("In text1 : ")
print(text1.concordance("monstrous"))

print("In text2 : ")
print(text2.concordance("affection"))

print("In text3 : ")
print(text3.concordance("lived"))

print("In text4 : ")
print(text4.concordance("god"))
print(text4.concordance("nation"))
print(text4.concordance("terror"))

print("In text5 :")
print(text5.concordance("lol"))
print(text5.concordance("im"))
print(text5.concordance("ur"))


## .similar() : words appearing in a similar range of context

print(text1.similar("monstrous"))
print(text2.similar("monstrous"))

print(text2.similar("affection"))

print(text3.similar("lived"))

print(text4.similar("god"))
print(text4.similar("nation"))
print(text4.similar("terror"))

print(text5.similar("lol"))
print(text5.similar("im"))
print(text5.similar("ur"))

## .common_contexts() : contexts shared by two or more words

print(text2.common_contexts(["monstrous", "very"]))

print(text4.common_contexts(["god", "terror"]))
print(text5.common_contexts(["lol", "ur"]))
print(text5.common_contexts(["lol", "im"]))

## .dispersion_plot() : displays positional information

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
text5.dispersion_plot(["lol", "im", "ur"])

## .generate() : generates some random text

text3.generate()
text4.generate()
text5.generate()

# Counting Vocabulary

print(len(text3))
print(len(text4))
print(len(text5))

print(len(set(text3)))
print(len(set(text4)))
print(len(set(text5)))

print(sorted(set(text3)))
print(sorted(set(text4)))
print(sorted(set(text5)))

print(len(text3) / len(set(text3)))         # It shows each word is used 16 times on an Average (Lexical Diversity)
print(len(text4) / len(set(text4)))
print(len(text5) / len(set(text5)))

print(text3.count("smote"))
print(text4.count("god"))
print(text5.count("lol"))

print(100 * text4.count('a') / len(text4))  # It calculates what percentage of the text is taken up by a specific word

print(text5.count('lol'))
print(100 * text5.count('lol') / len(text5))

print(text5.count('ur'))
print(100 * text5.count('ur') / len(text5))

print(text5.count('im'))
print(100 * text5.count('im') / len(text5))


def lexical_diversity(text):
    return len(text) / len(set(text))


def percentage(count, total):
    return 100 * count / total


print("Average of each word used in text3 : ", lexical_diversity(text3))
print("Average of each word used in text5 : ", lexical_diversity(text5))

print(percentage(4, 5))
print("Percentage of 'a' word used in text4 : ",
      percentage(text4.count('a'), len(text4)))
print("Percentage of 'lol' word used in text5 : ",
      percentage(text5.count('lol'), len(text5)))


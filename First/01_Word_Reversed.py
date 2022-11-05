# Если слово больше или равно 5 букв то делаем reverse букв если меньше оставляем неизменным.
#
def spin_words(sentence):
    words = sentence.split(" ")
    newSentence = []
    for word in words:
        if len(word) >= 5:
            rWorld = word[::-1]
        else:
            rWorld = word
        newSentence.append(rWorld)
    return " ".join(newSentence)

print(spin_words("Geeks for Geeks"))


# Тоже самое короче. Best Practices:
# def spin_words(sentence):
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

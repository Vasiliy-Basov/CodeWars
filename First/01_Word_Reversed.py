#!/bin/python3
# --------------------------------------------------------------------------
# Program by Vasiliy.B.
#
# Version   Date           Info
# 1.0       06.11.2022     Initial Version
# --------------------------------------------------------------------------

# Если слово больше или равно 5 букв то делаем reverse букв если меньше оставляем неизменным.

def spin_words(sentence):
    words = sentence.split(" ")   # Разделяем наше предложение слова, разделитель пробел
    newsentence = []              # Создаем пустой список
    for word in words:
        if len(word) >= 5:
            rword = word[::-1]    # Меняем местами буквы -1 значит что шаг -1
        else:
            rword = word
        newsentence.append(rword) # Добавляем в наш список измененное или неизменное слово
    return " ".join(newsentence)  # Делаем из списка строку с разделителем пробел

print(spin_words("Geeks for Geeks"))


# Тоже самое короче. Best Practices:
# def spin_words(sentence):
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

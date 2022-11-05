def digital_root(n):
    while len(str(n)) >= 2:
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        n = sum
    return n
print(digital_root(1356789))


# Быстрое решение
# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))

# Или
# def digital_root(n):
#     while n>9:
#         n=sum(map(int,str(n))) - т.е. мы применяем функцию int к str(n) где str(n) будет итерируемым объектом т.е. разбит на цифры
#         а на выходе мы получаем эти цифры и сумируем.
#     return n

# https://www.digitalocean.com/community/tutorials/how-to-use-the-python-map-function-ru
# функция map() используется для применения функции к каждому элементу итерируемого объекта
# (например, списка или словаря) и возврата нового итератора для получения результатов.
import count_greater_than

# Получаем список чисел и значение для сравнения от пользователя
list_a = list(map(int, input("Введите список чисел, разделенных пробелами: ").split()))
value = int(input("Введите значение для сравнения: "))

# Вызываем функцию из модуля и выводим результат
count = count_greater_than.count_greater_than(list_a, value)
print(f"Количество элементов, превышающих {value}: {count}")
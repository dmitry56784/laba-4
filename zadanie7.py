import max_digit_sum

# Получаем список чисел от пользователя
numbers = list(map(int, input("Введите список целых чисел, разделенных пробелами: ").split()))

# Вызываем функции из модуля и выводим результат
max_number = max_digit_sum.max_digit_sum(numbers)
print(f"Число с максимальной суммой цифр: {max_number}")
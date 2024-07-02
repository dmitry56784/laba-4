def count_greater_than(list_a, value):
  """Подсчитывает количество элементов в списке list_a,
  которые превышают заданное значение value.

  Args:
    list_a: Список чисел.
    value: Заданное значение для сравнения.

  Returns:
    Количество элементов, превышающих value.
  """

  count = 0
  for number in list_a:
    if number > value:
      count += 1

  return count
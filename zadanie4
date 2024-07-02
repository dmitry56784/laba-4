import datetime

def get_next_lucky_date(date, n):
  """Возвращает следующую подходящую дату экзамена."""

  # Преобразуем дату в объект datetime
  date = datetime.datetime.strptime(date, "%Y/%m/%d")

  # Устанавливаем флаг, указывающий, что мы нашли подходящую дату
  found = False

  # Перебираем дни, пока не найдем подходящую дату
  while not found:
    # Прибавляем к дате n дней
    date += datetime.timedelta(days=n)

    # Проверяем, является ли номер дня кратным четырем или это понедельник
    if date.day % 4 == 0 or date.weekday() == 0:
      continue

    # Если дата подходит, устанавливаем флаг и возвращаем дату
    found = True

  # Возвращаем подходящую дату
  return date


def main():
  # Получаем исходную дату и число n от пользователя
  date_str, n = input("Введите исходную дату в формате YYYY/MM/DD и число n: ").split()

  # Преобразуем исходную дату в объект datetime
  date = datetime.datetime.strptime(date_str, "%Y/%m/%d")

  # Получаем три подходящие даты экзамена
  lucky_dates = []
  for i in range(3):
    date = get_next_lucky_date(date, n)
    lucky_dates.append(date)

  # Выводим подходящие даты на экран
  for date in lucky_dates:
    print(date.strftime("%d %B, %A"))


if __name__ == "__main__":
  main()
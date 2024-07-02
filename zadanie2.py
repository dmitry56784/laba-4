import random

disciplines = []
weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
times = ["9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00"]
lucky_tickets = list(range(1, 21))

def get_random_element(list):
  return random.choice(list)
num_exams = int(input("Введите количество экзаменов: "))
disciplines_str = input("Введите наименования дисциплин через запятую и пробел: ")
disciplines = disciplines_str.split(", ")
for discipline in disciplines:
  weekday = get_random_element(weekdays)
  time = get_random_element(times)
  lucky_ticket = get_random_element(lucky_tickets)
  times.remove(time)
  lucky_tickets.remove(lucky_ticket)
  print(f"Экзамен по дисциплине «{discipline}» состоится в {weekday} время {time}. Ваш счастливый билет N {lucky_ticket}.")
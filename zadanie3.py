import datetime

def days_to_date(days):
  today = datetime.date.today()
  exam_date = today + datetime.timedelta(days=days)
  day = exam_date.day
  month = exam_date.month
  return day, month
def main():
  days = int(input("Введите количество дней до экзамена: "))
  day, month = days_to_date(days)
  print(f"Экзамен состоится {day} {month}")


if __name__ == "__main__":
  main()
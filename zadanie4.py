import datetime

def get_next_lucky_date(date, n):
    while True:
        date += datetime.timedelta(days=n)
        if date.weekday() != 0 and date.day % 4 != 0:
            return date

def main():
    date_str, n = input("Введите исходную дату в формате YYYY/MM/DD и число n: ").split()
    date = datetime.datetime.strptime(date_str, "%Y/%m/%d")

    lucky_dates = []
    for i in range(3):
        date = get_next_lucky_date(date, n)
        lucky_dates.append(date)

    for date in lucky_dates:
        print(date.strftime("%d %B, %A"))
if __name__ == "__main__":
    main()
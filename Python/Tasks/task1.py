# ➔	Напишите программу, которая запрашивает у пользователя последовательно день его рождения, месяц и год;
# ➔	Напишите функцию, которая определяет какому дню недели соответствует эта дата?
# ➔	Напишите функцию, которая определяет - високосный это был год, или нет?
# ➔	Напишите функцию, которая определяет сколько сейчас лет пользователю;
# ➔	Реализуйте вывод в консоль даты рождения пользователя в формате дд мм гггг, где цифры прорисованы звёздочками (*), как на электронном табло.
import locale

from datetime import datetime

locale.setlocale(locale.LC_TIME, 'Russian')

# Запрашиваем дату рождения
date_of_birth, month_of_birth, year_of_birth = map(int,
                                                   input("Введите дату своего рождения (день месяц год): ").split())


# Функция определения дня недели
def get_day_of_week(date_of_birth, month_of_birth, year_of_birth):
    date = datetime(int(year_of_birth), int(month_of_birth), int(date_of_birth))
    day_of_week = date.strftime("%A")
    return day_of_week


# Функция, которая определяет - високосный это был год, или нет
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Год был високостный"
    else:
        return "Год был невисокосный"


# Функция, которая определяет определяет сколько сейчас лет пользователю
def age(day, month,year):
    current_datetime = datetime.now()
    current_year = current_datetime.year
    current_month = current_datetime.month
    current_day = current_datetime.day

    age_now = current_year - year

    if (current_month < month) or (current_month == month and current_day < day):
        age_now -= 1
    return age_now


def tablo(date: int, month: int, year: int):
    digit_mapping = {
        '0': [" ***** ", "*     *", "*     *", "*     *", " ***** "],
        '1': ["   *   ", "   *   ", "   *   ", "   *   ", "   *   "],
        '2': [" ******", "      *", " ******", "*      ", " ******"],
        '3': [" ******", "      *", " ******", "      *", " ******"],
        '4': ["*     *", "*     *", " ******", "      *", "      *"],
        '5': [" ******", "*      ", " ******", "      *", " ******"],
        '6': [" ******", "*      ", " ******", "*     *", " ******"],
        '7': [" ******", "      *", "     * ", "    *  ", "    *  "],
        '8': [" ******", "*     *", " ******", "*     *", " ******"],
        '9': [" ******", "*     *", " ******", "      *", " ******"],
        ' ': ["       ", "       ", "       ", "       ", "       "],
    }

    date_str = f"{date:02d} {month:02d} {year}"
    output_lines = ["", "", "", "", ""]
    for char in date_str:
        digit_representation = digit_mapping[char]
        for i in range(5):
            output_lines[i] += digit_representation[i] + "  "  # Добавляем пробелы для разделения цифр

    for line in output_lines:
        print(line)

print(f"День недели, когда Вы родились был {get_day_of_week(date_of_birth, month_of_birth, year_of_birth)}")
print(leap_year(year_of_birth))
print(f"Вам сейчас {age(date_of_birth, month_of_birth, year_of_birth)} лет")
tablo(date_of_birth, month_of_birth, year_of_birth)

from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        try:
            user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            birthday_this_year = user_birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_next_year = birthday_this_year.replace(year=today.year + 1)
                print(f"{user['name']} congratulation day next year:", birthday_next_year)

            days_until_birthday = (birthday_this_year - today).days

            if 0 <= days_until_birthday <= 7:

                birthday_on_weekday = (today + timedelta(days=days_until_birthday)).weekday()

                if birthday_on_weekday in [5, 6]:
                    days_until_birthday = days_until_birthday + (7 - birthday_on_weekday)

                congrats_date = today + timedelta(days=days_until_birthday)
                congrats_date_str = congrats_date.strftime("%Y.%m.%d")
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": congrats_date_str})

        except ValueError:
            print(f"Invalid entry date {user['name']}.")

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.02.09"},
    {"name": "Jane Smith", "birthday": "1990.03.04"},
    {"name": "Іван", "birthday": "1988/03/10"},
    {"name": "Марія", "birthday": "1987.03.10"},
    {"name": "Петро", "birthday": "1977.03.15"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
for user_birthday in upcoming_birthdays:
    print(f"{user_birthday['name']} - congratulation_date: {user_birthday['congratulation_date']}")
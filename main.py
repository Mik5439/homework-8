from datetime import date, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    current_date = date.today()
    current_year = current_date.year

    # Ініціалізуємо словник для зберігання користувачів за днями тижня
    birthdays_per_week = {}

    # Проходимося по списку користувачів
    for user in users:
        # Отримуємо дату народження користувача 
        birthday = user.get('birthday')

        # Отримуємо дату народження користувача у цьому році
        if birthday.month == 1:
                birthday_this_year = birthday.replace(year=current_year + 1)
        else:
            birthday_this_year = birthday.replace(year=current_year)

        # Визначимо день тижня
        day_of_week = birthday_this_year.strftime("%A")

        # Додаємо користувачів до словника, якщо вони задовільняють умови
        if birthday_this_year >= current_date and birthday_this_year <= current_date + timedelta(days=6):
            if day_of_week in ("Saturday", "Sunday"):
                day_of_week = 'Monday' 
                
            if day_of_week not in birthdays_per_week:
                birthdays_per_week[day_of_week] = []
            birthdays_per_week[day_of_week].append(user.get("name"))
        else:
            continue
    return birthdays_per_week

if __name__ == "__main__":
    users = []

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

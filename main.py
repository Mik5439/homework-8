from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    if len(users) >= 1:
        # Отримуємо поточну дату
        current_date = date.today()
        current_year = date.today().year

        # Ініціалізуємо словник для зберігання користувачів за днями тижня
        birthdays_per_week = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        }
        list = []
        # Проходимося по списку користувачів
        for user in users:
            # Отримуємо дату народження користувача 
            birthday = user.get('birthday')

            # Отримуємо дату народження користувача у цьому році
            birthday_this_year = birthday.replace(year=current_year)
            
            # Отримуємо дату початку року
            start_of_year = date(current_date.year, 1, 1)
            
            # Визначаємо скільки днів руку минуло
            days_passed_this_year = (current_date - start_of_year).days - 1
            
            # Визначаємо на якому дні року день народження
            birthday_day_of_year = (birthday_this_year - start_of_year).days
            
            # Визначимо день народження на наступному тижні
            day_of_week = birthday_this_year.strftime("%A")
            
            if int(days_passed_this_year) < int(birthday_day_of_year + 1):
                if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                    day_of_week = 'Monday'
                next_week = current_date + timedelta(days=6)
                # Якщо день народження цього тижня, додамо до відповідного списку
                if birthday_this_year >= current_date and birthday_this_year <= next_week:
                    if next_week.year <= start_of_year.year:
                        birthdays_per_week[day_of_week].append(user.get('name'))   
                else:
                    continue   
            if int(days_passed_this_year) > int(birthday_day_of_year + 1):
                continue
        # Перевіряємо чи не пустий список з днями народженями
        for val in birthdays_per_week.values():
            if len(val) != 0:
                list.append(val)
        if len(list) == 0:
            birthdays_per_week = {}
        return birthdays_per_week
    return {}


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(2023, 6, 17).date()},
        {"name": "test", "birthday": datetime(1988, 5, 29).date()},
        {"name": "mik", "birthday": datetime(1976, 9, 17).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

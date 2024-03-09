from datetime import datetime

users = [{"name": "Bill Gates", "birthday": datetime(1955, 3, 10)},{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}]

def get_birthdays_per_week(users):
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            pass
        else:
            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                print(delta_days.strftime("%A"))
    
    
    
    return

get_birthdays_per_week(users)
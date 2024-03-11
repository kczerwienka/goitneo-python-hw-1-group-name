from datetime import datetime

def get_birthdays_per_week(users):
    today = datetime.today().date()
    res={}
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            pass
        else:
            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                if (birthday_this_year.strftime("%A") == "Saturday" or birthday_this_year.strftime("%A") == "Sunday") and today.strftime("%A") == "Monday":
                    if res.get("next_Monday") is None:
                        res["next_Monday"]=[name]
                    else:
                        res["next_Monday"].append(name)
                elif (birthday_this_year.strftime("%A") == "Saturday" or birthday_this_year.strftime("%A") == "Sunday") and today.strftime("%A") != "Monday":
                    print("M")
                    if res.get("Monday") is None:
                        res["Monday"]=[name]
                    else:
                        res["Monday"].append(name)
                else:
                    if res.get(birthday_this_year.strftime("%A")) is None:
                        res[birthday_this_year.strftime("%A")]=[name]
                    else:
                        res[birthday_this_year.strftime("%A")].append(name)

    
    for k, v in res.items():
        j_v = ", ".join(v)
        print(f"{k}: {j_v}")
    
    return


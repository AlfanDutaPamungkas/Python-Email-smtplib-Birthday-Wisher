import pandas
import datetime as dt
import smtplib
import random
from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD") # password app not your password email

now = dt.datetime.now()
month = now.month
day = now.day

temps = ["./letter_templates/letter_1.txt","./letter_templates/letter_2.txt","./letter_templates/letter_3.txt"]
temp = random.choice(temps)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = data.to_dict("index")

for i in birthdays_dict:
    if month == birthdays_dict[i]["month"] and day == birthdays_dict[i]["day"]:
        with open(temp) as file:
            mail = file.read()
            new_mail = mail.replace("[NAME]",birthdays_dict[i]["name"])
            
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthdays_dict[0]["email"],
                msg=f"Subject:Happy Birthday\n\n{new_mail}"
            )
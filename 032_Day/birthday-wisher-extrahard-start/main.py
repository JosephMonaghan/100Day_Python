##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib


email = "JM.Python.Learn@gmail.com"
app_passcode ="lnvq tenb dvxx darv"


# 1. Update the birthdays.csv
#read in birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")

#base letter



today = dt.datetime.now()
for idx, person in birthdays.iterrows():
    if person.month == today.month and person.day == today.day:
        let_num = random.randint(1,3)
        with open(f"./letter_templates/letter_{let_num}.txt") as file:
            base_letter = file.readlines()
        base_letter="".join(base_letter)
        named_letter = base_letter.replace("[NAME]", person.title)
        birthday_message = f"Subject: Happy Birthday!\n\n {named_letter}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password=app_passcode)
            connection.sendmail(from_addr=email,to_addrs=person.email,msg=birthday_message)



# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





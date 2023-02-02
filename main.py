# This script sends someone a random motivational quote every Monday

from random import choice
import datetime as dt
import smtplib

MY_EMAIL = "youremailaddress@gmail.com"  # Change this
MY_PASSWORD = "yourpassword"  # Change this, DO NOT use your actual password. Create an App Password instead.
# How to set up an App Password for gmail: https://support.google.com/accounts/answer/185833
RECIPIENT_EMAIL = "recievingemailaddress@website.com"  # Change this

now = dt.datetime.now()

if now.weekday() == 0:  # 0 = Monday, 1 = Tuesday ... 6 = Sunday
    with open("quotes.txt") as quotes:
        list_of_quotes = quotes.readlines()
        random_quote = choice(list_of_quotes)

    with smtplib.SMTP(
            "smtp.gmail.com:587"  # Change this if you're sending emails from somewhere other than gmail
    ) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECIPIENT_EMAIL,
                            msg=f"Subject:Monday Motivation!\n\n{random_quote}")

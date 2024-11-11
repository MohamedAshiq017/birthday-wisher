import datetime as dt
import pandas 
import random
import smtplib

MY_NAME="Mohamed Ashiq" #replace with your name 
MY_MAIL="abcdefghijklmmno@gmail.com" # replace your mail id
PASSWORD="abcdefghijklmno" #replace the password you created , for more information on how to create a less secure app password check README file 
SUBJECT="HAPPY BIRTHDAY" #change the subject line if you want to 

book=pandas.read_csv("birthdays.csv")
df=pandas.DataFrame(book)


today=dt.datetime.now()
print(f"Date:{today}")

for index,entry in df.iterrows():
  if entry['day']==today.day and entry['month']==today.month:
    print(f"\n\t{entry['name']} \t{entry['email']}")
    with open(f"./letter_templates/letter_{str(random.randint(1,3))}.txt",'r') as letter:
      content=letter.read()
    new_letter=content.replace("[NAME]",entry['name']).replace('MY_NAME',MY_NAME)
    print(f"\n{new_letter}")
    to_email=entry["email"]

    with smtplib.SMTP("smtp.gmail.com") as connection:   #if you are not using gmail then check for the smtp address of your mail service and replace the string.
      connection.starttls()
      connection.login(user=MY_MAIL,password=PASSWORD)
      connection.sendmail(from_addr=MY_MAIL,to_addrs=to_email,msg=f"subject:{SUBJECT}\n\n\n{new_letter}")




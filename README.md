# Birthday Wisher Automation Project

This is an automated Python project that sends personalized birthday wishes via email. By reading birthday data from a CSV file and selecting a random birthday message template, the program customizes the content and sends an email on the recipient's special day.

## Project Overview

The script reads a CSV file (`birthdays.csv`) containing birthday information, checks if any birthdays match the current date, selects a random letter template, customizes it with the recipient's name, and sends the email using SMTP.

### Features
- Sends personalized birthday greetings via email.
- Reads birthday data from a CSV file.
- Randomly selects one of three letter templates for variety.
- Uses Python's `smtplib` for email automation and `pandas` for handling data.

## Setup and Installation
Prepare the CSV file: Create a birthdays.csv file with the following format:

csv
name,email,year,month,day
Soldier Boy,soldierboy@example.com,2002,4,16
Billy Butcher,butcher@example.com,1985,5,25
Create letter templates: Prepare three text files (letter_1.txt, letter_2.txt, letter_3.txt) inside a letter_templates folder. Include [NAME] as a placeholder for the recipient's name in each template.

Set up SMTP details: Replace MY_MAIL and PASSWORD in the script with your email and an app-specific password (not your main email password). For Gmail users:
Make sure 2 step verification is enabled.
if app passwords not visible in the manage account window use the search bar and search for "App passwords" it'll show up then name it as anything and copy the password for the later use.
Enable "Allow less secure apps" or create an App Password.
while using the password in code ensure it has no space in between or at the beggining(Total 16 characters).
![step2](https://github.com/user-attachments/assets/a9ae5bd6-567d-4154-8dbd-c55391c90be2)


Code Explanation
datetime module: Used to get the current date.
pandas module: Reads and handles data from birthdays.csv.
smtplib module: Connects to the email server and sends the email.


Customization
Letter templates: Modify the content of letter_1.txt, letter_2.txt, and letter_3.txt as needed. Use [NAME] in the template where the recipient's name should appear.
Email Subject: Change the SUBJECT variable to customize the email subject line.
birthdays.csv: in the sme format 

##Automation:
Create an account on "python anywhere" and zip this repository and upload the zip file
Using the console unzip the zipped folder 
example: unzip birthday-wisher.zip

![step3](https://github.com/user-attachments/assets/733eb417-9b15-4e3b-ac65-1778dbf930ce)


Test Your Script:
Open a Bash Console.
Navigate to your project directory:
cd birthday-wisher
Run your script to ensure everything is working:
python main.py


6. Schedule Your Script
Go to the Tasks tab on your PythonAnywhere dashboard.
Click on Add a new scheduled task.
Enter the command to run your script:
python3.x /home/yourusername/birthday_wisher/main.py
Set the time for the task to run daily (e.g., 00:01 or 12:00) based on when you want the emails to be sent.
Check your timezone against UTC and choose the right UTC time of your preference to run the task

![step4](https://github.com/user-attachments/assets/906cc19e-2429-4689-ac72-f40977889e6f)

##Notes:
To create a less secure app passsword, you need to turn on the 2 steps verfication, then only you can create app passwords

update the birthday.csv with the example format provided and you can update the birthday.csv file on the python anywhere itself.
it will work even if multiple people born at same day

filenotfound error 
in main.py change the path of the letters, birthday.csv ,etc., file paths to absolute path

if packages missing
using the bash 
install the missing packages
example: pip install pandas

See Ya!




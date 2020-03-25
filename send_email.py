import smtplib
email_list = []
n = int(input('Enter no. of recipients: '))
for x in range(n):
    email_str = input('Recpient email %d : '%(x+1))
    email_list.append(email_str)
password_log = input()

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
smtpObj.ehlo()
smtpObj.login('bensonpx1198@gmail.com',password_log)
smtpObj.sendmail('bensonpx1198@gmail.com',email_list, 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Ben')
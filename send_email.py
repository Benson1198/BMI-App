import smtplib
email_list = []
email_id = input('Enter your email id: ')
password_log = input("Enter your password: ")
n = int(input('Enter no. of recipients: '))
for x in range(n):
    email_str = input('Recpient email %d : '%(x+1))
    email_list.append(email_str)


smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
smtpObj.ehlo()
smtpObj.login(email_id,password_log)
smtpObj.sendmail(email_id ,email_list, 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Ben')
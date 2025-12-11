import requests as request
from time import sleep
import yagmail as mail

lastip = ''
currentip = ''

user = '{SENDER_MAIL}@gmail.com'
app_password = '{APP_PASSWD}'
to = '{RECIEVER_MAIL}@gmail.com'

subject = 'Your IP has changed!'
content = []


while True:
    sleep(300)
    try:
        response = request.get("https://ifconfig.me/")
        currentip = response.content.decode(encoding='utf-8')
    except:
        print("No gateway to internet found")
        
    if lastip != currentip:
        print(f"CurrentIP: {currentip}\nLastIP: {lastip}")
        content = [f"Your new ip is: {currentip}"]
        print(content)
        lastip = currentip
        
        with mail.SMTP(user, app_password) as sendmail:
            try:
                sendmail.send(to, subject, content)
                print("Success")
            except:
                print("Mail not sent")
    else:
        print("No ip changes")
    


import imaplib
import base64

def get_mail_client(email_address):
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993
    password = "!"
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(email_address, password)
    return mail
m=(get_mail_client('singh.shubham987@gmail.com'))
m.select()
_, message_numbers_raw = m.search(None, 'FROM cofp.ru')
for message_number in message_numbers_raw[0].split():
    _, msg = m.fetch(message_number, '(UID BODY[TEXT])')
    result=str(base64.b64decode((msg[0][1])))
    print(result)
    

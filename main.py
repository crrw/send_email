import logging
import requests
import smtplib

def main():
    name = ''
    email = ''
    password = ''

    server = smtplib.SMTP_SSL('stmp.gmail.com', 465)
    server.ehlo
    server.login(email, password)

    # https://www.apispreadsheets.com/
    req = requests.get("https://api.apispreadsheets.com/data/3727/")

    if req.status_code == 200:
        data = req.json()['data']
    else:
        data = None
        raise ValueError('Error connecting to api')

    for i in len(data):
        email_name = data[i]["Name"].strip()
        email_address = data[i]["Email"].strip()
        email_subject = data[i]["Subject"].strip()
        email_message = data[i]["Message"].strip()

        full_email = ("From: {0} <{1}>\n"
                      "To: {2} <{3}>\n"
                      "Subject: {4}\n\n"
                      "{5}".format(name, email, email_name, email_address, email_subject, email_message))

    try:
        server.sendmail(email, [email_address], full_email)
        logging.info('Sending email to {to}'.format(to='email_address'))

    except Exception as ex:
        logging.info('Could not send email', ex)

    
    server.close()



if __name__ == '__main__':
    main()

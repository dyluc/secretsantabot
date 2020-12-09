import smtplib


def send_email(username, password, send_to_email, message):  # username, password of sender login
    print("Connecting...")
    server = smtplib.SMTP('smtp.gmail.com', 587, timeout=120)
    server.ehlo()
    server.starttls()
    server.login(username, password)

    try:
        server.sendmail(username, send_to_email, message)
        print("Successful, message sent to %s!" % send_to_email)
    except Exception as error:
        print("Error while sending mail to %s." % send_to_email)
        print("Error message: ", error)

    server.quit()

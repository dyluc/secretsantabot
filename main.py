import readdetails
import calculatematches
import smtp_send_names

# 1 ------
details_url = 'res/emails.txt'
sender_url = 'res/sender.txt'
message_url = 'res/message.txt'

details = readdetails.read_details(details_url)  # Read file into tuple
names = details[0]
emails = details[1]
sender_login = {"email": readdetails.read_sender(sender_url)[0].replace(' ', '').strip('\n'),
                "pswrd": readdetails.read_sender(sender_url)[1].replace(' ', '')}
message_string = readdetails.read_message(message_url)
# ---------
# 2---------
matches_dict = calculatematches.return_matches(names)
# ----------

# 3--------
# log matches to log.txt
with open("log.txt", 'a') as log_m:
    log_m.seek(0)
    log_m.truncate()
    for k, v in matches_dict.items():
        log_m.write(k + " -> " + v + "\n")
# ---------
# 4--------
for index, person in enumerate(names):
    person_email = emails[index]
    s_santa = matches_dict[person]
    msg = """From: {}\nTo: {}\nSubject: Test Subject!\n""".format(
        sender_login["email"],
        person_email)
    msg += message_string.format(to=person, ss=s_santa)
    smtp_send_names.send_email(
        sender_login["email"],
        sender_login["pswrd"], 
        person_email, msg)
# ---------

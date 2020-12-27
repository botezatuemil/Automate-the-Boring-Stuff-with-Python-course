import imapclient
import datetime
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)  # second argument for wanting the ssl encryption
print(conn.login('btzemil@gmail.com', 'emil14pro'))
print(conn.select_folder('INBOX', readonly=True))  # the folder you want to check
UIDs = conn.search(['SINCE', datetime.date(2020, 11, 19)])  # search the email from the date, it returns a code
print(UIDs)

rawMessage = conn.fetch([5221], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessage[5221][b'BODY[]'])

print(message.get_subject())
print(message.get_addresses('from'))  # show from who to who
print(message.text_part)  # show if exists some text part
print(message.html_part)
print(message.text_part.get_payload().decode('UTF-8'))  # print the actual message

print(conn.list_folders())  # show all the folders of email
conn.select_folder('INBOX', readonly=False)
UIDs = conn.search(['ON', datetime.date(2020, 11, 19)])
print(UIDs)
# conn.delete_messages([5219]) delete the email with the associated code
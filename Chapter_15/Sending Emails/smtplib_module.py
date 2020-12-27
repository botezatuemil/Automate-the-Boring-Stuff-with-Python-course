import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)  # define the object
print(conn.ehlo())  # make the connection to the server
print((conn.starttls()))  # encrypt the email
print(conn.login('btzemil@gmail.com', 'emil14pro'))
conn.sendmail('btzemil@gmail.com', 'btzemil@gmail.com', 'Subject: Ba nu stiu...\n\nBa Emil esti cam tanc, \nCu drag, \n\nEmil')
conn.quit()
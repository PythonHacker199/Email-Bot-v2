# hello guys
# welcome to hacker python channel
# Today we are here to make email bot V2
# first you need to install yagmail package
import  yagmail

reciever="Sender email"
body="hello there from hacker python"
filename="ok.py"

yag=yagmail.SMTP("your email","password")
yag.send(
    to=reciever,
    subject="Email Bot v2",
    contents=body,
    attachments=filename,
)
# So guys today also we have to pass parameters like less app secure in google account
# so bye guys have a nice day
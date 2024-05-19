import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_email(to='menniablaise@gmail.com', text_message='test email', html=False, html_message='<b>test email</b>'):
    sender_email = "blaise.s.mennia@gmail.com"
    reciever_email = to
    password = "kvlilewhmciuyjiz"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Jobobot"
    message["From"] = sender_email
    message["To"] = reciever_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <html>
    <body>
        <p>Hi,<br>
        How are you?<br>
        <a href="http://www.realpython.com">Real Python</a> 
        has many great tutorials.
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects --- Check if html or plain message
    if html:
        part2 = MIMEText(html_message, "html")
        message.attach(part2)
    else:
        part1 = MIMEText(text_message, "plain")
        message.attach(part1)

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, reciever_email, message.as_string()
        )


# send_email()
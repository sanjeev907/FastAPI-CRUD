# import os
# from email.message import EmailMessage
# import ssl
# import smtplib


# email_sender = 'skunknown7991@gmail.com'
# email_password = os.environ.get('EMAIL_PASSWORD')
# email_recevier = 'sanjeevkaushik7991@gmail.com'

# subject = "it was mail for use the mail"
# body = """
#     this the lorem
# """

# em = EmailMessage()

# em['From']=email_sender
# em['To']= email_recevier
# em['subject'] = subject
# em.set_content(body)


# content = ssl.create_default_context()

# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=content) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_recevier, em.as_string())

import smtplib



sender_email = os.environ.get('SANJEEV_EMAIL')
sender_password = os.environ.get('SANJEEV_EMAIL_PASSWORD')


def send_email(to_email, subject, body, cc=""):
    # Gmail SMTP server settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # TLS port
    
    # Create SMTP connection
    smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
    smtp_conn.ehlo()  # Identify yourself to the SMTP server
    smtp_conn.starttls()  # Enable encryption (TLS)
    smtp_conn.ehlo()  # Re-identify yourself after encryption
    
    # Log in to your Gmail account
    smtp_conn.login(str(sender_email), str(sender_password))
    
    # Compose the email
    email_headers = [
        f'From: {sender_email}',
        f'To: {to_email}',
        f'Subject: {subject}',
    ]
    
    if cc:
        email_headers.append(f'Cc: {cc}')
    
    email_headers.extend([
        'MIME-Version: 1.0',
        'Content-Type: text/html'
    ])
    
    email_body = body
    email_ = '\r\n'.join(email_headers + ['', email_body])
    
    # Send the email
    try:
        smtp_conn.sendmail(str(sender_email), [to_email] + ([cc] if cc else []), email_)
        smtp_conn.quit()
        return 'Email sent successfully!'
    except Exception as e:
        smtp_conn.quit()
        return f'Failed to send email. Error: {str(e)}'



# updated email func
def sendPostApprovalEmail(toEmail: str,  postTitle:str, poststatus: str, postOwnerUserName: str):
    email_body = f"""<html> <head></head> <body> 
        <p>Hi {postOwnerUserName},</p> 
        <p>Your post of postTitle: {postTitle} has been {poststatus} by admin. Please login to see details.</p><br/> 
        <p>Best regards,<br>Crypto Business World</p> </body> </html>"""

    send_email(toEmail,
              f"Post Update Notification",
              email_body.format(postTitle=postTitle, poststatus=poststatus, postOwnerUserName=postOwnerUserName),
              "sendPostApprovalEmail")

    return {"message": "mail sent successfully!"}
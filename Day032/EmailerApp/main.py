import smtplib

myemail = "bsnawder100DocInfo@gmail.com"
mypassword = "2&7ZfrKp34Q$"
email_subject = "Hello new email account!"
email_body = "Hello new test email account for my 100 Days of Code project."
email_msg = f"Subject:{email_subject}\n\n{email_body}"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=myemail, password=mypassword)
    connection.sendmail(from_addr=myemail,
                        to_addrs="bsnawder100DocTest@gmail.com",
                        msg=email_msg
    )


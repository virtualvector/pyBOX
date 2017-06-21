import smtplib

def main():
    fromaddr = 'rohithrajreganti@gmail.com'
    toaddrs  = 'rohithrajreganti@gmail.com'
    msg = "\r\n".join([
      "From: rohithrajreganti@gmail.com",
      "To: rohithrajreganti@gmail.com",
      "Subject: Just a message",
      "","Why, oh why" ])
    username = 'rohithrajreganti@gmail.com'
    password = 'iamsherlockholmes'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    
if __name__ == '__main__':
    main()
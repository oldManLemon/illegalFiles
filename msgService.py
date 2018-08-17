import smtplib
import settings
from string import Template
import offendersLookup as lookup

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
MY_USER = settings.masterUser
MY_ADDRESS = 'passive-aggressive-bot@bornhorstward.com.au'
PASSWORD = settings.masterPass

def emailService(jobNumber, illegalFiles):
    #print(jobNumber)
    #print(illegalFiles)
    firstName = []
    lastName = []
    email = ['a.hase@bornhorstward.com.au']
    contacts = lookup.dataMagic(jobNumber)
    for contact in contacts:
        #print(contact)
        #firstName = contact[0]
        #lastName = contact[1]
        #email = contact[2]
        firstName.append(contact[0])
        lastName.append(contact[1])
        email.append(contact[2])
        #print(firstName, lastName, email)
    #print('Firstname:', firstName)
    #print('Lastname:', lastName)
    #print('Email:', email)
        # set up the SMTP server
    s = smtplib.SMTP(host='mail.bornhorstward.com.au', port=25)
    s.starttls()
    s.login(MY_USER, PASSWORD)
    msg = MIMEMultipart()
    sendto = ''
    for address in email:
        try:
            sendto+=','+address
        
        except TypeError:
            sendto+=''


            # setup the parameters of the message
    print(sendto)        
    msg['From']=MY_ADDRESS
    msg['To']=sendto
    msg['Subject']=jobNumber+" Contains files that should be filed elsewhere"
    #messageTemplate = read_template('message.txt')
    message = "<div style='line-height: 1.5; font-family:  Calibri, sans-serif; font-size: 16px; color: rgba(0, 0, 0, 0.87);'>"
    message += "Hey  "
    for fname in firstName:
        message += fname+", "
    message += f"<br><br>You are being sent this email because you are registered as working on <b>{jobNumber}</b>.<br>"
    message += f"As per BW's procedures <a href='http://bwwiki:49494/point-cloud-procedures/'>Point Cloud, CCTV, GoPro Procuedures</a>"
    message += " you will need move to the below files into an appropriate folder.<br> Generally <a href='\\hawkeye\XternalData'>\\hawkeye\XternalData</a><br>"
    message += 'If you are moving CCTV, Bill would like to remind you that you should copy the viewing program as well just in case. <br><br>'
    #message = f"Please see x and file or delete this files as you see fit.\n {illegalFiles}, once these are you removed I will forgive you"
    for badFile in illegalFiles:
        #message = messageTemplate.substitute(badFiles=badFile.title()+'\r\n').join(msg)
        message += f'<a href="{badFile}">{badFile}</a><br>'
    message += "<br>Thanks <br> Passive Aggresive Bot<br>"
    message += '<br><div style="font-size: 10px"> <span>Please note, I am a bot. Replying to me will not do anything, nor stop anything</span>'
    message += '<br>'
    message += '<br>--Bot Links -- <br> '
    message += '<img width="40px" src="http://bwwiki:49494/bot-angry-icon-graphic-sml.png"><br>'
    message += '<a href="http://192.168.0.118/oldManLemon/passive-aggressive-bot/issues">Report Issues</a>  ||  <a href="http://192.168.0.118/oldManLemon/passive-aggressive-bot">Source Code</a>'
    message += '</div></div>'

    # add in the message body
    msg.attach(MIMEText(message, 'html'))
    
     # send the message via the server set up earlier.
    s.send_message(msg)
    #s.sendmail(MY_ADDRESS, ['a.hase@bornhorstward.com.au'], msg.as_string)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()

    # print(contacts)
    # leader = contacts[0]
    # leaderName = leader[0] + leader[1]
    # leader 



def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# def main():
   
#     message_template = read_template('message.txt')

#     # set up the SMTP server
#     s = smtplib.SMTP(host='mail.bornhorstward.com.au', port=25)
#     s.starttls()
#     s.login(MY_USER, PASSWORD)

#     # For each contact, send the email:
#     for fnames, lnames, email in zip(fname, lname, emails):
#         msg = MIMEMultipart()       # create a message

#         # add in the actual person name to the message template
#         message = message_template.substitute(PERSON_fNAME=fnames.title())
#         message = message_template.substitute(PERSON_lNAME=lnames.title())

#         # Prints out the message body for our sake
#         print(message)

#         # setup the parameters of the message
#         msg['From']=MY_ADDRESS
#         msg['To']=email
#         msg['Subject']="This is TEST"
        
#         # add in the message body
#         msg.attach(MIMEText(message, 'plain'))
        
#         # send the message via the server set up earlier.
#         s.send_message(msg)
#         del msg
        
#     # Terminate the SMTP session and close the connection
#     s.quit()
    
# if __name__ == '__main__':
#     main()
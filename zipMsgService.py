import smtplib
import settings
from string import Template
import offendersLookup as lookup

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
MY_USER = settings.masterUser
MY_ADDRESS = 'passive-aggressive-botz@bornhorstward.com.au'
PASSWORD = settings.masterPass

def emailService(jobNumber, illegalFiles):
    #print(jobNumber)
    #print(illegalFiles)
    illegalFiles = (illegalFiles)
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
        """ Comment out below line to stop emailing everyone """
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
    msg['Subject']=jobNumber+" Contains Zip duplicates that should be cleaned"
    #messageTemplate = read_template('message.txt')
    message = "<div style='line-height: 1.5; font-family:  Calibri, sans-serif; font-size: 16px; color: rgba(0, 0, 0, 0.87);'>"
    message += "Hey  "
    for fname in firstName:
        message += fname+", "
    message += f"<br><br>You are being sent this email because you are registered as working on <b>{jobNumber}</b>.<br>"
    message += f"It appears someone has extracted the content of a zip file and left both the zip and the resulting folder behind."
    message += " Could you please ensure that one is deleted so as to avoid duplication of data. It is not critical if you wish to keep just the zip or the folder. However both is not necessary. <br>"
    message += "<br>While it may not seem important, this type of duplication is pervasive and takes up space rapidly.<br><br> "
    message += 'Please review the files and folders below: <br><br>'
    #message = f"Please see x and file or delete this files as you see fit.\n {illegalFiles}, once these are you removed I will forgive you"
    #illegalFiles = zip(illegalFiles)
    names = []
    sources = []
    #print(illegalFiles[0])
    for badFile in range(len(illegalFiles)):
        #message = messageTemplate.substitute(badFiles=badFile.title()+'\r\n').join(msg)
        #print(illegalFiles[1])
        names.append(illegalFiles[1])
        sources.append(illegalFiles[0])
        

    message += "<table><th>Link</th><th>Folder</th><th>Zip</th><tr>"
    names = names[0]
    sources = sources[0] 
    #print(sources)
    #print(names)   
    for source,name in zip(sources,names):
        #print('Source:', source, 'Name:', name)

        message += f'<td><a href="{source}">{source}</a></td><td>{name}</td><td>{name}.zip</td></tr>'
    
    message += "</table>"

    message += "<br>Luke warm regards <br> Passive Aggresive Bot<br>"
    message += '<br><div style="font-size: 10px"> <span>Please note, I am a bot. Replying to me will not do anything, nor stop anything. If you have suggestions or issues, please click report issues</span>'
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


import smtplib
import settings
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
MY_USER = settings.masterUser
MY_ADDRESS = 'passive-aggressive-bot@bornhorstward.com.au'
PASSWORD = settings.masterPass

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    firstname = []
    lastname = []
    emails = []
    # with open(filename, mode='r', encoding='utf-8') as contacts_file:
    #     for a_contact in contacts_file:
    #         fname.append(a_contact.split(',')[0])
    #         lname.append(a_contact.split(',')[1])
    #         emails.append(a_contact.split(',')[2])
    return firstname,lastname, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    fname, lname, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='mail.bornhorstward.com.au', port=25)
    s.starttls()
    s.login(MY_USER, PASSWORD)

    # For each contact, send the email:
    for fnames, lnames, email in zip(fname, lname, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_fNAME=fnames.title())
        message = message_template.substitute(PERSON_lNAME=lnames.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()
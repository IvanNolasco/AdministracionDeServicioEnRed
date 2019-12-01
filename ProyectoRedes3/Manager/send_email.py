"""
@author: navi_
"""

# import necessary packages
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# function to read the contacts from a given contact file and return a
# list of names and email addresses
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

# function to read the message as a template
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content) 

# function to send an email alerting of a problem in the network
def send_email(router_id, type_problem):
    problems = {'1':'El porcentaje de uso del CPU',
                '2':'El porcentaje de uso de la memoria RAM',
                '3':'El nivel de temperatura',
                '4':'La capacidad del disco duro'}
    names, emails = get_contacts('adminsmail.txt')
    message_template = read_template('message.txt')
    my_email = 'sistema.de.monitoreo.redes3@gmail.com'
    password = 'redescom123'
    
    # set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(my_email, password)
    
    # for each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message
        
        # change the template with the actual admin name, touter id and the problem description
        message = message_template.substitute(ADMIN_NAME=name.title(), 
                                              ROUTER_ID=router_id, 
                                              PROBLEM_DESCRIPTION=problems[type_problem])
    
        # setup the parameters of the message
        msg['From'] = my_email
        msg['To'] = email
        msg['Subject'] = 'ALERTA del Sistema de Monitoreo de Red'
    
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
    
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        
    print('Se ha enviado un correo de ALERTA a todos los administradores de la red para informar del problema')
    
    # finish the SMTP session and close the connection
    server.quit()

if __name__ == '__main__':
    send_email('R4', '2')
    send_email('R1', '4')
    send_email('R5', '1')
    send_email('R3', '3')
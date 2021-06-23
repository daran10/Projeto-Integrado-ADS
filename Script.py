import pyautogui
import time
import smtplib
import os
import xml.etree.ElementTree as ET
import html2text
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from jinja2 import Environment, BaseLoader
import json
import logging

cred = json.load(open('docs/config.json','rb'))


# Enviar e-mails
def enviar_email(arquivo):
    Sender = "test@outlook.com.br"
    Receiver = cred["e-mail"]
    msg = MIMEMultipart()

    msg['From'] = Sender
    msg['To'] = Receiver
    msg['Subject'] = "Erro ICMS IPI"

    html, text = criar_HTML(arquivo)


    #body = MIMEText("Mensagem de Erro")
    #part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    #msg.attach(part1)
    msg.attach(part2)

    #msg.attach(body)
    arquivo_formato = arquivo + ".pdf"
    path = os.path.join(os.environ['USERPROFILE'], "Documents")

    filename = path+'\\'+arquivo_formato

    attachment = open(filename,'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    attachment.close()

#    server = smtplib.SMTP("smtp.gmail.com",587)
    server = smtplib.SMTP("smtp.office365.com",587)
    server.starttls()
    password = "projetoRPA"
    server.login(Sender, password)
    text = msg.as_string()
    server.sendmail(Sender, Receiver, text)
    server.quit()
    #print('\nEmail enviado com sucesso!')



# Enviar e-mails
'''
def enviar_email():
    Sender = "andre.m.tolentino.rpa@gmail.com"
    Receiver = "andre.tolentino@engdb.com.br"
    msg = MIMEMultipart()

    msg['From'] = Sender
    msg['To'] = Receiver
    msg['Subject'] = "Erro ICMS IPI"

    body = "Mensagem de Erro"

    msg.attach(MIMEText(body))

    arquivo = "Erro_EFD_ICMS_2020-08-21.jrpxml"
    path = os.path.join(os.environ['USERPROFILE'], "Documents")

    filename = path+'\\'+arquivo

    attachment = open(filename,'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    attachment.close()

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    password = "projetoRPA"
    server.login(Sender, password)
    text = msg.as_string()
    server.sendmail(Sender, Receiver, text)
    server.quit()
    print('\nEmail enviado com sucesso!')
'''

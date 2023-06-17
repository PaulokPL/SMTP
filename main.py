import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import imaplib
import email
import os
import PySide2
import os.path
import socket
import pytz
from datetime import datetime, timedelta, timezone
import time
import threading
import sys
from PySide2.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QHBoxLayout
from PySide2.QtWidgets import QWidget, QLineEdit, QListWidget
from PySide2.QtWidgets import QPushButton, QLabel, QMainWindow, QCheckBox, QMessageBox
from email.utils import parsedate_to_datetime
import imaplib
import email
# import nltk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from selenium.webdriver.support.ui import Select
from sematch.semantic.similarity import WordNetSimilarity


# Dane do logowania
SMTP_SERVER = 'smtp.poczta.onet.pl'
SMTP_PORT = 587
SMTP_USERNAME = ''
SMTP_PASSWORD = ''

IMAP_SERVER = 'imap.poczta.onet.pl'
IMAP_PORT = 993
IMAP_USERNAME = ''
IMAP_PASSWORD = ''

# Odczyt maili

nicknames = []

def user():
    if(fieldEdit.text() != "" and fieldEdit1.text() != ""):
        nicknames.append(fieldEdit.text())
        nicknames.append(fieldEdit1.text())
        app.exit()
        app.quit()


class Accou(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create new account")
        self.setGeometry(300, 300, 800, 800)
        self.fir_namae = QLabel('First name:', self)
        self.fir_namae.move(10, 25)
        self.las_name = QLabel('Last name:', self)
        self.las_name.move(10, 65)
        self.fir_namae1 = QLabel('Password:', self)
        self.fir_namae1.move(10, 105)
        self.las_name1 = QLabel('Username:', self)
        self.las_name1.move(10, 145)
        self.fir_namae2 = QLabel('Birthdate - day:', self)
        self.fir_namae2.move(10, 185)
        self.las_name3 = QLabel('Birthdate - month:', self)
        self.las_name3.move(10, 225)
        self.las_name4 = QLabel('Birthdate - year:', self)
        self.las_name4.move(10, 265)
        self.las_name4 = QLabel('Recovery Mail:', self)
        self.las_name4.move(10, 305)

        self.fieldEdit = QLineEdit(self)
        self.fieldEdit.move(100, 20)
        self.fieldEdit.resize(200, 25)
        self.fieldEdit1 = QLineEdit(self)
        self.fieldEdit1.move(100, 60)
        self.fieldEdit1.resize(200, 25)

        self.fieldEdit2 = QLineEdit(self)
        self.fieldEdit2.move(100, 100)
        self.fieldEdit2.resize(200, 25)
        self.fieldEdit2.setEchoMode(QLineEdit.Password)
        self.fieldEdit3 = QLineEdit(self)
        self.fieldEdit3.move(100, 140)
        self.fieldEdit3.resize(200, 25)
        self.fieldEdit4 = QLineEdit(self)
        self.fieldEdit4.move(100, 180)
        self.fieldEdit4.resize(200, 25)
        self.fieldEdit5 = QLineEdit(self)
        self.fieldEdit5.move(100, 220)
        self.fieldEdit5.resize(200, 25)
        self.fieldEdit6 = QLineEdit(self)
        self.fieldEdit6.move(100, 260)
        self.fieldEdit6.resize(200, 25)
        self.fieldEdit7 = QLineEdit(self)
        self.fieldEdit7.move(100, 300)
        self.fieldEdit7.resize(200, 25)

        self.button_send = QPushButton("Create", self)
        self.button_send.setGeometry(300, 150, 70, 30)
        self.button_send.clicked.connect(self.create1)

    def create1(self):
        driver = webdriver.Chrome(executable_path="C:/Users/pawel/Downloads/chromedriver_win32/chromedriver.exe")
        driver.get("https://konto.onet.pl/register?state=https%3A%2F%2Fpoczta.onet.pl%2F&client_id=poczta.onet.pl.front.onetapi.pl")
        time.sleep(5)
        button = driver.find_element_by_xpath("//button[@aria-label='accept and close']")
        button.click()


        input_field = driver.find_element_by_name("alias")
        input_field.send_keys(self.fieldEdit3.text())
        time.sleep(5)
        button = driver.find_element_by_xpath("//button[@type='submit']")
        button.click()
        time.sleep(5)

        input_field = driver.find_element_by_name("newPassword")
        input_field.send_keys(self.fieldEdit2.text())
        input_field = driver.find_element_by_name("rePassword")
        input_field.send_keys(self.fieldEdit2.text())
        time.sleep(5)
        button = driver.find_element_by_xpath("//button[@type='submit']")
        button.click()
        time.sleep(5)
        input_field = driver.find_element_by_id("recoveryEmail")
        input_field.send_keys(self.fieldEdit7.text())
        time.sleep(5)
        button = driver.find_element_by_xpath("//button[@type='submit']")
        button.click()
        time.sleep(5)
        button = driver.find_element_by_xpath("//span[@class='sc-397b8c06-1 fHIJBP']")
        button.click()
        input_field = driver.find_element_by_name("name")
        input_field.send_keys(self.fieldEdit1.text() + " " + self.fieldEdit.text())
        input_field = driver.find_element_by_iname("birthDate.day")
        input_field.send_keys(self.fieldEdit4.text())
        select = Select(driver.find_element_by_name("birthDate.month"))
        select.select_by_value(self.fieldEdit5.text())
        input_field = driver.find_element_by_id("birthDate.year")
        input_field.send_keys(self.fieldEdit6.text())
        time.sleep(5)
        button = driver.find_element_by_xpath("//button[@type='submit']")
        button.click()
        time.sleep(5)
        button = driver.find_element_by_xpath("//button[@type='button']")
        button.click()
        time.sleep(5)
        button = driver.find_element_by_xpath("//button[@type='submit']")
        button.click()
        time.sleep(5)
        time.sleep(35)
        driver.quit()


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, user, passwo):
        super().__init__()
        self.username = user
        self.password = passwo
        self.setWindowTitle("Write email")
        self.setGeometry(300, 300, 400, 300)
        self.recipient_label = QLabel('Recipient:', self)
        self.recipient_label.move(20, 23)
        self.recipient_edit = QLineEdit(self)
        self.recipient_edit.setGeometry(80, 20, 200, 20)
        self.topic_label = QLabel('Subject:', self)
        self.topic_label.move(20, 63)
        self.topic_edit = QLineEdit(self)
        self.topic_edit.setGeometry(80, 60, 200, 20)
        self.body_label = QLabel('Body:', self)
        self.body_label.move(20, 103)
        self.body_edit = QLineEdit(self)
        self.body_edit.setGeometry(80, 100, 200, 150)
        self.button_send = QPushButton("Send email", self)
        self.button_send.setGeometry(300, 150, 70, 30)
        self.button_send.clicked.connect(self.sendmail)

    def sendmail(self):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = self.recipient_edit.text()
        msg['Subject'] = self.topic_edit.text()

        # Dodanie treści wiadomości
        msg.attach(MIMEText(self.body_edit.text(), 'plain'))

        # Wysłanie wiadomości
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.username, self.recipient_edit.text(), msg.as_string())
        server.quit()




class MainWindow(QMainWindow):
    def __init__(self, user, passw):
        super().__init__()
        self.username = user
        self.password = passw
        self.setGeometry(100, 100, 800, 500)
        self.button = QPushButton("Write mail", self)
        self.button.setGeometry(200, 0, 100, 30)
        self.button.clicked.connect(self.show_new_window)
        self.button2 = QPushButton("Refresh", self)
        self.button2.setGeometry(50, 0, 100, 30)
        self.button2.clicked.connect(self.read_emails)
        self.mail_list = QListWidget(self)
        self.mail_list.setGeometry(10, 50, 280, 450)
        self.mail_list.itemClicked.connect(self.show_mail_content)
        self.mail_content = QTextEdit(self)
        self.mail_content.setGeometry(300, 50, 280, 450)
        self.mail_content.setReadOnly(True)
        # self.inbox = QTextEdit(self)
        # self.inbox.setReadOnly(True)
        # self.inbox.setGeometry(10, 40, 550, 380)
        self.button3 = QPushButton("Start autoresponding", self)
        self.button3.setGeometry(350, 0, 150, 30)
        # self.button3.clicked.connect(self.autoresponder)
        self.setWindowTitle("Email")
        self.is_running = False
        self.button3.clicked.connect(self.start_autoresponder)
        self.message_box = QMessageBox(self)
        self.message_box.setText("Autoresponder is running.")
        self.message_box.setStandardButtons(QMessageBox.Ok)
        self.label1 = QLabel("Search mails", self)
        self.label1.setGeometry(600, 100, 80, 10)
        self.keywor = QLineEdit(self)
        self.keywor.setGeometry(600, 120, 130, 20)
        self.button4 = QPushButton("Search", self)
        self.button4.setGeometry(600, 150, 80, 30)
        self.button4.clicked.connect(self.filter_emails)
        self.button5 = QPushButton("Create new account", self)
        self.button5.setGeometry(600, 200, 150, 30)
        self.button5.clicked.connect(self.account)

        self.mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        self.mail.login(self.username, self.password)
        self.mail.select('inbox')
        _, self.mail_ids = self.mail.search(None, 'ALL')
        for mail_id in self.mail_ids[0].split():
            _, mail_data = self.mail.fetch(mail_id, '(RFC822)')
            mail_message = email.message_from_bytes(mail_data[0][1])
            mail_subject = mail_message['Subject']
            mail_sender = mail_message['From']
            mail_item = f"{mail_sender}: {mail_subject}"
            self.mail_list.addItem(mail_item)

    def account(self, checked):
        self.q = Accou()
        self.q.show()

    def filter_emails(self):
        # Zdefiniowanie słowa kluczowegoe
        self.mail_list.clear()
        keyword = self.keywor.text()
        keyword = keyword.lower()
        # pobranie listy stop words z biblioteki nltk
        stop_words = set(stopwords.words('english'))

        # wyszukanie i pobranie wiadomości
        _, data = self.mail.search(None, 'ALL')
        mail_ids = data[0].split()
        messages = []

        for mail_id in mail_ids:
            # pobranie nagłówka wiadomości
            _, data = self.mail.fetch(mail_id, '(BODY[HEADER.FIELDS (FROM SUBJECT DATE)])')
            msg = email.message_from_bytes(data[0][1])
            subject = msg['Subject']
            sender = msg['From']
            date = msg['Date']

            # pobranie treści wiadomości
            _, data = self.mail.fetch(mail_id, '(BODY[TEXT])')
            body = data[0][1].decode()

            # tokenizacja treści wiadomości
            word_tokens = word_tokenize(body)

            # usunięcie stop words z listy tokenów
            filtered_tokens = [word.lower() for word in word_tokens if word.lower() not in stop_words]

            # wyszukanie słowa kluczowego w liście tokenów
            if keyword.lower() in filtered_tokens:
                # dodanie krotki z danymi do listy wiadomości, jeśli słowo kluczowe zostało znalezione
                messages.append((subject, sender, date, body))
                self.mail_list.addItem(sender + ":  " + subject)




    def show_mail_content(self):
        # pobranie zawartości wybranego maila
        current_row = self.mail_list.currentRow()
        _, mail_data = self.mail.fetch(self.mail_ids[0].split()[current_row], '(RFC822)')
        mail_message = email.message_from_bytes(mail_data[0][1])
        mail_body = ""
        if mail_message.is_multipart():
            for part in mail_message.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                if "attachment" not in content_disposition:
                    if "text/plain" in content_type:
                        mail_body = part.get_payload(decode=True).decode()
        else:
            mail_body = mail_message.get_payload(decode=True).decode()

        # wyświetlenie zawartości maila w QTextEdit
        self.mail_content.setText(mail_body)

    # def autoresponder(self):
    #     self.a = Autorespon(self.username, self.password, )
    #     self.a.show()


    def start_autoresponder(self):

        self.is_running = not self.is_running
        if self.is_running:
            self.dateti = datetime.now(pytz.utc)
            self.button3.setText("Stop Autoresponder")
            self.message_box.show()
            thread = threading.Thread(target=self.run_autoresponder)
            thread.start()
        else:
            self.button3.setText("Start Autoresponder")
            self.message_box.hide()

    def run_autoresponder(self):
        while self.is_running:
            mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
            mail.login(self.username, self.password)
            mail.select('inbox')
            status, response = mail.search(None, 'UNSEEN')
            if status == 'OK':
                for msg_id in response[0].split():
                    _, data = mail.fetch(msg_id, '(RFC822)')
                    _, b = data[0]
                    msg = email.message_from_bytes(b)
                    msg_date = datetime.strptime(msg['date'], '%a, %d %b %Y %H:%M:%S %z')
                    # date = datetime.strptime('2018-11-10 10:55:31', '%Y-%m-%d %H:%M:%S')
                    if(msg_date > self.dateti):
                        if msg['from'] and msg['from'].lower() != self.username.lower():
                            subject = 'Re: {}'.format(msg['subject'])
                            to = msg['reply-to'] if msg['reply-to'] else msg['from']
                            text = 'Thank you for your email. I am currently not available but I will respond as soon as possible.'
                            self.send_email(to, subject, text)
                            mail.store(msg_id, '+FLAGS', '\Seen')
            mail.close()
            mail.logout()
            time.sleep(5)

    def send_email(self, to, subject, text):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text))
        smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtp.starttls()
        smtp.login(self.username, self.password)
        smtp.sendmail(self.username, to, msg.as_string())
        smtp.quit()

    def show_new_window(self, checked):
        self.w = AnotherWindow(self.username, self.password)
        self.w.show()

    def read_emails(self):
        self.mail_list.clear()
        self.mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        self.mail.login(self.username, self.password)
        self.mail.select('inbox')
        _, self.mail_ids = self.mail.search(None, 'ALL')
        for mail_id in self.mail_ids[0].split():
            _, mail_data = self.mail.fetch(mail_id, '(RFC822)')
            mail_message = email.message_from_bytes(mail_data[0][1])
            mail_subject = mail_message['Subject']
            mail_sender = mail_message['From']
            mail_item = f"{mail_sender}: {mail_subject}"
            self.mail_list.addItem(mail_item)



def read_emails():
    # Tworzenie nowego katalogu na pliki z załącznikami
    # nawiązanie połączenia z serwerem IMAP
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(IMAP_USERNAME, IMAP_PASSWORD)
    mail.select('inbox')

    # pobranie nieprzeczytanych maili
    _, search_data = mail.search(None, 'ALL')

    # lista maili
    # emails = []
    # num = search_data[0].split()
    # print(len(num))
    # iteracja po nieprzeczytanych mailach
    for message_id in search_data[0].split():
        # fetch the email message by its id
        _, message_data = mail.fetch(message_id, '(RFC822)')

        # parse the message data into an email object
        message = email.message_from_bytes(message_data[0][1])

        # print the email details
        print('From:', message['From'])
        print('To:', message['To'])
        print('Subject:', message['Subject'])
        print('Date:', message['Date'])
        # print('Body:', message.get_payload())

    # zamknięcie połączenia z serwerem IMAP
    mail.close()
    mail.logout()
    # print(emails)
    # return emails




if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QWidget()
    nickname_label = QLabel('Username:', widget)
    nickname_label.move(10, 25)
    password_label = QLabel('Password:', widget)
    password_label.move(10, 65)

    fieldEdit = QLineEdit(widget)
    fieldEdit.move(70, 20)
    fieldEdit.resize(200, 25)
    fieldEdit1 = QLineEdit(widget)
    fieldEdit1.move(70, 60)
    fieldEdit1.resize(200, 25)
    fieldEdit1.setEchoMode(QLineEdit.Password)
    pybutton = QPushButton('Accept', widget)
    pybutton.resize(200, 32)
    pybutton.move(70, 100)
    pybutton.clicked.connect(user)
    widget.setGeometry(100, 100, 300, 150)
    widget.setWindowTitle("Type your username and password")
    widget.show()
    app.exec_()
    widget.hide()
    app1 = QApplication.instance()
    if (app1 is None):
        app1 = QApplication(sys.argv)
    # window = ChatWindow(nicknames[0], host, port)
    # app = QApplication(sys.argv)
    w = MainWindow(nicknames[0], nicknames[1])
    w.show()
    app.exec_()
    # read_emails()


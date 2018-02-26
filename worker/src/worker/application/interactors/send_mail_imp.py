import smtplib

from worker.application.conf.config import SERVER_MAIL, SERVER_FROM_USER, SERVER_FROM_PASSWORD
from worker.domain.repositories.user_repository import UserRepository
from worker.domain.interactors.send_mail import SendMail


class SendMailImp(SendMail):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def send(self, to, message, subject):
        server = smtplib.SMTP(SERVER_MAIL, 587)
        server.ehlo()
        server.starttls()
        server.login(SERVER_FROM_USER, SERVER_FROM_PASSWORD)
        server.sendmail(SERVER_FROM_USER, to, message)
        server.close()

    def send_to_topic(self, topic, message, subject):
        users = list(self.user_repository.get_users_by_topic(topic))
        for user in users:
            self.send(user.email, message, subject)

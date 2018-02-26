class SendMail:
    def send(self, to, message, subject):
        raise NotImplementedError()

    def send_to_topic(self, topic, message, subject):
        raise NotImplementedError()

import logging
import requests


class Mailer:
    def __init__(self, api_key):
        self.api_key = api_key

    def send(self, sender, recipient, subject, body, attachment):
        logging.debug(
            f"{sender}, {recipient}, {subject}, {body}, {attachment}")

        url = f"https://api.eu.mailgun.net/v3/{site}/messages"
        auth = ("api", self.api_key)
        data = {"from": sender,
                "to": [recipient],
                "subject": subject,
                "text": body}

        logging.debug(f"url: {url}, body: {body}")

        if attachment != None:
            requests.post(
                url,
                auth=auth,
                files=[("attachment", (attachment.get(
                    "filename"), attachment.get("content")))],
                data=data)
        else:
            requests.post(
                url,
                auth=auth,
                data=data)

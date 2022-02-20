class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = list()
info = input()
while info != "Stop":
    sender, receiver, content = info.split()
    temp_mail = Email(sender, receiver, content)
    emails.append(temp_mail)

    info = input()

index = input().split(", ")

for x in index:
    emails[int(x)].send()

for mail in emails:
    print(mail.get_info())

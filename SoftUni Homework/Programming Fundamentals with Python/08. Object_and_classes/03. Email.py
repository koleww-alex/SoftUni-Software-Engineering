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


command = input()

emails = []

while command != "Stop":
    list_of_people = command.split()
    sender = list_of_people[0]
    receiver = list_of_people[1]
    content = list_of_people[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

indices = list(map(int, input().split(", ")))


for x in indices:
    emails[x].send()

for email in emails:
    print(email.get_info())

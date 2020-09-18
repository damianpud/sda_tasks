import smtplib
import json
import pickle
from io import UnsupportedOperation
file_name = "pickle_users_list"

email_address = 'address'
email_password = 'password'


class User:
    def __init__(self, user_nick: str, first_name: str, last_name: str, email: str, active: bool):
        self.user_nick = user_nick
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.active = active

    def __repr__(self):
        return f'{self.user_nick} {self.first_name} {self.last_name} {self.email} {self.active}'


class NewsletterSystem:
    def __init__(self):
        self.user_list = list()
        self.user_nick_list = list()

    def add_user(self, user_nick, user_first_name, user_last_name, user_email, user_active):
        self.user_list.append(User(user_nick, user_first_name, user_last_name, user_email, user_active))
        self.user_nick_list.append(user_nick)

    def remove_user(self, user_nick):
        del self.user_list[self.user_nick_list.index(user_nick)]
        self.user_nick_list.remove(user_nick)

    def send_email(self):
        if len(self.user_list) > 0:
            subject = input("Enter subject: ")
            body = input("Enter body message: ")
            msg = f"Subject: {subject}\n\n{body}"
            for el in self.user_list:
                if el.active:
                    try:
                        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                            smtp.ehlo()
                            smtp.starttls()
                            smtp.ehlo()
                            smtp.login(email_address, email_password)
                            smtp.sendmail(email_address, el.email, msg)
                        print(f"Message was send successfully to {el.email}")
                    except smtplib.SMTPAuthenticationError:
                        print(f"You don't have an access to account.\n")
                else:
                    print(f"User {el.first_name} {el.last_name} is inactive, email wasn't sent successfully.")
        elif len(newsletter.user_list) == 0:
            print("Users list is empty. You can't send newsletter.\n")

    def show_users_list(self):
        for el in self.user_list:
            print(f'Nick: {el.user_nick}\nName: {el.first_name}\nSurname: {el.last_name}\n'
                  f'email: {el.email}\nStatus active: {el.active}\n')

    def read(self):
        try:
            with open(file_name, 'rb') as handler:
                self.user_list = pickle.load(handler)
        except FileNotFoundError:
            with open(file_name, 'xb'):
                return list()
        except UnsupportedOperation:
            return list()

    def save(self):
        with open(file_name, 'wb') as handler:
            pickle.dump(self.user_list, handler)


""" 
    # json read method
    def read(self):
        try:
            f = open("users_list.txt", "r")
            data = f.read()
            object_data = json.loads(data)
            for el in object_data:
                user_nick = el['Nick'][0]
                user_first_name = el['Name'][0]
                user_last_name = el['Surname'][0]
                user_email = el['email'][0]
                user_active = el['Status active']
                self.add_user(user_nick, user_first_name, user_last_name, user_email, user_active)
            f.close()
        except FileNotFoundError:
            f = open("users_list.txt", "x")
            f.close()
            return list()
        except json.decoder.JSONDecodeError:
            return list()

    # json save method
    def save(self):
        data_list = list()
        for el in self.user_list:
            object_data = dict()
            object_data['Nick'] = el.user_nick,
            object_data['Name'] = el.first_name,
            object_data['Surname'] = el.last_name,
            object_data['email'] = el.email,
            object_data['Status active'] = el.active
            data_list.append(object_data)
        f = open("users_list.txt", "w")
        f.write(json.dumps(data_list))
        f.close()
"""


if __name__ == '__main__':
    newsletter = NewsletterSystem()
    newsletter.read()
    newsletter.show_users_list()


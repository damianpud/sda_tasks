from newsletter_task.objects_app import NewsletterSystem
import re
menu = ("Show users", "Add user", "Delete user", "Send message", "Quit")


def show_menu_list():
    for index in range(len(menu)):
        print(f"{index}. {menu[index]}")


def chose_from_menu():
    while True:
        try:
            chose = int(input("Chose from menu: "))
            if chose in range(len(menu)):
                return chose
            else:
                print("Index out of range.\n")
                show_menu_list()
        except ValueError:
            print('Wrong value, try again.\n')


def run():
    start = True
    newsletter = NewsletterSystem()
    newsletter.read()
    while start:
        show_menu_list()
        chose = chose_from_menu()
        if chose == 0:
            if len(newsletter.user_list) == 0:
                print("Users list is empty.\n")
            else:
                newsletter.show_users_list()
        elif chose == 1:
            user_nick = input("Enter the user nick: ")
            user_first_name = input("Enter the user first name: ")
            user_last_name = input("Enter the user last name: ")
            user_email = input("Enter the email: ")
            user_active = True
            if re.fullmatch('\w+\.*\w*\@\w+\.[a-z]{2,3}', user_email, re.A):
                newsletter.add_user(user_nick, user_first_name, user_last_name, user_email, user_active)
                print(f"User {user_nick} was added")
            else:
                print('Wrong email sequence')
        elif chose == 2:
            user_nick = input("Enter the user nick: ")
            delete_chose = input(f"Are you sure, you want to delete user {user_nick} ? [y/n]: ")
            if delete_chose == 'y':
                try:
                    newsletter.remove_user(user_nick)
                    print(f"User {user_nick} was deleted.\n")
                except ValueError:
                    print(f"{user_nick} is not in users list")
            elif delete_chose == 'n':
                print(f"User {user_nick} wasn't deleted.\n")
        elif chose == 3:
            newsletter.send_email()
        elif chose == 4:
            newsletter.save()
            start = False


if __name__ == '__main__':
    run()

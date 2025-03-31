from homework_02.model import Contact, Directory


def display_menu(directory: Directory) -> None:
    print(str(directory))


def get_menu_choice():
    choice = input("Выберите интересующий пункт меню: ")
    return choice


def display_contacts(contacts: list) -> None:
    print("Просмотр контактов:")
    for contact in contacts:
        print(contact)
    print()


def get_contact_input():
    new_name = input('Введите имя: ')
    new_number = input('Введите номер: ')
    new_comment = input('Введите комментарий: ')
    return check_contact_input(new_name, new_number, new_comment)


def check_contact_input(name, number, comment):
    if len(name) < 1 or len(number) < 1 or len(comment) < 1:
        print("Новый контакт не создан. Неверно введены данные\n")
        return None
    return [name, number, comment]


def display_message(message: str) -> None:
    print(message)

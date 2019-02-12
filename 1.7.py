def pol_calc():
    operation = input("Введите 'польскую' операцию:")
    hide = operation.split()
    output = 0

    assert hide[0] == '+' or hide[0] == '-' or hide[0] == '*' or hide[0] == '/', 'Допустимые операнды +,-,*,/.'
    assert len(hide) <= 3, 'Максимум 2 числа.'

    if hide[0] == '+':
        output = int(hide[1]) + int(hide[2])
        print(output)
    elif hide[0] == '-':
        output = int(hide[1]) - int(hide[2])
        print(output)
    elif hide[0] == '*':
        output = int(hide[1]) * int(hide[2])
        print(output)
    elif hide[0] == '/':
        try:
            output = int(hide[1]) / int(hide[2])
        except ZeroDivisionError:
            print("Делить на ноль нельзя")
        else:
            print(output)


pol_calc()


# ######## "Tasks#3"
#
# documents = [
#     {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#     {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#     {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
#     {"type": "insurance", "number": "101006"}
# ]
#
# directories = {
#         '1': ['2207 876234', '11-2'],
#         '2': ['10006'],
#         '3': []
#       }
#
#
# def document_number_check(number):
#     for doc_regester in documents:
#         if doc_regester['number'] == number:
#             print(doc_regester['name'])
#
#
# def prnt():
#     for docs in documents:
#         print(docs['type'], docs['number'], docs['name'])
#
#
# def shelf_chek(number):
#     for shelfs in directories.items():
#         for doc_number in shelfs[1]:
#             if doc_number == number:
#                 for shelf in shelfs[0]:
#                     print(shelf)
#
#
# def add_doc():
#     type = input('Введите тип документа:')
#     number = input('Введите номер документа:')
#     name = input('Введите имя владельца:')
#     documents.append({"type": type, "number": number, "name": name})
#     directories.setdefault(input('Введите номер полки:'), []).append(number)
#     return directories, documents
#
#
# def ls_names():
#     try:
#         for doc_regester in documents:
#             print(doc_regester['name'])
#     except KeyError:
#         print('Имя владельца не указано. Добавьте имя в базу.')
#
#
# command = input('Введите команду:')
#
# if command == 'p':
#     document_number_check(input('Введите номер документа:'))
# elif command == 'l':
#     prnt()
# elif command == 's':
#     shelf_chek(input('Введите номер документа:'))
# elif command == 'a':
#     add_doc()
#     print(directories)
#     print(documents)
# elif command == 'ls':
#     ls_names()
# else:
#     print('Доступные комманды: p, l, s, a, ls.')

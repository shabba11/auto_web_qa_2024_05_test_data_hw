import json
from files import JSON_FILE_PATH, CSV_FILE_PATH
from csv import DictReader

with open(JSON_FILE_PATH, "r") as user:
    users = json.load(user)

with open(CSV_FILE_PATH, newline='') as book:
    reader = DictReader(book)
    books_list = [row for row in reader]

num_of_books = len(books_list) // len(users)


def generate_result_data(book_list, users_list):
    """Генерация пользователей с книгами разделенных максимально поровну

    :param book_list: список книг
    :param users_list: список пользователей
    :return: отфильтрованный список пользователей с книгами
    """
    data = []

    for usr in users_list:
        data.append({
            'name': usr['name'],
            'gender': usr['gender'],
            'address': usr['address'],
            'age': usr['age'],
            'books': []
        })

    num_user = 0
    for b in book_list:
        data[num_user]['books'].append({
                "title": b["Title"],
                "author": b["Author"],
                "pages": b["Pages"],
                "genre": b["Genre"]
            })
        num_user += 1
        if len(data) == num_user:
            num_user = 0

    return data


result_data = generate_result_data(book_list=books_list, users_list=users)

with open("result.json", "a") as result:
    json.dump(result_data, result, indent=2)

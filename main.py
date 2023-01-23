from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import emoji

if __name__ == '__main__':
    print(datetime.datetime.now(calculate_salary()))
    print(datetime.datetime.now(get_employees()))

    print(emoji.emojize('well done :thumbs_up:'))
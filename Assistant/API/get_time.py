from datetime import datetime


def get_time_now():
    return datetime.now().time()


def get_date_now():
    return datetime.now().date()

print(get_date_now())
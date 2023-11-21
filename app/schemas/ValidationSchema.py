import re


def is_date(value):
    return re.match(r"(\d{4}-\d{2}-\d{2})|(\d{2}\.\d{2}\.\d{4})", value)


def is_phone(value):
    return re.match(r"\+7 \d{3} \d{3} \d{2} \d{2}", value)


def is_email(value):
    return re.match(r"[^@]+@[^@]+\.[^@]+", value)


# Функция для определения типа поля
def field_validation(value):
    if is_date(value):
        return 'date'
    elif is_phone(value):
        return 'phone'
    elif is_email(value):
        return 'email'
    else:
        return 'text'

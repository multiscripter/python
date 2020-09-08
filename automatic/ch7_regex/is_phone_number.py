import re


def is_phone_number(text):
    if len(text) is not 12:
        return False
    a = 0
    for char in text:
        if a in [3, 7] and char is not '-':
            return False
        elif a not in [3, 7] and not char.isdecimal():
            return False
        a += 1
    return True


def is_phone_number_by_regex(tpl, text):
    regex = re.compile(tpl)
    return regex.search(text)

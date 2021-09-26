from datetime import datetime


def norm_man(weight, height, birthdate):
    now = datetime.now()
    return int(66.5 + 13.75 * weight + 5.003 * height - 6.755 * (
                now.year - birthdate.year - (1 if now.month < birthdate.month else 0)))


def norm_woman(weight, height, birthdate):
    now = datetime.now()
    return int(55.1 + 9.563 * weight + 1.85 * height - 4.676 * (
                    now.year - birthdate.year - (1 if now.month < birthdate.month else 0)))

from datetime import datetime


def current_date():
    return datetime.now().strftime("%d-%m-%Y")


def current_time():
    return datetime.now().strftime("%H:%M:%S")


def calculate_duration(entry, exit):

    fmt = "%H:%M:%S"

    start = datetime.strptime(entry, fmt)
    end = datetime.strptime(exit, fmt)

    duration = end - start

    return str(duration)
import csv


def read_details(url):
    names = []
    emails = []
    with open(url) as csvfile:
        file_reader = csv.reader(csvfile)
        for record in file_reader:
            if len(record) != 0:
                names.append(record[0].replace(' ', ''))
                emails.append(record[1].replace(' ', ''))
    return names, emails


def read_sender(url):
    with open(url, 'r') as file:
        return file.readline().replace(' ', ''), file.readline().replace(' ', '')


def read_message(url):
    with open(url, 'r') as file:
        return file.read().strip(' ')

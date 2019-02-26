import csv


def read_data_from_csv(file_name):

    rows = []
    try:
        with open(file_name, 'r') as data_file:
            reader = csv.reader(data_file)
            next(reader)
            for row in reader:
                rows.append(row)
        return rows
    except FileNotFoundError as e:
        print(e)
        return rows

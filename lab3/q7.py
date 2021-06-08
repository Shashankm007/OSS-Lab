# Generalize the previous implementation of csv parser to support any delimiter.

import csv
def parse_csv(filename, delimiter):
    with open(filename,'r')as f:
        data = csv.reader(f, delimiter=delimiter)
        for row in data:
            print(row)
parse_csv('data.csv', ',')
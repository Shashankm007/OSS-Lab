# Write a python function ‘parse_csv’ to parse csv (comma separated values) files.

import csv
def parse_csv(filename):
    with open(filename,'r')as f:
        data = csv.reader(f)
        for row in data:
            print(row)
parse_csv('data.csv')
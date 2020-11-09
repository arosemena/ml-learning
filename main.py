#!/usr/local/bin/python3

from regression.linear import cost
import csv

#
with open('test_data/fish_stats.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(', '.join(row))

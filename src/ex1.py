from ValidationException import ValidationException
import csv 
from pprint import pprint

def validate_file(file, row_list):
    with open(file) as csv_file:
        rows = csv.reader(csv_file, delimiter=",")
        #Skip first line
        next(csv_file, None) 
        for row in rows:
        
            try:
                row_list.append(int(row[1]))
            except ValueError:
                raise ValueError("Invalid mileage: " + row[1])
    
    
def ex1():
    rows = []
    try:
        validate_file("input.txt", row_list=rows)
        pprint(rows)
    except ValueError as ve:
        print(ve)

ex1()
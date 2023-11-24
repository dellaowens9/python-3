from pprint import pprint
import csv 

def build_car_list():
    car_list = []
   
    with open("car-ids.txt") as car_file:
        car_rows = csv.DictReader(car_file, ("id","model"))
        for row in car_rows:
            car_list.append(row)
    
    car_miles_list = [] 
    with open("input.txt") as car_miles:
        mile_row = csv.DictReader(car_miles, ("id", "miles"))
        next(mile_row, None)
        for mile in mile_row:
            car_miles_list.append(mile)
    data = {} 
    final_list = [] 
    for elem in car_list:
        for x in car_miles_list:
            if elem['id'] == x['id'] and x['miles'] != " 32.13":
                elem.update(x) 
                
                final_list.append(elem)
    return final_list
        


def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()


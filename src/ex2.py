import csv 


def find_total_visits():
    total = 0
    row_list = [] 
    with open("week-1.csv") as week1:
        rows = csv.reader(week1, delimiter=",")
        for row in rows:
            for x in row:
                if x == ' 1':
                    total += 1

    with open("week-2.csv") as week2:
        week2_rows = csv.reader(week2, delimiter=",")

        for row in week2_rows:
            for x in row:
                if x == ' 1':
                    total += 1
                    
    with open("week-3.csv") as week3:
        week3_rows = csv.reader(week3, delimiter=",")

        for row in week3_rows:
            for x in row:
                if x == ' 1':
                    total += 1
        return total 


def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()
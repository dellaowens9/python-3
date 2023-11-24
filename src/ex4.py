import boto3
from botocore.exceptions import ClientError

def calculate():

    user_input_1 = int(input("Enter a number: "))
    user_input_2 = int(input("Enter a number: "))
    total = 0

    while (user_input_1 != 'q'):
        user_input_1 = int(input("Enter a number: "))
        user_input_2 = int(input("Enter a number: "))
        total = user_input_1 + user_input_2 
        with open("calculator-log.txt", "a") as calculator_file:
            calculator_file.writelines(f"{user_input_1} + {user_input_2} = {total}\n") 
        total = 0


def ex4():
    calculate()

ex4()
# -*- coding: utf-8 -*-
"""Workbook 6-7-debugging-scientific-lib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EeRz9wFfHI7nU-grwJRDN-0xzQDGSxfl
"""

#ERROR HANDLING AND DEBUGGING

#6.1. Send Bulk SMS
def get_phone_number(person):
    phone_dict = {"Jerry Seinfeld":"+1 960-454-6956",
                  "George Constanza":"+1 844-833-4965",
                  "Elaine Benes":"+1 543-920-5729",
                  "Cosmo Kramer":"+1 556-673-6702",
                  "Jim Halpert":"+1 867-767-7664",
                  "Pam Beesly":"+1 410-570-7381",
                  "Michael Scott":"+1 657-220-6601",
                  "Dwight Schrute":"+1 940-573-6702",
                  "Rachel Green":"+1 813-856-3347",
                  "Monica Geller":"+1 527-324-1403",
                  "Ross Geller":"+1 687-801-6781",
                  "Phoebe Buffay":"+1 208-702-5161",
                  "Joey Tribbiani":"+1 908-665-3975",
                  "Chandler Bing":"+1 444-970-5300"}
    return phone_dict[person]


def send_bulk_sms(cst_list):
    for person in cst_list:
        try:
            num=get_phone_number(person)
            print("Message is successfully sent to",num)
        except: 
            print("Customer is not in the phone book:",person)

# send_bulk_sms(["Pam Beesly", "George Constanza", "Elaine Benes", "Michael Scott", "Maurice Moss"])
send_bulk_sms(["Roy Trenneman", "Monica Geller", "Michael Scott", "Pam Beesly",
                   "Maurice Moss", "Jen Barber", "Ross Geller", "Joey Tribbiani",
                   "Phoebe Buffay", "Denholm Reynholm", "Jim Halpert", "Cosmo Kramer",
                   "Dwight Schrute", "Jerry Seinfeld", "George Constanza"])

def get_phone_number(person):
    customers = ["Jerry Seinfeld","George Constanza","Elaine Benes","Cosmo Kramer",
               "Jim Halpert","Pam Beesly","Michael Scott","Dwight Schrute",
               "Rachel Green", "Monica Geller", "Ross Geller", "Phoebe Buffay",
               "Joey Tribbiani", "Chandler Bing"]
    numbers = ["+1 960-454-6956", "+1 844-833-4965", "+1 543-920-5729", "+1 556-673-6702",
               "+1 867-767-7664", "+1 410-570-7381", "+1 657-220-6601", "+1 940-573-6702",
               "+1 813-856-3347", "+1 527-324-1403", "+1 687-801-6781", "+1 208-702-5161",
               "+1 908-665-3975", "+1 444-970-5300"]

    return numbers[customers.index(person)]


def send_bulk_sms(cst_list):
    for person in cst_list:
        try:
            num=get_phone_number(person)
            print("Message is successfully sent to",num)
        except: 
            print("Customer is not in the phone book:",person)

send_bulk_sms(["Pam Beesly", "George Constanza", "Elaine Benes", "Michael Scott", "Maurice Moss"])
send_bulk_sms(["Roy Trenneman", "Monica Geller", "Michael Scott", "Pam Beesly",
                   "Maurice Moss", "Jen Barber", "Ross Geller", "Joey Tribbiani",
                   "Phoebe Buffay", "Denholm Reynholm", "Jim Halpert", "Cosmo Kramer",
                   "Dwight Schrute", "Jerry Seinfeld", "George Constanza"])

#6.3. Calculate Expenses
def sum_prices(shopping_list):

    total = 0
    for (item, price) in shopping_list:
        total += price
    return round(total, 2)

def calculate_expenses(shopping_lists):
    return_list=[]
    for lis in shopping_lists:
        try:
            x=sum_prices(lis)
        
        except:x="Incomplete"
        return_list+=[x]        
    return return_list



PRT=calculate_expenses([[("chocolate", 4.25), ("jambonbutter", 4.75), ("ice cream", 3.5), ("milk", 3.25)], [("coffee", 4.75), ("olive", 2.25), ("ice cream", 2.99)]])
PRT=calculate_expenses([[("coffee", 2.5), ("milk", "dunno"), ("ice cream", 2.75)],
                        [("candy", 2.99), ("chocolate", 3.99), ("tea", 3.5), ("coffee", 2.99), ("olive", 2.99)],
                        [("tea", 3.99), ("coffee", 2.5), ("olive", 2.25), ("chocolate", 4.25), ("jambonbutter", 4.25), ("egg", 2.25)]])
PRT=calculate_expenses([[("tea", 4.99), ("olive", 3.5), ("chocolate", 4.75), ("coffee", 3.99),
                         ("milk", 2.99), ("egg", 3.99), ("jambonbutter", "not sure")],
                         [("jambonbutter", 3.5), ("egg", 3.75), ("tea", 3.99), ("coffee", 4.5), ("olive", 3.75)],
                         [("jambonbutter", 3.99), ("milk", 3.5), ("chocolate", 4.25), ("ice cream", 3.5),
                          ("cheese", 2.75), ("candy", 2.75), ("tea", 4.5), ("olive", "unknown")],
                          [("ice cream", 3.99), ("olive", 3.75), ("chocolate", 2.99), ("coffee", 4.5),
                          ("milk", 3.25), ("tea", 2.25), ("candy", 4.25), ("cheese", 4.75)],
                          [("ice cream", 3.75), ("coffee", 3.25), ("candy", "unknown"),
                          ("chocolate", 3.99), ("egg", 4.99), ("olive", 3.25), ("milk", 2.5)]])

print(PRT)
# sum_prices(lis)

# [15.75, 9.99]

#6.4. Find Zero ##KİTABIN CEVABI
def find_zero(numbers):
    index_of_zero = -1
    index_counter = -1
    try:
        for number in numbers:
            index_counter += 1
            temporary = 32/number   # Apply division to catch ZeroDivisionError exception.
    except ZeroDivisionError:       # 32 and temporary have no meaning here. They can be anything.
        index_of_zero = index_counter
    return index_of_zero

# 6.5. Exercise: Calculate Discount Averages
def average_discount(list_of_changes):
    total = 0
    count = 0
    for change in list_of_changes:
        if change < 0:
            total += (- change)     # to make it positive
            count += 1

    return round((total / count), 2) 


def calculate_discount_averages(lists):
    return_list=[]
    for small_list in lists:
        try: 
            rl_item=average_discount(small_list)
        except: 
            rl_item=0
        return_list.append(rl_item)
    return return_list

PRT=calculate_discount_averages([[-3.25, 4.5, 3.5], [-0.25, -2, -1, -1.5], [-4.25, -0.75, -2, 4.5]])
PRT=calculate_discount_averages([[2.75, 3.25, -3.25], [2.5, 1.99, 1, 1, 0.5],
                                 [-0.25, -4.5, -2.25, -4, 2, 2], [-3, -2.5, -3, -1.99, -4.5]])
PRT=calculate_discount_averages([[-0.75, 4, 2.25, 3.5, -1.25, 4.5],
                                [-1.5, -2.99, 3.99, -0.25, -0.25, -2, 2.99, -4, -3.25],
                                [1.25, 0.75, 0.5, 0.25, 1.5, 0.99],
                                [0.25, 0.25, 0.75, 1.5, 2.75, 3, 2.25],
                                [-3.25, 4.5, 4.99, 4.5, -1.99]])
print(PRT)
# [3.25, 1.19, 2.33]

>>> ball_game([1, 3, 2], 1)
1

>>> ball_game([1, 3, 2], 2)
3

>>> ball_game([1, 3, 2], 3)
3

>>> ball_game([3, 4, 5, 1, 2], 4)
2

>>> ball_game([3, 4, 5, 1, 2], 5)
5

>>> ball_game([3, 4, 5, 1, 2], 6)
5

>>> ball_game([8, 7, 1, 5, 3, 10, 4, 2, 6, 9], 4)
3

>>> ball_game([8, 7, 1, 5, 3, 10, 4, 2, 6, 9], 5)
5

>>> ball_game([8, 7, 1, 5, 3, 10, 4, 2, 6, 9], 6)
10

>>> ball_game([8, 7, 1, 5, 3, 10, 4, 2, 6, 9], 7)

#6.8. Exercise: Memento
def memento(file_name):
    try:
        fl=open(file_name,"r")
        content=fl.read()

        try:
            password=int(content)
            return "Finally you found the correct one! The password is: "+ str(password)
        except:return 'Wrong file, try again!'
    except: return "File not found, try again!"

test1=open("test1.txt","w")
test1.write("dasdkjlkldsa9102801")
test2=open("test2.txt","w")
test2.write("15646456")
test1.close()
test2.close()

print(memento("test.txt"))
# 'File not found, try again!'

print(memento("test1.txt"))
# 'Wrong file, try again!'

print(memento("test2.txt"))
# 'Finally you found the correct one! The password is: 15646456'

#7.1. Railway Statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dat=open("test1.txt","r")


data=pd.read_csv("california_housing_train.csv")
population=np.array(data["population"],dtype=int)
house=np.array(data["households"])
print(population)
print(house)
# help(pd)
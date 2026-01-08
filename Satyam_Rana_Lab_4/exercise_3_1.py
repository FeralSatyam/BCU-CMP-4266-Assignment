
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:29:11 2022

@author: minut
"""
def add(num1,num2):
    result = num1 + num2
    print(f"Results: adding {num1} by {num2} = {result}")
def subtract (num1,num2):
    result = num1 - num2
    print(f"Results: subtracting {num1} by {num2} = {result}")
def multipy(num1,num2):
    result = num1 * num2
    print(f"Results: multiplying {num1} by {num2} = {result}")
def divide (num1,num2):
    result = num1 / num2
    print(f"Results: dividing {num1} by {num2} = {result}")
def calculator(num1,num2,operator):
    match (operator):
        case '+':
            add(num1, num2)
        case '-':
            subtract(num1, num2)
        case '*':
            multipy(num1, num2)
        case '/':
            divide(num1, num2)

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
operator = input("Select and operator\n* for multiplication\n+ for addition\n/ for division: ")
calculator(num1, num2, operator)
# Author: Sona Keshishyan
__version__ = '0.1.0'

from operator import contains
import random
import re


def restrictions(y: str):
    list1 = list()
    y = y.replace(' ', '')
    y1 = (" ").join(y)
    y2 = y1.split()
    for i in y2:
        if i == 'A':
            if "A" not in list1:
                list1.append("A")
        elif i == 'B':
            if "B" not in list1:
                list1.append("B")
        else:
            if "C" not in list1:
                list1.append("C")
    return list1

def codeGenerator(size: int, restrictions: list):
    code = ""
    total_size = size
    if "A" in restrictions:
        total_size -= 1
        upper_case = random.randint(65, 90)
        code += chr(upper_case)
    if "B" in restrictions:
        total_size -= 1
        number = random.randint(48, 57)
        code += chr(number)
    if "C" in restrictions:
        total_size -= 1
        special1 = random.randint(33, 47)
        code += chr(special1)
    while total_size > 0:
        random_number = random.randint(1,100)
        if 1 <= random_number <= 14:
            x = random.randint(97, 122)
        elif 14 < random_number <= 28:
            x = random.randint(33, 47)
        elif 28 < random_number <= 42:
            x = random.randint(48,57)
        elif 42 < random_number <= 56:
            x = random.randint(58,64)
        elif 56 < random_number <= 70:
            x = random.randint(65,90)
        elif 70 < random_number <= 84:
            x = random.randint(123, 126)
        else:
            x = random.randint(97, 122)
        code += chr(x)
        total_size -= 1
    
    return code


def error(size, restriction):
    if size < len(restriction):
        return [True, "Size of password is too short for given restrictions"]
    if size > 25:
        return [True, "Max password length is 25 characters"]
    else:
        return [False]

    
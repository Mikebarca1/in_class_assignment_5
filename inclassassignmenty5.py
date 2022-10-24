#Problem 1:
#References:
#https://realpython.com/python-recursion/

import re

def sort(list_of_number):

    if len(list_of_number) <= 1:
        return list_of_number
    else:
        pivot = list_of_number[0]
        small = []
        big = []
        for i in range(1,len(list_of_number)):
            if list_of_number[i] < pivot:
                small.append(list_of_number[i])
            if list_of_number[i] > pivot:
                big.append(list_of_number[i])
        return sort(small) + [pivot] + sort(big)


    
def read(fileinput):
    list_of_number = []
    with open(fileinput) as file_object:
        numline = file_object.readline()
        number = re.findall("[0-9]+", numline)
        for x in number:
            x = int(x)
            list_of_number.append(x)
    return list_of_number



def write(fileoutput, number):
    with open(fileoutput, "w") as sorted_output:
        for b in sort(number):
            b = str(b)
            sorted_output.write(f"{b}\n")
            
            
def main():
    number = read("/Users/michaelotalora/Downloads/numbers.txt")
    return write("/Users/michaelotalora/Downloads/sorted.txt", number)


if __name__ == "__main__":
    main()
    
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:43:37 2022

@author: michaelotalora
"""


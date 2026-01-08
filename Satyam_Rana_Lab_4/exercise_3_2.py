# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:38:40 2022

@author: minut
"""

def get_data():
    h0 = int(input("Provide the number of houses with 0 occupancy: "))
    h1 = int(input("Provide the number of houses with 1 occupancy: "))
    h2 = int(input("Provide the number of houses with 2 occupancy: "))
    h3 = int(input("Provide the number of houses with 3 occupancy: "))
    h4 = int(input("Provide the number of houses with 4 occupancy: "))
    h5 = int(input("Provide the number of houses with 5 occupancy: "))
    h6 = int(input("Provide the number of houses with 6 occupancy: "))
    h7 = int(input("Provide the number of houses with 6+ occupancy: "))
    return h0, h1, h2, h3, h4, h5, h6, h7
    
def cal_percentage(h0,h1,h2,h3,h4,h5,h6,h7):
    total_house_sum = sum([h0, h1, h2, h3, h4, h5, h6], h7)
    p0 = float((h0/total_house_sum) * 100)
    p1 = float((h1/total_house_sum) * 100)
    p2 = float((h2/total_house_sum) * 100)
    p3 = float((h3/total_house_sum) * 100)
    p4 = float((h4/total_house_sum) * 100)
    p5 = float((h5/total_house_sum) * 100)
    p6 = float((h6/total_house_sum) * 100)
    p7 = float((h7/total_house_sum) * 100)
    return p0, p1, p2, p3, p4, p5, p6, p7

def display_result(h0,h1,h2,h3,h4,h5,h6,h7,p0,p1,p2,p3,p4,p5,p6,p7):
    for i in range(8):
        print(f"Occupants: {i}\t", end="")
    print(" ")
    print(f"No. houses: {h0}\t", end="")
    print(f"No. houses: {h1}\t", end="")
    print(f"No. houses: {h2}\t", end="")
    print(f"No. houses: {h3}\t", end="")
    print(f"No. houses: {h4}\t", end="")
    print(f"No. houses: {h5}\t", end="")
    print(f"No. houses: {h6}\t", end="")
    print(f"No. houses: {h7}\t", end="")
    print(" ")
    print(f"Percentage: {p0:.1f}%\t", end="")
    print(f"Percentage: {p1:.1f}%\t", end="")
    print(f"Percentage: {p2:.1f}%\t", end="")
    print(f"Percentage: {p3:.1f}%\t", end="")
    print(f"Percentage: {p4:.1f}%\t", end="")
    print(f"Percentage: {p5:.1f}%\t", end="")
    print(f"Percentage: {p6:.1f}%\t", end="")
    print(f"Percentage: {p7:.1f}%\t", end="")
    
if __name__=="__main__":
    h0,h1,h2,h3,h4,h5,h6,h7=get_data()
    p0,p1,p2,p3,p4,p5,p6,p7 = cal_percentage(h0,h1,h2,h3,h4,h5,h6,h7)
    display_result(h0,h1,h2,h3,h4,h5,h6,h7,p0,p1,p2,p3,p4,p5,p6,p7)
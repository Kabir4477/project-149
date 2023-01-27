# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:17:11 2023

@author: drsau
"""

from tkinter import *
import random

root=Tk()
root.title("Generate random password")
root.geometry("400x400")


label1 = Label(root)

def random_number():
    list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    random_no1 = random.randint(0,25)
    random_no2 = random.randint(0,25)
    random_no3 = random.randint(0, 25)
    random_no4 = random.randint(0, 25)
    random_no5 = random.randint(0, 25)


    
    random_alphabate1 = list1[random_no1]
    random_alphabate2 = list1[random_no2]
    random_alphabate3 = list1[random_no3]
    random_alphabate4 = list1[random_no4]
    random_alphabate5= list1[random_no5]

    label1["text"] =  random_alphabate1 + random_alphabate2 +  random_alphabate3 +  random_alphabate4 + random_alphabate5
    
btn1 = Button(root)
btn1 = Button(root, text="Generate Random Password ",command = random_number)
btn1.place(relx=0.5,rely = 0.5,anchor = CENTER )
label1.place(relx=0.5,rely=0.6,anchor=CENTER)


root.mainloop()
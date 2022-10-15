# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 20:05:40 2022

@author: turtl_4
"""

from tkinter import *
root=Tk()
root.title("fibonacci")
root.geometry("400x400")

label_series = Label(root,text="fibonacci series")
imput_num = Entry(root)
label_output_serias = Label(root)
label_output_sum = Label(root)


def fibonacci():
    number = int(imput_num.get())
    first_num=0
    second_num=1
    sum=0
    sum2=0
    counter = 1
    while(counter<=number):
        label_output_serias["text"] += str(sum) + " "
        label_output_sum["text"] = "fibonacci sum , " + str(sum2)
        counter = counter + 1
        first_num = second_num 
        second_num = sum
        sum = first_num + second_num
        sum2 = sum2 + sum
    




label_series.pack()
imput_num.pack()
btn = Button(root,text = "show fibonacci series",command = fibonacci)
btn.pack()
label_output_serias.pack()
label_output_sum.pack()
root.mainloop()
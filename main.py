import tkinter
from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("BMi Calculator")

#creating function

def calculate_bmi():
    kg = float(entry_kg.get())
    heigh = float(entry_height.get())
    bmi = kg / (heigh*heigh)
    label_result ['text'] = f"BMI:{bmi}"

#creatinng gui 

label_kg = Label(root, text= "KG: ")
label_kg.grid(column= 0, row= 0)

entry_kg = tkinter.Entry(root)
entry_kg.grid(column= 1, row= 0)

label_height = Label(root, text= "HEIGHT: ")
label_height.grid(column= 0, row= 1)

entry_height = tkinter.Entry(root)
entry_height.grid(column= 1, row= 1)

button_calculate = tkinter.Button(root, text="Calculate", command = calculate_bmi)
button_calculate.grid(column= 0, row= 2)

label_result = Label(root, text= "BMI: ")
label_result.grid(column= 1, row= 2)

root.mainloop()

#By Paikshit

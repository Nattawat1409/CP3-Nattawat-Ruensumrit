import math
from tkinter import *

def CalculateBMI(event):
    USER_BMI = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)  # convert unit from cm to m for firstly value to calculate
    formatBMI = "{:.1f}".format(USER_BMI)

    resultBMI.configure(text=formatBMI)
    if float(formatBMI) > 30:
        bodytype.configure(text="Very fat")
    elif float(formatBMI) >= 25.0:
        bodytype.configure(text="Fat")
    elif float(formatBMI) >= 23.0:
        bodytype.configure(text="Overweight")
    elif float(formatBMI) >= 18.6:
        bodytype.configure(text="Normal weight is appropriate")
    else:
        bodytype.configure(text="Your weight is Too thin")

Mainwindow = Tk()
Mainwindow.title("BMI Calculator")
Mainwindow.configure(bg="#f0f0f0")

Topic = Label(Mainwindow, text="Program to calculate BMI", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
Topic.grid(row = 0 , column = 0 ,columnspan = 2,pady=2)

labelHeight = Label(Mainwindow, text="Height (cm.):", font=("Helvetica", 12), bg="#f0f0f0")
labelHeight.grid(row=1, column=0, pady=5, padx=5 , sticky = E)
textBoxHeight = Entry(Mainwindow, font=("Helvetica", 12), width=10)
textBoxHeight.grid(row=1, column=1, pady=5, padx=5)

labelWeight = Label(Mainwindow, text="Weight (Kg.):", font=("Helvetica", 12), bg="#f0f0f0")
labelWeight.grid(row=2, column=0, pady=5, padx=5, sticky=E)
textBoxWeight = Entry(Mainwindow, font=("Helvetica", 12), width=10)
textBoxWeight.grid(row=2, column=1, pady=5, padx=5)

CalculateButton = Button(Mainwindow, text="Calculate BMI", font=("Helvetica", 12), activeforeground="white", activebackground="blue", bg="#4CAF50", fg="white", padx=10, pady=5)
CalculateButton.bind('<Button-1>', CalculateBMI)
CalculateButton.grid(row=3, column=0, columnspan=2, pady=10)

resultBMI = Label(Mainwindow, text="Result BMI", font=("Helvetica", 12), fg="white", bg="green",width= 10, padx=10, pady=5)
resultBMI.grid(row=4, column=0, columnspan=2, pady=5)

bodytype = Label(Mainwindow, text="Your Criteria", font=("Helvetica", 12), fg="white", bg="green", padx=10, pady=5)
bodytype.grid(row=5, column=0, columnspan=2, pady=5)

Mainwindow.mainloop()

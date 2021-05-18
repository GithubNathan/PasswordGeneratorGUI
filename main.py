import string
import random
import sys
import string
from tkinter import *
import pyperclip

ws = Tk()
ws.title('Password Generator')
ws.geometry('400x300')

def printLength():
    plength = length.get()
    Label(ws, text=f'{plength} characters.', pady=20, bg='#ffbf00').pack()
    i = 0
    password = "Password: "
    while i < int(plength):
        password += random.choice(otherCharList)
        password += random.choice(string.ascii_letters)
        i += 1

    Label(ws, text=password, pady=20, bg='#ffbf00').pack()
    pyperclip.copy(password)



length = Entry(ws)
length.pack(pady=30)

Button(ws, text="Set Password Length", padx=10, pady=5, command=printLength).pack()

otherCharList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']


ws.mainloop()


#!/usr/bin/python
#-*- coding:utf8 -*-

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

def eventMessage(self):
    messagebox.showinfo('たけのこ', 'ハローたけのこ')

def eventQuit(root):
    messagebox.showinfo('たけのこ', '終了します')
    root.destroy()

root = tk.Tk()
root.title('たけのこウインドウ')
root.geometry('800x660')

label = ttk.Label(root, text='たけのこアプリ')
label.pack(side='top', fill='both')

img = ImageTk.PhotoImage(Image.open('hello_takenoko.png', 'r'))
panel = tk.Label(root, image = img)
panel.pack(side='bottom', fill='both', expand='yes')

frame = ttk.Frame()
btn1 = ttk.Button(frame, text='こんにちは', command = lambda : eventMessage(btn1)).grid(column=0, row=0)
btn2 = ttk.Button(frame, text='終了', command = lambda : eventQuit(root)).grid(column=1, row=0)
frame.pack()

root.mainloop()

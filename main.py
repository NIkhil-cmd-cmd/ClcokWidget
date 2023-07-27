from tkinter import * 
#import ttk

root=Tk()
def _from_rgb(rgb):
    return "#%02x%02x%02x" %rgb
def time():
    string=strftime(' %a %D \n %-I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
from time import strftime 

root.title("Digital Clock")

label=Label(root, font=("times new roman", 80), background=_from_rgb((92,92,92)), foreground="yellow")
root.attributes("-alpha", 0.7)
label.pack(anchor="center")
time()
root.mainloop()
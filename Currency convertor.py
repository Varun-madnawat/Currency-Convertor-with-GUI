import tkinter as tk
from tkinter import ttk

def newcurr():
    z = float(entry.get())
    x = cur.get()
    y = tcur.get()
    new = z * (currency[y] / currency[x])
    h = round(new, 2)
    display = f"{z} {x} = {h} {y}"
    convertor.config(text=display) 


s = tk.Tk()
s.title("Currency converter")
s.geometry("400x150")

currency = {"USD": 1.00, "INR": 83.22, "EUR" : 0.92, "JPY" : 147, "GBP" : 0.79, "AUD" : 1.5 }

entry = tk.Entry(s, font=("Arial", 10),width= 15)
entry.grid(row=1, column=0, padx= 20,pady= 10)
entry.insert(0,"0.00")


n = tk.StringVar() 
cur = ttk.Combobox(s, width = 10, textvariable = n)
cur.grid(column = 1, row = 1, padx= 10,pady=10)
cur["values"] = list(currency.keys())
cur.current(1)


m = tk.StringVar() 
tcur = ttk.Combobox(s, width = 10, textvariable = m)
tcur.grid(column = 2, row = 1, padx=15,pady=10)
tcur["values"] = list(currency.keys())
tcur.current(2)

convertor= tk.StringVar()
convertor = ttk.Label(s, font=("Arial", 10))
convertor.grid(row=2, column=0, columnspan=3, padx=10, pady=10)



convert = ttk.Button(s, text="Convert", command=newcurr)
convert.grid(column=0, row=3, columnspan=3, pady=10)

s.mainloop()


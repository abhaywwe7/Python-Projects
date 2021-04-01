from tkinter import *
from yahoo_fin import stock_info

# https://www.marketwatch.com/investing/stock/dswl
def currentstockprice():
    price = stock_info.get_live_price(p1.get())
    Current_stock.set(price)

root = Tk()
root.title("Stock Predictor")
Current_stock = StringVar()
Label(root, text="Enter company symbol: ").grid(row=0, sticky= W)
Label(root, text="Result: ").grid(row=4, sticky= W)
result = Label(root, textvariable=Current_stock).grid(row=4, column= 1, sticky=W)
p1 = Entry(root)
p1.grid(row=0, column=1)
b= Button(root, text= "Show", command=currentstockprice)
b.grid(row=0, column=2, columnspan=2, rowspan=1, padx=5,pady=4 )
mainloop()
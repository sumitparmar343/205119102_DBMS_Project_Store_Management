# import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect( host="localhost", user="root", passwd="7729", database='store' )
c = conn.cursor()

class Database:
    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.heading = Label(master, text="Add To The Database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=450, y=0)

        # labels for the window
        self.name_l = Label(master, text="Enter Product Name", font=('arial 18 bold'))
        self.name_l.place(x=0, y=70)

        self.stock_l = Label(master, text="Enter Stocks", font=("arial 18 bold"))
        self.stock_l.place(x=0, y=120)
        
        self.cp_l = Label(master, text="Enter Cost Price", font=("arial 18 bold"))
        self.cp_l.place(x=0, y=170)
        
        self.sp_l = Label(master, text="Enter Selling Price", font=("arial 18 bold"))
        self.sp_l.place(x=0, y=220)
        
        self.vendor_l = Label(master, text="Enter Vendor Name", font=("arial 18 bold"))
        self.vendor_l.place(x=0, y=270)
        
        self.vendor_phone_l = Label(master, text="Enter Vendor Phone Number", font=("arial 18 bold"))
        self.vendor_phone_l.place(x=0, y=320) 

        # entries for lables
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=400, y=70)
        
        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=400, y=120)
        
        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=400, y=170)
        
        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=400, y=220)
        
        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=400, y=270)
        
        self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_phone_e.place(x=400, y=320)

        # button to add to the database
        self.btn_add = Button(master, text="Add To Database", width=25, height=2, bg='steelblue', fg='white', command = self.get_items)
        self.btn_add.place(x=520, y=370)
    
        # text box for the logs
        self.tBox = Text(master, width=60, height=20)
        self.tBox.place(x=800, y=70)

    def get_items(self, *args, **kwaargs):
        
        # get data from entries
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()

        
        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("Error", "Please Fill All Entries.")
        else:
            # dynamic entries
            self.totalcp = float(self.cp) * float(self.stock)
            self.totalsp = float(self.sp) * float(self.stock)
            self.assumed_profit = float(self.totalsp - self.totalcp)
            
            sql = "INSERT INTO inventory (name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phone))
            conn.commit()

            tkinter.messagebox.showinfo("Success", "Successfully added to the Database.")

            

root = Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Add To Database")
root.mainloop()




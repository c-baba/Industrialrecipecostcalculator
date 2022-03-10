from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import sqlite3
from ingredientreport import ingredientreport
from tkinter import filedialog
import csv
import pandas as pd
def pricelist():
    
    
    
    price = tk.ThemedTk()
    price.get_themes()
    price.set_theme("adapta")

    w = 1500
    h = 700
    ws = price.winfo_screenwidth()
    hs = price.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    price.geometry("%dx%d+%d+%d" % (w, h, x, y))
    price.title("Price List")

    #conn1 = sqlite3.connect("//10.185.8.2//data//10 - PRODUCTION//24 - Cost Control//Pricelist.db") From server
    conn1 = sqlite3.connect("Pricelist.db")

    c1 = conn1.cursor()
    recordlast = c1.execute("SELECT  ID FROM prices").fetchall()[-1]
    recordid = (int(recordlast[0]))

    def excel():
        cols = ["ID","Category", "Type", "Product Name", "Supplier", "Price/Unit", "Currency"]  # Your column headings here
        path = 'pricelist.csv'
        excel_name = filedialog.asksaveasfilename(title='Save location', defaultextension=[('Excel', '*.xlsx')],
                                                  filetypes=[('Excel', '*.xlsx')])
        lst = []
        with open(path, "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')
            for row_id in tree.get_children():
                row = tree.item(row_id, 'values')
                lst.append(row)
            lst = list(map(list, lst))
            lst.insert(0, cols)
            for row in lst:
                csvwriter.writerow(row)

        writer = pd.ExcelWriter(excel_name)
        df = pd.read_csv(path, encoding="iso8859_9")
        df.to_excel(writer, 'sheetname')
        writer.save()

    def submit():



        id = recordid+1

        conn = sqlite3.connect("PriceList.db")
        c = conn.cursor()
        c.execute("INSERT INTO prices  VALUES (:e_ID,:e_Category, :e_Type, :e_PrdName,:e_Supplier, :e_PriceUnit, :e_Currency)",
                {
                    "e_ID":id,
                    "e_Category": e_Category.get(),
                    "e_Type": e_Type.get(),
                    "e_PrdName": e_PrdName.get(),
                    "e_Supplier": e_Supplier.get(),
                    "e_PriceUnit": e_PriceUnit.get(),
                    "e_Currency": e_Currency.get(),

                }


                )

        conn.commit()
        conn.close()

           
        e_Category.delete(0, END)
        e_Type.delete(0, END)
        e_PrdName.delete(0, END)
        e_Supplier.delete(0, END)
        e_PriceUnit.delete(0,END)
        e_Currency.delete(0, END)
        view()
    
    
    def delete():
        conn = sqlite3.connect("PriceList.db")
        c = conn.cursor()

        c.execute("DELETE FROM 'Prices' WHERE ID like ?", (Deleterecord.get(),))

        conn.commit()
        conn.close()
        Deleterecord.delete(0,END)
        view()

    def view():
        for record in tree.get_children():
            tree.delete(record)
        conn = sqlite3.connect("Pricelist.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Prices")
        rows = cur.fetchall()
        for row in rows:
            tree.insert(parent="", index=0, values=row)
        conn.close()

    def searchproductname():

        lookup_record = filtre1.get()
        for record in tree.get_children():
            tree.delete(record)
        conn = sqlite3.connect("PriceList.db")
        c = conn.cursor()

        c.execute("SELECT  * FROM prices WHERE Productname like ?", (lookup_record,))
        records = c.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                tree.insert(parent="", index="end", iid=count, text='',
                            values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                            tags=('evenrow'))
            else:
                tree.insert(parent="", index="end", iid=count, text='',
                            values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                            tags=('evenrow'))
            count += 1
        conn.commit()
        conn.close()
        filtre1.delete(0, END)

    def searchcategory():

        lookup_record = filtre1.get()
        for record in tree.get_children():
            tree.delete(record)
        conn = sqlite3.connect("PriceList.db")
        c = conn.cursor()

        c.execute("SELECT  * FROM prices WHERE Category like ?", (lookup_record,))
        records = c.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                tree.insert(parent="", index="end", iid=count, text='',
                            values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                            tags=('evenrow'))
            else:
                tree.insert(parent="", index="end", iid=count, text='',
                            values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                            tags=('evenrow'))
            count += 1
        conn.commit()
        conn.close()
        filtre1.delete(0, END)

    def searchsupplier():

        lookup_record = filtre1.get()
        for record in tree.get_children():
            tree.delete(record)
        conn = sqlite3.connect("PriceList.db")
        c = conn.cursor()

        c.execute("SELECT  * FROM Prices WHERE Supplier like ?", (lookup_record,))
        records = c.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                tree.insert(parent="", index="end", iid=count, text='',
                            values=(
                            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                            tags=('evenrow'))
            else:
                tree.insert(parent="", index="end", iid=count, text='',
                            values=(
                            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                            tags=('evenrow'))
            count += 1
        conn.commit()
        conn.close()
        filtre1.delete(0, END)

    lookup_record = StringVar()

    # Newprice
    Label1 = ttk.Label(price, text="New Ingredient Record", font=("Helvetica", 12), background="#f0f0f0")
    Label1.place(x=82, y=10)

    # Category
    Categorylabel = ttk.Label(price, text="Category         :", font=("Helvetica", 11), background="#f0f0f0")
    Categorylabel.place(x=10, y=40)
    current_var = StringVar()
    e_Category = ttk.Combobox(price,textvariable=current_var, width=40,height=5)

    e_Category['values'] = ('Raw Material', 'Ingredient', 'Packaging Material',"Other Material")
    e_Category['state'] = 'readonly'
    e_Category.place(x=86, y=33)

    # Type
    Typelabel = ttk.Label(price, text="Type", font=("Helvetica", 11), background="#f0f0f0")
    Typelabel.place(x=10, y=80)
    e_Type = ttk.Entry(price, width=40)
    e_Type.place(x=86, y=73)

    # Prd.Name
    PrdNamelabel = ttk.Label(price, text="Product", font=("Helvetica", 11), background="#f0f0f0")
    PrdNamelabel.place(x=10, y=110)
    e_PrdName = ttk.Entry(price, width=40)
    e_PrdName.place(x=86, y=103)

    # Supplier
    Supplierlabel = ttk.Label(price, text="Supplier    ", font=("Helvetica", 11), background="#f0f0f0")
    Supplierlabel.place(x=10, y=140)
    e_Supplier = ttk.Entry(price, width=40)
    e_Supplier.place(x=86, y=133)

    # Price/Unit
    PriceUnitlabel = ttk.Label(price, text="Price/Unit       ", font=("Helvetica", 11), background="#f0f0f0")
    PriceUnitlabel.place(x=10, y=170)
    e_PriceUnit = ttk.Entry(price, width=40)
    e_PriceUnit.place(x=86, y=163)

    # Currency
    Currencylabel = ttk.Label(price, text="Currency       :", font=("Helvetica", 11), background="#f0f0f0")
    Currencylabel.place(x=10, y=200)
    e_Currency = ttk.Entry(price, width=40)
    e_Currency.place(x=86, y=193)

    # Save Record
    Button1 = ttk.Button(price, text="Save Record", padding=(125, 10),command=submit)
    Button1.place(x=10, y=233)

    # DeleteRecord
    Label2 = ttk.Label(price, text="Delete Record", font=("Helvetica", 12), background="#f0f0f0")
    Label2.place(x=82, y=280)

    Deleterecordlabel = ttk.Label(price, text="Enter the ID number You Want to Delete", font=("Helvetica", 10),
                              background="#f0f0f0")
    Deleterecordlabel.place(x=10, y=305)
    Deleterecordl = StringVar()
    Deleterecord = ttk.Entry(price, width=52, textvariable=Deleterecordl)
    Deleterecord.place(x=10, y=330)

    ButtonDeleterecord = ttk.Button(price, text="Delete Record", padding=(125, 10), command=delete)
    ButtonDeleterecord.place(x=10, y=360)


    #table
    tree = ttk.Treeview(price, columns=("ID","Category", "Type", "Product Name", "Supplier", "Price/Unit", "Currency"),
                        show="headings",
                        height=29)
    tree.heading("#1", text="ID")
    tree.column("#1", minwidth=0, width=50)
    tree.heading("#2", text="Category")
    tree.column("#2", minwidth=0, width=200)
    tree.heading("#3", text="Type")
    tree.column("#3", minwidth=0, width=200)
    tree.heading("#4", text="Product Name")
    tree.column("#4", minwidth=0, width=200)
    tree.heading("#5", text="Supplier")
    tree.column("#5", minwidth=0, width=150)
    tree.heading("#6", text="Price/Unit")
    tree.column("#6", minwidth=0, width=100)
    tree.heading("#7", text="Currency")
    tree.column("#7", minwidth=0, width=100)

    tree.place(x=360, y=30)
    price.command(view())




    # Filter
    lookup_record = StringVar()

    labelfiltre = ttk.Label(price, text="Search with Filter", font=("Helvetica", 11), background="#f0f0f0")
    labelfiltre.place(x=82, y=410)

    filtre1 = ttk.Entry(price, width=52, textvariable=lookup_record)
    filtre1.place(x=10, y=430)

    filtrereset = ttk.Button(price, text="Clear Filter", padding=(20, 51), command=view)
    filtrereset.place(x=220, y=465)

    filtrebutton = ttk.Button(price, text="Search with \nProduct Name", width=30,command=searchproductname)
    filtrebutton.place(x=10, y=465)

    filtrebuton2 = ttk.Button(price, text="Search with \nCategory", width=30,command=searchcategory)
    filtrebuton2.place(x=10, y=508)

    filtrebuton2 = ttk.Button(price, text="Search with \nSupplier", width=30,command=searchsupplier)
    filtrebuton2.place(x=10, y=552)

    # Button Back

    Buton2 = ttk.Button(price, text="Back", padding=(135, 10), command=price.destroy)
    Buton2.place(x=10, y=645)

    Buton2 = ttk.Button(price, text="Save list a Excel", padding=(30, 10),command=excel)
    Buton2.place(x=190, y=600)

    # Buton Ingredient Report
    Buton2 = ttk.Button(price, text="Ingredient Reports", padding=(30, 10),command=ingredientreport)
    Buton2.place(x=10, y=600)


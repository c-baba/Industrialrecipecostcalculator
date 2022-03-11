from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import sqlite3
from tkinter import filedialog
import csv
import pandas as pd
from tkinter import messagebox
import pyscreenshot
from PIL import Image

def cvslist():
    cvslist = tk.ThemedTk()
    cvslist.get_themes()
    cvslist.set_theme("adapta")

    w = 1500
    h = 700
    ws = cvslist.winfo_screenwidth()
    hs = cvslist.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    cvslist.geometry("%dx%d+%d+%d" % (w, h, x, y))
    cvslist.title("CVS List")

    def excel():
        cols = ["Date", "Product Name", "Recipe Price", "Manpower Price", "Energy Price", "Packaging","CVS","CVS Per Pack","CVS Without Packaging"]  # Your column headings here
        path = 'cvslist.csv'
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
        df = pd.read_csv(path, encoding="utf-8")
        df.to_excel(writer, 'sheetname')
        writer.save()

    def view():
        for record in tree.get_children():
            tree.delete(record)
        conn = sqlite3.connect("cvsdatabase.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM cvsdatabase")
        rows = cur.fetchall()
        for row in rows:
            tree.insert(parent="", index=0, values=row)
        conn.close()

    tree = ttk.Treeview(cvslist, columns=(
    "Date", "Product Name", "Recipe Price", "Manpower Price", "Energy Price", "Packaging", "Recipe Price", "Recipe Price Per Pack","Recipe Price Without Packaging"),
                        show="headings",
                        height=29)
    tree.heading("#1", text="Date")
    tree.column("#1", minwidth=0, width=50)
    tree.heading("#2", text="Product Name")
    tree.column("#2", minwidth=0, width=200)
    tree.heading("#3", text="Recipe Price")
    tree.column("#3", minwidth=0, width=200)
    tree.heading("#4", text="Manpower Price")
    tree.column("#4", minwidth=0, width=200)
    tree.heading("#5", text="Energy Price")
    tree.column("#5", minwidth=0, width=150)
    tree.heading("#6", text="Packaging")
    tree.column("#6", minwidth=0, width=100)
    tree.heading("#7", text="Recipe Price")
    tree.column("#7", minwidth=0, width=100)
    tree.heading("#8", text="Recipe Price Per Pack")
    tree.column("#8", minwidth=0, width=100)
    tree.heading("#9", text="Recipe Price Without Packaging")
    tree.column("#9", minwidth=0, width=200)
    tree.place(x=180, y=30)

    def OnDoubleClick(event):
        curItem = tree.focus()
        a = tree.item(curItem)
        b = (a["values"])

        name = b[1]+ ".png"

        img = Image.open(name)
        img.show()

    tree.bind("<Double-1>", OnDoubleClick)
    cvslist.command(view())

    butonexcel = ttk.Button(cvslist,text="Save as Excel",command=excel)
    butonexcel.place(x=30,y=100)
    butonexit = ttk.Button(cvslist,text="Exit",command=cvslist.destroy)
    butonexit.place(x=30,y=160)
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import sqlite3
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from tkinter import messagebox
import pyscreenshot

from datetime import date

from collections import Counter

def ingredientreport():
    ingredientreport = tk.ThemedTk()
    ingredientreport.get_themes()
    ingredientreport.set_theme("adapta")

    w = 1550
    h = 850
    ws = ingredientreport.winfo_screenwidth()
    hs = ingredientreport.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    ingredientreport.geometry("%dx%d+%d+%d" % (w, h, x, y))
    ingredientreport.configure(background="#FFFFFF")
    ingredientreport.title("Ingredient Report")





    s = ttk.Style()
    s.configure('TFrame', background='#FFFFFF')

    frame1 = ttk.Frame(ingredientreport, width=1550, height=800,style='TFrame')

    frame1.place(x=0, y=0)
  




    def rawmaterial():

        frame1.destroy()
        frame2 = ttk.Frame(ingredientreport, width=1550, height=800, style='TFrame')

        frame2.place(x=0, y=0)

        buton = ttk.Button(frame2, text="Raw Material \nReport", command=rawmaterial)
        buton.place(x=10, y=1)

        buton = ttk.Button(frame2, text="Ingredient Material \nReport", command=Ingredient)

        buton.place(x=100, y=1)

        buton = ttk.Button(frame2, text="Packaging Material \nReport", command=Packaging)
        buton.place(x=220, y=0)

        buton = ttk.Button(frame2, text="Other Material \nReport", command=other)
        buton.place(x=335, y=0)

        i = "Raw Material"

        conn = sqlite3.connect("PriceList.db")
        c = conn.cursor()
        c.execute("SELECT  Productname FROM prices WHERE Category like ?", (i,))
        records = c.fetchall()
        c.execute("SELECT  Price FROM prices WHERE Category like ?", (i,))
        recordsprice = c.fetchall()
        c.execute("SELECT  Supplier FROM prices WHERE Category like ?", (i,))
        recordssupplier = c.fetchall()
        conn = sqlite3.connect("cvsdatabase.db")
        c = conn.cursor()
        c.execute("SELECT  Recipeall FROM cvsdatabase ")
        recordsrecipeall = c.fetchall()


        recipeingredient = []
        a= []
        for row in recordsrecipeall:
            a.append(row[0])
            for val in a:
                if val != None:
                    recipeingredient.append(val)


        recipeall = []
        c = 0
        for i in recipeingredient:
            a = recipeingredient[c]
            lista = a.split(",")
            for b in lista:
                recipeall.append(b)
            c += 1

        cee = []
        for row in records:
            cee.append(row[0])
        finalrecipeamount = []

        for a in cee:
            for b in recipeall:
                if a ==b:
                    finalrecipeamount.append(b)

        #fig how many time use ingredient in recipe

        fig = Figure(figsize=(6, 4),
                     dpi=100)


        plt = fig.add_subplot()

        counts = Counter(finalrecipeamount)
        plt.set_title("Raw Material Usage Rate in Recipes", fontsize=12)
        plt.pie([v for v in counts.values()], labels=[k for k in counts],
                autopct='%1.1f%%', shadow=True, textprops={'fontsize': 8})

        fig.set_facecolor('white')
        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=-69, y=400)
        #-----------------------------------------------
        fig = Figure(figsize=(6, 4),
                     dpi=100)

        c = []
        for row in recordssupplier:
            c.append(row[0])
        y = Counter(c)


        plt = fig.add_subplot()

        counts = Counter(c)
        plt.set_title("Supplier List For Raw Material", fontsize=12)
        plt.pie([v for v in counts.values()], labels=[k for k in counts],
                autopct='%1.1f%%', shadow=True, textprops={'fontsize': 10})

        fig.set_facecolor('white')
        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=-69, y=50)

        # bar plot price ıqf fruit
        fig = Figure(figsize=(12, 7),
                     dpi=100)
        c = []
        for row in records:
            c.append(row[0])
        x = c

        d = []
        for row in recordsprice:
            d.append(row[0])
        y = d
        plt = fig.add_subplot()

        plt.set_title("Price List For Raw Material", fontsize=12)

        plt.barh(x, y)
        for i, v in enumerate(y):
            plt.text(v + 0.5, i + .01, str(v), color='Black')

        fig.set_facecolor('white')

        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=450, y=5)

    buton = ttk.Button(ingredientreport, text="Raw Material \nReport", command=rawmaterial)
    buton.place(x=10,y=1)
    def Ingredient():
        frame1.destroy()
        frame2 = ttk.Frame(ingredientreport, width=1550, height=800, style='TFrame')

        frame2.place(x=0, y=0)

        buton = ttk.Button(frame2, text="Raw Material \nReport", command=rawmaterial)
        buton.place(x=10, y=1)

        buton = ttk.Button(frame2, text="Ingredient Material \nReport", command=Ingredient)

        buton.place(x=100, y=1)

        buton = ttk.Button(frame2, text="Packaging Material \nReport", command=Packaging)
        buton.place(x=220, y=0)

        buton = ttk.Button(frame2, text="Other Material \nReport", command=other)
        buton.place(x=335, y=0)

        i = "Ingredient"

        conn = sqlite3.connect("PriceList.db")
        c = conn.cursor()
        c.execute("SELECT  Productname FROM prices WHERE Category like ?", (i,))
        records = c.fetchall()
        c.execute("SELECT  Price FROM prices WHERE Category like ?", (i,))
        recordsprice = c.fetchall()
        c.execute("SELECT  Supplier FROM prices WHERE Category like ?", (i,))
        recordssupplier = c.fetchall()
        conn = sqlite3.connect("cvsdatabase.db")
        c = conn.cursor()
        c.execute("SELECT  Recipeall FROM cvsdatabase ")
        recordsrecipeall = c.fetchall()

        recipeingredient = []
        a = []
        for row in recordsrecipeall:
            a.append(row[0])
            for val in a:
                if val != None:
                    recipeingredient.append(val)

        recipeall = []
        c = 0
        for i in recipeingredient:
            a = recipeingredient[c]
            lista = a.split(",")
            for b in lista:
                recipeall.append(b)
            c += 1

        cee = []
        for row in records:
            cee.append(row[0])
        finalrecipeamount = []

        for a in cee:
            for b in recipeall:
                if a == b:
                    finalrecipeamount.append(b)

        # fig how many time use ingredient in recipe

        fig = Figure(figsize=(6, 4),
                     dpi=100)

        plt = fig.add_subplot()

        counts = Counter(finalrecipeamount)
        plt.set_title("Raw Material Usage Rate in Recipes", fontsize=12)
        plt.pie([v for v in counts.values()], labels=[k for k in counts],
                autopct='%1.1f%%', shadow=True, textprops={'fontsize': 8})

        fig.set_facecolor('white')
        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=-69, y=400)
        #-------------------------------------------------------
        fig = Figure(figsize=(6, 4),
                     dpi=100)

        c = []
        for row in recordssupplier:
            c.append(row[0])
        y = Counter(c)

        plt = fig.add_subplot()

        counts = Counter(c)
        plt.set_title("Supplier List For Ingredient Material", fontsize=12)
        plt.pie([v for v in counts.values()], labels=[k for k in counts],
                autopct='%1.1f%%', shadow=True, textprops={'fontsize': 10})

        fig.set_facecolor('white')
        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=-69, y=50)

        # bar plot price ıqf fruit
        fig = Figure(figsize=(12, 7),
                     dpi=100)
        c = []
        for row in records:
            c.append(row[0])
        x = c

        d = []
        for row in recordsprice:
            d.append(row[0])
        y = d
        plt = fig.add_subplot()

        plt.set_title("Price List For Ingredient Material", fontsize=12)

        plt.barh(x, y)
        for i, v in enumerate(y):
            plt.text(v + 0.5, i + .01, str(v), color='Black')

        fig.set_facecolor('white')

        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=450, y=5)

    buton = ttk.Button(ingredientreport, text="Ingredient Material \nReport", command=Ingredient)
    buton.place(x=100, y=1)


    def Packaging():

        frame1.destroy()
        frame2 = ttk.Frame(ingredientreport, width=1550, height=800, style='TFrame')

        frame2.place(x=0, y=0)

        buton = ttk.Button(frame2, text="Raw Material \nReport", command=rawmaterial)
        buton.place(x=10, y=1)

        buton = ttk.Button(frame2, text="Ingredient Material \nReport", command=Ingredient)

        buton.place(x=100, y=1)

        buton = ttk.Button(frame2, text="Packaging Material \nReport", command=Packaging)
        buton.place(x=220, y=0)

        buton = ttk.Button(frame2, text="Other Material \nReport", command=other)
        buton.place(x=335, y=0)

        i = "Packaging Material"

        conn = sqlite3.connect("PriceList.db")
        c = conn.cursor()
        c.execute("SELECT  Productname FROM prices WHERE Category like ?", (i,))
        records = c.fetchall()
        c.execute("SELECT  Price FROM prices WHERE Category like ?", (i,))
        recordsprice = c.fetchall()
        c.execute("SELECT  Supplier FROM prices WHERE Category like ?", (i,))
        recordssupplier = c.fetchall()
        conn = sqlite3.connect("cvsdatabase.db")
        c = conn.cursor()
        c.execute("SELECT  Recipeall FROM cvsdatabase ")
        recordsrecipeall = c.fetchall()

        recipeingredient = []
        a = []
        for row in recordsrecipeall:
            a.append(row[0])
            for val in a:
                if val != None:
                    recipeingredient.append(val)

        recipeall = []
        c = 0
        for i in recipeingredient:
            a = recipeingredient[c]
            lista = a.split(",")
            for b in lista:
                recipeall.append(b)
            c += 1

        cee = []
        for row in records:
            cee.append(row[0])
        print(cee)
        finalrecipeamount = []

        for a in cee:
            for b in recipeall:
                if a == b:
                    finalrecipeamount.append(b)
        print(finalrecipeamount)
        # fig how many time use ingredient in recipe

        fig = Figure(figsize=(6, 4),
                     dpi=100)

        plt = fig.add_subplot()

        counts = Counter(finalrecipeamount)
        plt.set_title("Raw Material Usage Rate in Recipes", fontsize=12)
        plt.pie([v for v in counts.values()], labels=[k for k in counts],
                autopct='%1.1f%%', shadow=True, textprops={'fontsize': 8})

        fig.set_facecolor('white')
        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=-69, y=400)
        # -------------------------------------------------------
        fig = Figure(figsize=(6, 4),
                     dpi=100)

        c = []
        for row in recordssupplier:
            c.append(row[0])
        y = Counter(c)

        plt = fig.add_subplot()

        counts = Counter(c)
        plt.set_title("Supplier List For Packaging Material", fontsize=12)
        plt.pie([v for v in counts.values()], labels=[k for k in counts],
                autopct='%1.1f%%', shadow=True, textprops={'fontsize': 10})

        fig.set_facecolor('white')
        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=-69, y=50)

        # bar plot price ıqf fruit
        fig = Figure(figsize=(12, 7),
                     dpi=100)
        c = []
        for row in records:
            c.append(row[0])
        x = c

        d = []
        for row in recordsprice:
            d.append(row[0])
        y = d
        plt = fig.add_subplot()

        plt.set_title("Price List For Packaging Material", fontsize=12)

        plt.barh(x, y)
        for i, v in enumerate(y):
            plt.text(v + 0.5, i + .01, str(v), color='Black')

        fig.set_facecolor('white')

        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=450, y=5)

    buton = ttk.Button(ingredientreport, text="Packaging Material \nReport", command=Packaging)
    buton.place(x=220, y=0)


    def other():

        frame1.destroy()
        frame2 = ttk.Frame(ingredientreport, width=1550, height=800, style='TFrame')

        frame2.place(x=0, y=0)

        buton = ttk.Button(frame2, text="Raw Material \nReport", command=rawmaterial)
        buton.place(x=10, y=1)

        buton = ttk.Button(frame2, text="Ingredient Material \nReport", command=Ingredient)

        buton.place(x=100, y=1)

        buton = ttk.Button(frame2, text="Packaging Material \nReport", command=Packaging)
        buton.place(x=220, y=0)

        buton = ttk.Button(frame2, text="Other Material \nReport", command=other)
        buton.place(x=335, y=0)

        i = "Other Material"

        conn = sqlite3.connect("PriceList.db")
        c = conn.cursor()
        c.execute("SELECT  Productname FROM prices WHERE Category like ?", (i,))
        records = c.fetchall()
        c.execute("SELECT  Price FROM prices WHERE Category like ?", (i,))
        recordsprice = c.fetchall()
        c.execute("SELECT  Supplier FROM prices WHERE Category like ?", (i,))
        recordssupplier = c.fetchall()
        conn = sqlite3.connect("cvsdatabase.db")
        c = conn.cursor()
        c.execute("SELECT  Recipeall FROM cvsdatabase ")
        recordsrecipeall = c.fetchall()

        recipeingredient = []
        a = []
        for row in recordsrecipeall:
            a.append(row[0])
            for val in a:
                if val != None:
                    recipeingredient.append(val)

        recipeall = []
        c = 0
        for i in recipeingredient:
            a = recipeingredient[c]
            lista = a.split(",")
            for b in lista:
                recipeall.append(b)
            c += 1

        cee = []

        for row in records:
            cee.append(row[0])
        finalrecipeamount = []

        for a in cee:
            for b in recipeall:
                if a == b:
                    finalrecipeamount.append(b)

        # fig how many time use ingredient in recipe

        fig = Figure(figsize=(6, 4),
                     dpi=100)

        plt = fig.add_subplot()

        counts = Counter(finalrecipeamount)
        plt.set_title("Raw Material Usage Rate in Recipes", fontsize=12)
        plt.pie([v for v in counts.values()], labels=[k for k in counts],
                autopct='%1.1f%%', shadow=True, textprops={'fontsize': 8})

        fig.set_facecolor('white')
        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=-69, y=400)
        # -------------------------------------------------------
        fig = Figure(figsize=(6, 4),
                     dpi=100)

        c = []
        for row in recordssupplier:
            c.append(row[0])
        y = Counter(c)

        plt = fig.add_subplot()

        counts = Counter(c)
        plt.set_title("Supplier List For Other Material", fontsize=12)
        plt.pie([v for v in counts.values()], labels=[k for k in counts],
                autopct='%1.1f%%', shadow=True, textprops={'fontsize': 10})

        fig.set_facecolor('white')
        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=-69, y=50)

        # bar plot price ıqf fruit
        fig = Figure(figsize=(12, 7),
                     dpi=100)
        c = []
        for row in records:
            c.append(row[0])
        x = c

        d = []
        for row in recordsprice:
            d.append(row[0])
        y = d
        plt = fig.add_subplot()

        plt.set_title("Price List For Other Material", fontsize=12)

        plt.barh(x, y)
        for i, v in enumerate(y):
            plt.text(v + 0.5, i + .01, str(v), color='Black')

        fig.set_facecolor('white')

        canvas = FigureCanvasTkAgg(fig,
                                   master=frame2)
        canvas.draw()

        canvas.get_tk_widget().place(x=450, y=5)

    buton = ttk.Button(ingredientreport, text="Other Material \nReport", command=other)
    buton.place(x=335, y=0)
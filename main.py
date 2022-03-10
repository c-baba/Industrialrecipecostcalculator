from pricelist import pricelist
from cvscalculator import RecipeCostcalculator
from cvslist import cvslist
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk


mainl = tk.ThemedTk()
mainl.get_themes()
mainl.set_theme("adapta")
w = 800
h = 300
ws = mainl.winfo_screenwidth()
hs = mainl.winfo_screenheight()


x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
mainl.geometry("%dx%d+%d+%d" % (w, h, x, y))
mainl.config(bg="white")
mainl.title("Recipe Price Calculator")
buton = ttk.Button(mainl, text="Price of Ingredients", width=30, command=pricelist)
buton.place(x=30, y=100)
buton = ttk.Button(mainl, text="Recipe Price List", width=30, command=cvslist)
buton.place(x=30, y=150)
buton = ttk.Button(mainl, text="Recipe Price Calculator", width=30, command=RecipeCostcalculator)
buton.place(x=30, y=200),

howtouse = ttk.Label(mainl, text="                               How to Use\n"
                                 "Price of Ingredient Menu: You can see all ingredient in database, \nadd or delete ingredient"
                                 ",Save as Excel Database and See Ingredient Reports \n"
                                 "Recipe Price List Menu: You can see Price Records About Recipes\n"
                                 "Recipe Price Calculator Menu: You call calculate Recipe Price and Save in Database",background="#FFFFFF")
howtouse.place(x=260,y=100)

mainloop()

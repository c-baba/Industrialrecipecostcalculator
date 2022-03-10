import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import sqlite3
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from tkinter import messagebox
from PIL import ImageGrab

from datetime import date
import time

from collections import Counter

def RecipeCostcalculator():
    RecipeCostcalculator = tk.ThemedTk()
    RecipeCostcalculator.get_themes()
    RecipeCostcalculator.set_theme("adapta")

    w = 1000
    h = 700
    ws = RecipeCostcalculator.winfo_screenwidth()
    hs = RecipeCostcalculator.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    RecipeCostcalculator.geometry("%dx%d+%d+%d" % (w, h, x, y))

    RecipeCostcalculator.title("RecipeCost Calculator")

    def calculateRecipeCost():

        #calculateRecipeCost---------------------------------------------------------------------------------------------
        # recipecalculate
        listingredient = []
        listamount = []
        def createlist():
            if entryingredient1.get() != "":
                listingredient.append(entryingredient1.get())
                listamount.append(entryingredient1amount.get())
            if entryingredient2.get() != "":
                listingredient.append(entryingredient2.get())
                listamount.append(entryingredient2amount.get())
            if entryingredient3.get() != "":
                listingredient.append(entryingredient3.get())
                listamount.append(entryingredient3amount.get())
            if entryingredient4.get() != "":
                listingredient.append(entryingredient4.get())
                listamount.append(entryingredient4amount.get())
            if entryingredient5.get() != "":
                listingredient.append(entryingredient5.get())
                listamount.append(entryingredient5amount.get())
            if entryingredient6.get() != "":
                listingredient.append(entryingredient6.get())
                listamount.append(entryingredient6amount.get())
            if entryingredient7.get() != "":
                listingredient.append(entryingredient7.get())
                listamount.append(entryingredient7amount.get())
            if entryingredient8.get() != "":
                listingredient.append(entryingredient8.get())
                listamount.append(entryingredient8amount.get())
            if entryingredient9.get() != "":
                listingredient.append(entryingredient9.get())
                listamount.append(entryingredient9amount.get())
            if entryingredient10.get() != "":
                listingredient.append(entryingredient10.get())
                listamount.append(entryingredient10amount.get())
            if entryingredient11.get() != "":
                listingredient.append(entryingredient11.get())
                listamount.append(entryingredient11amount.get())
            if entryingredient12.get() != "":
                listingredient.append(entryingredient12.get())
                listamount.append(entryingredient12amount.get())
            if entryingredient13.get() != "":
                listingredient.append(entryingredient13.get())
                listamount.append(entryingredient13amount.get())
            if entryingredient14.get() != "":
                listingredient.append(entryingredient14.get())
                listamount.append(entryingredient14amount.get())
            if entryingredient15.get() != "":
                listingredient.append(entryingredient15.get())
                listamount.append(entryingredient15amount.get())
            if entryingredient16.get() != "":
                listingredient.append(entryingredient16.get())
                listamount.append(entryingredient16amount.get())
            if entryingredient17.get() != "":
                listingredient.append(entryingredient17.get())
                listamount.append(entryingredient17amount.get())
            if entryingredient18.get() != "":
                listingredient.append(entryingredient18.get())
                listamount.append(entryingredient18amount.get())
        createlist()

        if listamount == ['']:
            tkinter.messagebox.showerror(message="Please Check Ingredient Amount")
            return

        listamountfinal1 = []
        print(listamount)
        for i in listamount:
            listamountfinal1.append(float(i))

        listamountfinal = sum(listamountfinal1)

        ingredientlist = []
        for i in listingredient:
            conn = sqlite3.connect("PriceList.db")
            c = conn.cursor()
            c.execute("SELECT  Price FROM prices WHERE Productname like ?", (i,))
            records = c.fetchall()
            if records == []:
                tkinter.messagebox.showerror(message="Please Check Ingredient Name")
                return
            a = records[0]
            b = (a[0])
            ingredientlist.append(b)

        recipeamount = [float(a)*float(b) for a,b in zip(ingredientlist,listamount)]


        recipeamountfinal2 = sum(recipeamount) / listamountfinal
        recipeamountfinal1 = recipeamountfinal2 * ((listamountfinal/int(entryrendementofrecipe.get())))
        if entryrendementoffilling.get() == "":
            tkinter.messagebox.showerror(message="Please Check Filling Machine Rendemet")
            return
        recipeamountfinal = round(recipeamountfinal1 / ((int(entryrendementoffilling.get())/100)),4) #After rendements final recipe.
        recipepriceeffect = []
        for i in recipeamount:
            recipepriceeffect.append((i / listamountfinal))
        recipefinaleffectf = []
        for i in recipepriceeffect:
            recipefinaleffectf.append(round(((i/recipeamountfinal2)*100),2))

        witheffect = zip(listingredient,recipefinaleffectf)
        recipewitheffect = dict(witheffect) #ingridienteffect of price
        print(recipewitheffect[listingredient[0]])
        # Packagingcalculate
        listiPackaging = []
        def createlist1():
            if entryPackaging1.get() != "":
                listiPackaging.append(entryPackaging1.get())
            if entryPackaging2.get() != "":
                listiPackaging.append(entryPackaging2.get())
            if entryPackaging3.get() != "":
                listiPackaging.append(entryPackaging3.get())
            if entryPackaging4.get() != "":
                listiPackaging.append(entryPackaging4.get())
        createlist1()

        Packagingprice = []
        for i in listiPackaging:
            conn = sqlite3.connect("PriceList.db")
            c = conn.cursor()
            c.execute("SELECT  Price FROM prices WHERE Productname like ?", (i,))
            records = c.fetchall()
            a = records[0]
            b = (a[0])
            Packagingprice.append(b)

        Packagingpricelast = []
        for i in Packagingprice:
            a = i * ((100 + int(entrylostambalag.get()))/100)
            Packagingpricelast.append(a)
        if entryPackaginginproduct.get() == "":
            tkinter.messagebox.showerror(message="Please Check Product Amount Per Packaging")
            return
        finalPackagingprice = round(sum(Packagingpricelast)/float(entryPackaginginproduct.get()),2)

        #calculatecarton
        listicarton = []

        def createlist2():
            if entrycarton1.get() != "":
                listicarton.append(entrycarton1.get())
            if entrycarton2.get() != "":
                listicarton.append(entrycarton2.get())
        createlist2()
        cartonprice = []
        for i in listicarton:
            conn = sqlite3.connect("PriceList.db")
            c = conn.cursor()
            c.execute("SELECT  Price FROM prices WHERE Productname like ?", (i,))
            records = c.fetchall()

            a = records[0]
            b = (a[0])
            cartonprice.append(b)

        cartonpricelast = []
        for i in cartonprice:
            a = i * ((100 + int(entrylostambalag.get())) / 100)
            cartonpricelast.append(a)
        if entryPackaginginCarton.get() == "":
            tkinter.messagebox.showerror(message="Please Check Packaging in Carton")
            return
        finalcartonprice1 = round(sum(cartonpricelast) / float(entryPackaginginCarton.get()), 2)
        finalcartonprice = finalcartonprice1/float(entryPackaginginproduct.get())

        #pallet calculator

        palletname = []
        palletprice = []
        if entrypallet.get() == "":
            palletprice.append(0)
        else:
            palletname.append(entrypallet.get())

        for i in palletname:
            conn = sqlite3.connect("PriceList.db")
            c = conn.cursor()
            c.execute("SELECT  Price FROM prices WHERE Productname like ?", (i,))
            records = c.fetchall()
            if records == []:
                palletprice.append(1)
            else:
                a = records[0]
                b = (a[0])
                palletprice.append(b)

        palletpricelast = []
        for i in palletprice:
            if entrylostambalag.get() == "":
                tkinter.messagebox.showerror(message="Please Check Theoretical Loss Amount for carton and Packaging")
                return
            a = i * ((100 + int(entrylostambalag.get())) / 100)
            palletpricelast.append(a)
        finalpallet1 = round(sum(palletpricelast) / float(entryamballageinPallet.get()), 2)

        finalpaletprice = finalpallet1 / float(entryPackaginginproduct.get())

        Packagingpricefinal = round((finalPackagingprice + finalcartonprice + finalpaletprice),2)


        listallrecipe = listingredient + listiPackaging +listicarton+palletname
        strlistallrecipe = ','.join(str(e) for e in listallrecipe)

        #calculate manpower
        if entrylabelmanpower.get() == "" or entrydaymanpower.get() == "":
            tkinter.messagebox.showerror(message="Please Check Manpower Calculation")
            return
        awp = float(entrylabelmanpower.get()) * float(entrydaymanpower.get())
        mwp = float(awp)

        if entryworkersalary.get() == "" or entrylineleadersalary.get() == "" or entryshiftleadersalary.get() == "":
            tkinter.messagebox.showerror(message="Please Check Manpower Calculation")
            return
        worker = round((float(entryworkersalary.get()) / mwp), 2)
        linechef = round((float(entrylineleadersalary.get()) / mwp), 2)
        lineleader = round((float(entryshiftleadersalary.get()) / mwp), 2)

        if entryworkeramount.get() == "0":
            twrk = 0
        else:
            wmw = ((float(entryworkeramount.get()) * float(entrydaymanpower.get())) / mwp)*10
            twrk = round(((worker * wmw) /  float(entryrendementofrecipe.get())), 5)

        if entrychefamount.get() == "0":
            tllrk = 0
        else:
            llmw = ((float(entrychefamount.get()) * float(entrydaymanpower.get())) / mwp)*10
            tllrk = round(((linechef * llmw) / float(entryrendementofrecipe.get())), 5)
        if entryleaderamount.get() == "0":
            tslrk = 0
        else:
            slmw = ((float(entryleaderamount.get()) * float(entrydaymanpower.get())) / mwp)*10
            tslrk = round(((lineleader * slmw) / float(entryrendementofrecipe.get())), 5)

        manpowerprice = round((twrk + tllrk+tslrk),4)

        #enerrgycostcalculator
        if enryvapourquant.get() == "" or enryvapourprice.get() == "" or enrywaterquant.get() == "" or enrywaterprice.get() == "" or enryelectrquant.get() == "" or enryelectrprice.get() == "":
            tkinter.messagebox.showerror(message="Please Check Energy Calculation")
            return
        vaporprice = (float(enryvapourquant.get()) * float(enryvapourprice.get()) * 10) / float(
            entryrendementofrecipe.get())
        waterprice = (float(enrywaterquant.get()) * float(enrywaterprice.get()) * 10) / float(
            entryrendementofrecipe.get())
        electricprice = (float(enryelectrquant.get()) * float(enryelectrprice.get()) * 10) / float(
            entryrendementofrecipe.get())
        Energyprice = round((vaporprice+waterprice+electricprice),4)

        # Packagingpricefinal Packaging amount (Packaging,carton,pallet)
        # recipeamountfinal  recipe amount
        totalRecipeCost = (round((manpowerprice+Energyprice+Packagingpricefinal+recipeamountfinal),4))
        RecipeCostdict = {"Recipe Cost":recipeamountfinal,"Manpower Cost":manpowerprice,"Energy Cost":Energyprice,"Packaging Cost":Packagingpricefinal}
        totalRecipeCostperPackaging = round((totalRecipeCost*float(entryPackaginginproduct.get())),4)
        totalRecipeCostperpackwithoutpackaging = round(totalRecipeCostperPackaging - (Packagingpricefinal*float(entryPackaginginproduct.get())),4)

        # calculateRecipeCost---------------------------------------------------------------------------------------------

        #Graphics
        #find all recipe

        allrecipe = listingredient + listiPackaging + listicarton + palletname

        Currency = []
        Supplier = []
        for i in allrecipe:
            conn = sqlite3.connect("PriceList.db")
            c = conn.cursor()
            c.execute("SELECT Currency FROM prices WHERE Productname like ?", (i,))
            records = c.fetchall()

            a = records[0]
            b = (a[0])
            Currency.append(b)
        for i in allrecipe:
            conn = sqlite3.connect("PriceList.db")
            c = conn.cursor()
            c.execute("SELECT Supplier FROM prices WHERE Productname like ?", (i,))
            records = c.fetchall()

            a = records[0]
            b = (a[0])
            Supplier.append(b)

        #resultScreen
        def screenresult():
            RecipeCostresult = tk.ThemedTk()
            RecipeCostresult.get_themes()
            RecipeCostresult.set_theme("adapta")

            w = 1500
            h = 700
            ws = RecipeCostresult.winfo_screenwidth()
            hs = RecipeCostresult.winfo_screenheight()

            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)

            RecipeCostresult.geometry("%dx%d+%d+%d" % (w, h, x, y))
            RecipeCostresult.configure(background="#FFFFFF")
            RecipeCostresult.title("RecipeCost Result")
            labelproductname = ttk.Label(RecipeCostresult, text="Product Name:", font=("Helvetica", 10), background="#FFFFFF")
            labelproductname.place(x=30, y=30)
            labelproductnamer = ttk.Label(RecipeCostresult, text=productnameentry.get(), font=("Helvetica", 10), background="#FFFFFF")
            labelproductnamer.place(x=190, y=30)
            labeltlkg =ttk.Label(RecipeCostresult, text="Price/kg", font=("Helvetica", 10), background="#FFFFFF")
            labeltlkg.place(x=190, y=70)

            labelrawmaterial = ttk.Label(RecipeCostresult, text="Raw Material(Recipe)", font=("Helvetica", 10), background="#FFFFFF")
            labelrawmaterial.place(x=30, y=90)
            labelrawmaterialr = ttk.Label(RecipeCostresult, text=recipeamountfinal, font=("Helvetica", 10), background="#FFFFFF")
            labelrawmaterialr.place(x=190, y=90)

            labelmanpower = ttk.Label(RecipeCostresult, text="Manpower", font=("Helvetica", 10),
                                         background="#FFFFFF")
            labelmanpower.place(x=30, y=120)
            labelmanpowerr = ttk.Label(RecipeCostresult, text=manpowerprice, font=("Helvetica", 10),
                                          background="#FFFFFF")
            labelmanpowerr.place(x=190, y=120)

            labelpackaging= ttk.Label(RecipeCostresult, text="Packaging", font=("Helvetica", 10),
                                      background="#FFFFFF")
            labelpackaging.place(x=30, y=150)
            labelpackagingr = ttk.Label(RecipeCostresult, text=Packagingpricefinal, font=("Helvetica", 10),
                                       background="#FFFFFF")
            labelpackagingr.place(x=190, y=150)

            labelenergy = ttk.Label(RecipeCostresult, text="Energy", font=("Helvetica", 10),
                                       background="#FFFFFF")
            labelenergy.place(x=30, y=180)
            labelenergyr = ttk.Label(RecipeCostresult, text=Energyprice, font=("Helvetica", 10),
                                        background="#FFFFFF")
            labelenergyr.place(x=190, y=180)

            labelRecipeCost = ttk.Label(RecipeCostresult, text="Total RecipeCost", font=("Helvetica", 10),
                                    background="#FFFFFF")
            labelRecipeCost.place(x=30, y=210)
            labelRecipeCostr = ttk.Label(RecipeCostresult, text=totalRecipeCost, font=("Helvetica", 10),
                                     background="#FFFFFF")
            labelRecipeCostr.place(x=190, y=210)

            labelRecipeCostperpack = ttk.Label(RecipeCostresult, text="Total RecipeCost per Packaging", font=("Helvetica", 10),
                                    background="#FFFFFF")
            labelRecipeCostperpack.place(x=30, y=240)
            labelRecipeCostperpackr = ttk.Label(RecipeCostresult, text=totalRecipeCostperPackaging, font=("Helvetica", 10),
                                     background="#FFFFFF")
            labelRecipeCostperpackr.place(x=190, y=240)

            labelRecipeCostperpackwhpack = ttk.Label(RecipeCostresult, text="Total RecipeCost per Packaging \nwithout Packaging Amount", font=("Helvetica", 10),
                                        background="#FFFFFF")
            labelRecipeCostperpackwhpack.place(x=30, y=270)
            labelRecipeCostperpackwhpackr = ttk.Label(RecipeCostresult, text=totalRecipeCostperpackwithoutpackaging, font=("Helvetica", 10),
                                         background="#FFFFFF")
            labelRecipeCostperpackwhpackr.place(x=190, y=270)

            labelingredienteffectofrecipe = ttk.Label(RecipeCostresult, text="Ingredient Effect to Recipe Price (%)", font=("Helvetica", 10),
                                         background="#FFFFFF")
            labelingredienteffectofrecipe.place(x=45,y=330)


            ya= 360
            cd = 0
            for i in listingredient:
                labelingredienteffectofrecipe = ttk.Label(RecipeCostresult,text=listingredient[cd],font=("Helvetica", 10),
                                         background="#FFFFFF")
                labelingredienteffectofrecipe.place(x=30,y=ya)
                labelingredienteffectamount = ttk.Label(RecipeCostresult,text=recipewitheffect[listingredient[cd]],font=("Helvetica", 10),
                                         background="#FFFFFF")
                labelingredienteffectamount.place(x=200,y=ya)
                ya += 30
                cd +=1
            yb = 90
            cb = 0
            labeltlkg = ttk.Label(RecipeCostresult, text="Ingredient Name", font=("Helvetica", 10), background="#FFFFFF")
            labeltlkg.place(x=300, y=70)
            labeltlkg = ttk.Label(RecipeCostresult, text="Amount(kg)", font=("Helvetica", 10), background="#FFFFFF")
            labeltlkg.place(x=410, y=70)
            for i in listingredient:
                labelingredient = ttk.Label(RecipeCostresult,text=listingredient[cb],font=("Helvetica", 10),
                                         background="#FFFFFF")
                labelingredient.place(x=300,y=yb)
                labelingredientamount = ttk.Label(RecipeCostresult,text=listamount[cb],font=("Helvetica", 10),
                                         background="#FFFFFF")
                labelingredientamount.place(x=440,y=yb)
                yb += 30
                cb +=1

            def savedatabase():
                today = date.today()
                d1 = today.strftime("%d/%m/%Y")
                conn = sqlite3.connect("cvsdatabase.db")
                c = conn.cursor()
                c.execute(
                    "INSERT INTO cvsdatabase  VALUES (:e_date, :e_productname, :e_rwprice,:e_mnprice, :e_pckprice, :e_energyprice,:e_ttRecipeCost,:e_ttRecipeCostppck,:e_ttRecipeCostpwpck,:e_recipeall)",

                    {

                        "e_date": d1,
                        "e_productname": productnameentry.get(),
                        "e_rwprice":recipeamountfinal,
                        "e_mnprice": manpowerprice,
                        "e_pckprice": Packagingpricefinal,
                        "e_energyprice": Energyprice,
                        "e_ttRecipeCost": totalRecipeCost,
                        "e_ttRecipeCostppck": totalRecipeCostperPackaging,
                        "e_ttRecipeCostpwpck": totalRecipeCostperpackwithoutpackaging,
                        "e_recipeall": strlistallrecipe


                    }

                    )

                conn.commit()
                conn.close()

                def savepng():
                    name = productnameentry.get()+".png"
                    im = ImageGrab.grab((30, 140, 1900, 1000))
                    im.save(name)

                savepng()
                time.sleep(2)
                messagebox.showinfo(title="Record Successful", message="Record Successful")


            savebutton = ttk.Button(RecipeCostresult,text="Save Recipe Cost to Database",width=30,command=savedatabase)
            savebutton.place(x=350 ,y=600)

            #graphics
            def currencypiechart():


                fig = Figure(figsize=(3.5, 3.5),
                             dpi=100)

                y = Counter(Currency)

                plt = fig.add_subplot()
                counts = Counter(Currency)
                plt.set_title("Currencies affecting the Recipe", fontsize=8)
                plt.pie([v for v in counts.values()], labels=[k for k in counts],
                           autopct='%1.1f%%', shadow=True,textprops={'fontsize': 8})
                fig.set_facecolor('white')


                canvas = FigureCanvasTkAgg(fig,
                                           master=RecipeCostresult)
                canvas.draw()


                canvas.get_tk_widget().place(x=600,y=20)

            def supplierpiechart():
                fig = Figure(figsize=(3.5, 3.5),
                             dpi=100)

                y = Counter(Supplier)


                plt = fig.add_subplot()

                counts = Counter(Supplier)

                plt.set_title("Supplier the Recipe", fontsize=8)
                plt.pie([v for v in counts.values()], labels=[k for k in counts],
                           autopct='%1.1f%%', shadow=True,textprops={'fontsize': 8})
                fig.set_facecolor('white')

                canvas = FigureCanvasTkAgg(fig,
                                           master=RecipeCostresult)
                canvas.draw()

                canvas.get_tk_widget().place(x=600,y=350)

            #def theoricpriceperkg():
                #   counteuro = Currency.count("EURO")
                #   countusd = Currency.count("USD")
                #   countcountr = Currency.count("TL")
                #   a = (0.8*counteuro)+(0.5*countusd)+(0.2*countcountr)
                #    figprice = [totalRecipeCost,(totalRecipeCost+a),(totalRecipeCost+(2*a)),(totalRecipeCost+(3*a)),(totalRecipeCost+(4*a)),(totalRecipeCost+(5*a))]
                #   x = [0,1,2,3,4,5]
                #   y = figprice
                #   fig = Figure(figsize=(3.5, 3.5),
                #                dpi=100)

                #  plt = fig.add_subplot(111)

                #  plt.set_title("KG RecipeCost Change with 1 Euro increment per year", fontsize=8)
                # plt.plot(x,y,color='#0066FF')
                #  fig.set_facecolor('white')
                #  canvas = FigureCanvasTkAgg(fig,
                #                          master=RecipeCostresult)
                # canvas.draw()
                #canvas.get_tk_widget().place(x=700, y=20)
            #def theoricpriceperpack():

                #   counteuro = Currency.count("EURO")
                #   countusd = Currency.count("USD")

                #  a = (0.8*counteuro)+(0.5*countusd)
                #  figprice = [totalRecipeCostperPackaging,(totalRecipeCostperPackaging+a),(totalRecipeCostperPackaging+(2*a)),(totalRecipeCostperPackaging+(3*a)),(totalRecipeCostperPackaging+(4*a)),(totalRecipeCostperPackaging+(5*a))]
                #  x = [0,1,2,3,4,5]
                #  y = figprice
                # fig = Figure(figsize=(3.5, 3.5),
                #               dpi=100)

                #  plt = fig.add_subplot(111)

                # plt.set_title("Change of RecipeCost of the package according to Annual Euro Increase", fontsize=8)
                # plt.plot(x,y,color='#0066FF')
                #fig.set_facecolor('white')
                #canvas = FigureCanvasTkAgg(fig,
                #                           master=RecipeCostresult)
                # canvas.draw()
                #canvas.get_tk_widget().place(x=1050, y=350)

            def RecipeCostpiechart():

                fig = Figure(figsize=(3.5, 3.5),
                             dpi=100)


                plt = fig.add_subplot()

                plt.set_title("Price Effect For RecipeCost", fontsize=8)
                plt.pie([v for v in RecipeCostdict.values()], labels=[k for k in RecipeCostdict.keys()],
                           autopct='%1.1f%%', shadow=True,textprops={'fontsize': 8})
                fig.set_facecolor('white')


                canvas = FigureCanvasTkAgg(fig,
                                           master=RecipeCostresult)
                canvas.draw()

                canvas.get_tk_widget().place(x=1050,y=350)

            def ingredientpiechart():
                fig = Figure(figsize=(3.5, 3.5),
                             dpi=100)

                y = Counter(recipewitheffect)
                print(y)

                plt = fig.add_subplot()

                counts = Counter(recipewitheffect)
                plt.set_title("Effect Of Ingredient Price To Recipe", fontsize=8)
                plt.pie([v for v in counts.values()], labels=[k for k in counts],
                        autopct='%1.1f%%', shadow=True,textprops={'fontsize': 8})
                fig.set_facecolor('white')

                canvas = FigureCanvasTkAgg(fig,
                                           master=RecipeCostresult)
                canvas.draw()

                canvas.get_tk_widget().place(x=1050, y=20)

            ingredientpiechart()
            RecipeCostpiechart()
            #theoricpriceperpack()
            #theoricpriceperkg()
            supplierpiechart()
            currencypiechart()


        screenresult()






    xplace = 30
    yplace = 70
    xamplace = 230


    labelproductname =ttk.Label(RecipeCostcalculator, text="Product Name", font=("Helvetica", 10), background="#f0f0f0")
    labelproductname.place(x=30,y=10)
    productnameentry = ttk.Entry(RecipeCostcalculator, width=35)
    productnameentry.place(x=120,y=5)



    Label1 = ttk.Label(RecipeCostcalculator, text="Recipe", font=("Helvetica", 10), background="#f0f0f0")
    Label1.place(x=120, y=35)
    labelname = ttk.Label(RecipeCostcalculator, text="Ingredient Name", font=("Helvetica", 10), background="#f0f0f0")
    labelname.place(x=82, y=50)
    labelname = ttk.Label(RecipeCostcalculator, text="Amount", font=("Helvetica", 10), background="#f0f0f0")
    labelname.place(x=230, y=50)

    labelrecipeinformation = ttk.Label(RecipeCostcalculator, text="Information About Recipe", font=("Helvetica", 10), background="#f0f0f0")
    labelrecipeinformation.place(x=450, y=50)
    labelrendementofrecipe = ttk.Label(RecipeCostcalculator, text="Rendement of Recipe(kg)\n DefaultValue: 1000", font=("Helvetica", 10),
                                       background="#f0f0f0")
    labelrendementofrecipe.place(x=300, y=75)
    entryrendementofrecipe = ttk.Entry(RecipeCostcalculator,width=5)
    entryrendementofrecipe.insert(END, "1000")

    entryrendementofrecipe.place(x=455, y=75)
    labelrendementofrecipe = ttk.Label(RecipeCostcalculator, text="Rendement of \nFilling Machine(%)",
                                       font=("Helvetica", 10),
                                       background="#f0f0f0")
    labelrendementofrecipe.place(x=300, y=120)
    entryrendementoffilling = ttk.Entry(RecipeCostcalculator, width=5)


    entryrendementoffilling.place(x=455, y=120)

    labelPackaginginproduct = ttk.Label(RecipeCostcalculator, text="Product Amount \nPer One Package (kg)",
                                       font=("Helvetica", 10),
                                       background="#f0f0f0")
    labelPackaginginproduct.place(x=300, y=175)

    entryPackaginginproduct = ttk.Entry(RecipeCostcalculator, width=5)

    entryPackaginginproduct.place(x=455, y=175)

    labelPackaginginCarton = ttk.Label(RecipeCostcalculator, text='Packaging in Carton(pcs)',
                                       font=("Helvetica", 10),
                                       background="#f0f0f0")
    labelPackaginginCarton.place(x=300, y=230)
    entryPackaginginCarton = ttk.Entry(RecipeCostcalculator, width=5)

    entryPackaginginCarton.place(x=455, y=230)

    labelCartoninPallet = ttk.Label(RecipeCostcalculator, text="Packaging in Pallet(pcs)",
                                       font=("Helvetica", 10),
                                       background="#f0f0f0")
    labelCartoninPallet.place(x=300, y=260)
    entryamballageinPallet = ttk.Entry(RecipeCostcalculator, width=5)

    entryamballageinPallet.place(x=455, y=260)

    labellostambalag = ttk.Label(RecipeCostcalculator, text="Theoretical loss amounts for\n"
                                                        "carton and packaging (%)",
                                    font=("Helvetica", 10),
                                    background="#f0f0f0")
    labellostambalag.place(x=500, y=75)
    entrylostambalag = ttk.Entry(RecipeCostcalculator, width=5)

    entrylostambalag.place(x=670, y=80)


    #Recipeentrys
    entryingredient1 = ttk.Entry(RecipeCostcalculator,width=30)
    entryingredient1.place(x=xplace,y=yplace)
    entryingredient1amount = ttk.Entry(RecipeCostcalculator,width=5)
    entryingredient1amount.place(x=xamplace,y=yplace)

    entryingredient2 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient2.place(x=xplace, y=yplace+30)
    entryingredient2amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient2amount.place(x=xamplace, y=yplace+30)

    entryingredient3 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient3.place(x=xplace, y=yplace+60)
    entryingredient3amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient3amount.place(x=xamplace, y=yplace + 60)

    entryingredient4 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient4.place(x=xplace, y=yplace+90)
    entryingredient4amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient4amount.place(x=xamplace, y=yplace + 90)

    entryingredient5 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient5.place(x=xplace, y=yplace+120)
    entryingredient5amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient5amount.place(x=xamplace, y=yplace + 120)

    entryingredient6 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient6.place(x=xplace, y=yplace+150)
    entryingredient6amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient6amount.place(x=xamplace, y=yplace + 150)

    entryingredient7 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient7.place(x=xplace, y=yplace+180)
    entryingredient7amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient7amount.place(x=xamplace, y=yplace + 180)

    entryingredient8 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient8.place(x=xplace, y=yplace + 210)
    entryingredient8amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient8amount.place(x=xamplace, y=yplace + 210)

    entryingredient9 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient9.place(x=xplace, y=yplace + 240)
    entryingredient9amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient9amount.place(x=xamplace, y=yplace + 240)

    entryingredient10 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient10.place(x=xplace, y=yplace + 270)
    entryingredient10amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient10amount.place(x=xamplace, y=yplace + 270)

    entryingredient11 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient11.place(x=xplace, y=yplace + 300)
    entryingredient11amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient11amount.place(x=xamplace, y=yplace + 300)

    entryingredient12 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient12.place(x=xplace, y=yplace + 330)
    entryingredient12amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient12amount.place(x=xamplace, y=yplace + 330)

    entryingredient13 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient13.place(x=xplace, y=yplace + 360)
    entryingredient13amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient13amount.place(x=xamplace, y=yplace + 360)

    entryingredient14 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient14.place(x=xplace, y=yplace + 390)
    entryingredient14amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient14amount.place(x=xamplace, y=yplace + 390)

    entryingredient15 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient15.place(x=xplace, y=yplace + 420)
    entryingredient15amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient15amount.place(x=xamplace, y=yplace + 420)

    entryingredient16 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient16.place(x=xplace, y=yplace + 450)
    entryingredient16amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient16amount.place(x=xamplace, y=yplace + 450)

    entryingredient17 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient17.place(x=xplace, y=yplace + 480)
    entryingredient17amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient17amount.place(x=xamplace, y=yplace + 480)

    entryingredient18 = ttk.Entry(RecipeCostcalculator, width=30)
    entryingredient18.place(x=xplace, y=yplace + 510)

    entryingredient18amount = ttk.Entry(RecipeCostcalculator, width=5)
    entryingredient18amount.place(x=xamplace, y=yplace + 510)

    #informationaboutPackaging
    labelPackaging = ttk.Label(RecipeCostcalculator, text="Enter Product Amballage\n(Without Carton and Pallet)", font=("Helvetica", 10), background="#f0f0f0")
    labelPackaging.place(x=320, y=yplace + 230)
    entryPackaging1 = ttk.Entry(RecipeCostcalculator, width=30)
    entryPackaging1.place(x=300, y=yplace + 270)
    entryPackaging2 = ttk.Entry(RecipeCostcalculator, width=30)
    entryPackaging2.place(x=300, y=yplace + 300)
    entryPackaging3 = ttk.Entry(RecipeCostcalculator, width=30)
    entryPackaging3.place(x=300, y=yplace + 330)
    entryPackaging4 = ttk.Entry(RecipeCostcalculator, width=30)
    entryPackaging4.place(x=300, y=yplace + 360)


    #productcartonandlabel
    labelcarton = ttk.Label(RecipeCostcalculator, text="Enter Product Carton and Label",
                            font=("Helvetica", 10), background="#f0f0f0")
    labelcarton.place(x=300, y=yplace +390)
    entrycarton1 = ttk.Entry(RecipeCostcalculator, width=30)
    entrycarton1.place(x=300, y=yplace + 420)
    entrycarton2 = ttk.Entry(RecipeCostcalculator, width=30)
    entrycarton2.place(x=300, y=yplace + 450)

    labelcarton = ttk.Label(RecipeCostcalculator, text="Enter Product Pallet",
                            font=("Helvetica", 10), background="#f0f0f0")
    labelcarton.place(x=330, y=yplace + 485)
    entrypallet = ttk.Entry(RecipeCostcalculator, width=30)
    entrypallet.place(x=300, y=yplace + 510)

    #information about manpower

    Manpowercalculation = ttk.Label(RecipeCostcalculator, text="Manpower Calculation",
                            font=("Helvetica", 12), background="#f0f0f0")
    Manpowercalculation.place(x=600,y=150)
    labelmanpower = ttk.Label(RecipeCostcalculator, text="Enter Daily Working Hour\n"
                                                  "without Timeout",
                            font=("Helvetica", 10), background="#f0f0f0")
    labelmanpower.place(x=500, y=180)
    entrylabelmanpower = ttk.Entry(RecipeCostcalculator, width=5)

    entrylabelmanpower.place(x=670, y=180)

    labelmanpower = ttk.Label(RecipeCostcalculator, text="Worker Amount in Line",
                              font=("Helvetica", 10), background="#f0f0f0")
    labelmanpower.place(x=500, y=260)
    entryworkeramount = ttk.Entry(RecipeCostcalculator, width=5)

    entryworkeramount.place(x=670, y=260)

    labelmanpower = ttk.Label(RecipeCostcalculator, text="Line Chef Amount in Line",
                              font=("Helvetica", 10), background="#f0f0f0")
    labelmanpower.place(x=500, y=290)
    entrychefamount = ttk.Entry(RecipeCostcalculator, width=5)

    entrychefamount.place(x=670, y=290)

    labelmanpower = ttk.Label(RecipeCostcalculator, text="Line Leader Amount in Line",
                              font=("Helvetica", 10), background="#f0f0f0")
    labelmanpower.place(x=500, y=320)
    entryleaderamount = ttk.Entry(RecipeCostcalculator, width=5)

    entryleaderamount.place(x=670, y=320)



    labelmanpower = ttk.Label(RecipeCostcalculator, text="Enter Worker Salary\n"
                                                  "with all social right",
                              font=("Helvetica", 10), background="#f0f0f0")
    labelmanpower.place(x=720, y=180)
    entryworkersalary = ttk.Entry(RecipeCostcalculator, width=10)

    entryworkersalary.place(x=870, y=180)

    labelmanpower = ttk.Label(RecipeCostcalculator, text="Enter Line Chef Salary\n"
                                                  "with all social right",
                              font=("Helvetica", 10), background="#f0f0f0")
    labelmanpower.place(x=720, y=230)
    entrylineleadersalary = ttk.Entry(RecipeCostcalculator, width=10)

    entrylineleadersalary.place(x=870, y=230)

    labelmanpower = ttk.Label(RecipeCostcalculator, text="Enter Shift Leader Salary\n"
                                                  "with all social right",
                              font=("Helvetica", 10), background="#f0f0f0")
    labelmanpower.place(x=720, y=280)
    entryshiftleadersalary = ttk.Entry(RecipeCostcalculator, width=10)

    entryshiftleadersalary.place(x=870, y=280)

    labelmanpower = ttk.Label(RecipeCostcalculator, text="Enter Monthly Working Day",
                              font=("Helvetica", 10), background="#f0f0f0")
    labelmanpower.place(x=500, y=230)
    entrydaymanpower = ttk.Entry(RecipeCostcalculator, width=5)

    entrydaymanpower.place(x=670, y=230)



    #energy cost,

    energycostcalculator = ttk.Label(RecipeCostcalculator, text="Energy Cost Calculation",
                                    font=("Helvetica", 12), background="#f0f0f0")
    energycostcalculator.place(x=600, y=350)

    energycostcalculator = ttk.Label(RecipeCostcalculator, text="Vapour Quantity (kg)",
                                     font=("Helvetica", 10), background="#f0f0f0")
    energycostcalculator.place(x=500, y=380)

    enryvapourquant = ttk.Entry(RecipeCostcalculator,width=10)

    enryvapourquant.place(x=670, y=380)

    energycostcalculator = ttk.Label(RecipeCostcalculator, text="Vapour Price per Unit",
                                    font=("Helvetica", 10), background="#f0f0f0")
    energycostcalculator.place(x=500, y=410)

    enryvapourprice = ttk.Entry(RecipeCostcalculator, width=10)

    enryvapourprice.place(x=670, y=410)

    energycostcalculator = ttk.Label(RecipeCostcalculator, text="Electric Quantity (Kw)",
                                     font=("Helvetica", 10), background="#f0f0f0")
    energycostcalculator.place(x=750, y=380)

    enryelectrquant = ttk.Entry(RecipeCostcalculator, width=10)

    enryelectrquant.place(x=890, y=375)

    energycostcalculator = ttk.Label(RecipeCostcalculator, text="Electric Price per Unit",
                                     font=("Helvetica", 10), background="#f0f0f0")
    energycostcalculator.place(x=750, y=415)

    enryelectrprice = ttk.Entry(RecipeCostcalculator, width=10)

    enryelectrprice.place(x=890, y=400)

    energycostcalculator = ttk.Label(RecipeCostcalculator, text="Water Quantity (m3)",
                                     font=("Helvetica", 10), background="#f0f0f0")
    energycostcalculator.place(x=500, y=440)

    enrywaterquant = ttk.Entry(RecipeCostcalculator, width=10)

    enrywaterquant.place(x=670, y=440)

    energycostcalculator = ttk.Label(RecipeCostcalculator, text="Water Price per Unit",
                                     font=("Helvetica", 10), background="#f0f0f0")
    energycostcalculator.place(x=500, y=470)



    enrywaterprice = ttk.Entry(RecipeCostcalculator, width=10)

    enrywaterprice.place(x=670, y=470)

    def ingredientlist():


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
        ingredientlist = tk.ThemedTk()
        ingredientlist.get_themes()
        ingredientlist.set_theme("adapta")

        w = 1180
        h = 650
        ws = ingredientlist.winfo_screenwidth()
        hs = ingredientlist.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        ingredientlist.geometry("%dx%d+%d+%d" % (w, h, x, y))
        ingredientlist.title("Price List")
        tree = ttk.Treeview(ingredientlist, columns=(
        "ID", "Category", "Type", "Product Name", "Supplier", "Price/Unit", "Currency", "Conversion to TL"),
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
        tree.heading("#8", text="Conversion to TL")
        tree.column("#8", minwidth=0, width=100)
        tree.place(x=0, y=0)
        ingredientlist.command(view())

    butoncalculateRecipeCost = ttk.Button(RecipeCostcalculator, width=70, text="Ingredient List", command=ingredientlist)
    butoncalculateRecipeCost.place(x=500, y=530)

    butoncalculateRecipeCost = ttk.Button(RecipeCostcalculator, width=70, text="Calculate RecipeCost", command=calculateRecipeCost)
    butoncalculateRecipeCost.place(x=500, y=570)

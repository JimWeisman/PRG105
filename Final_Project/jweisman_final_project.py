"""
final step 1
jim weismamn
python
spring 2019
"""

import tkinter
import tkinter.messagebox


tk = tkinter

class MarketGui:
    def __init__(self,):
        self.main_window = tkinter.Tk()
        self.main_window.title("The Olive Tap, Crystal Lake")

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.middletwo_frame = tkinter.Frame(self.main_window)
        self.middlethree_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

    # Product 1
        self.canvas = tkinter.Canvas(self.top_frame,  width=300, height=155)
        #self.pop = tkinter.Canvas(self.main_window)
        self.image1 = tkinter.PhotoImage(file='Flavor_Infused_Oils.gif')
        self.canvas.create_image(200, 50, image=self.image1)
        self.canvas.pack(side = 'left')

    #Product 2
        self.canvas = tkinter.Canvas(self.middle_frame, width=300, height=160)
        #self.pop = tkinter.Canvas(self.main_window)
        self.image2 = tkinter.PhotoImage(file='You_Pick_4.gif')
        self.canvas.create_image(200, 75, image=self.image2)
        self.canvas.pack(side = 'left')

    #Product 3
        self.canvas = tkinter.Canvas(self.middletwo_frame, width=300, height=150)
        #self.pop = tkinter.Canvas(self.main_window)
        self.image3 = tkinter.PhotoImage(file='bigstock-Blood-Oranges_100x100px.gif')
        self.canvas.create_image(200, 75, image=self.image3)
        self.canvas.pack(side = 'left')

    #Product 4
        self.canvas = tkinter.Canvas(self.middlethree_frame, width=300, height=150)
        #self.pop = tkinter.Canvas(self.main_window)
        self.image4 = tkinter.PhotoImage(file='Fresh_Italian_Herbs.gif')
        self.canvas.create_image(200, 75, image=self.image4)
        self.canvas.pack(side = 'left')


        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb_var8 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        self.cb_var8.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame,text='Spicy Tuscan Olive Oil - Small $9.95', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,text='Spicy Tuscan Olive Oil - Large $19.95', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.middle_frame, text='Small You Pick 4 100 ml. Sampler Set at $36.50', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.middle_frame, text = 'Large You Pick 8 100 ml. Sampler Set at $72.50', variable = self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.middletwo_frame, text='Small Blood Orange Olive Oil at $8.95', variable= self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.middletwo_frame, text=' large Blood Orange Olive Oil at $18.95', variable= self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.middlethree_frame, text='Small Italian Herbs Riserva Balsamic Vinegar at 9.95',variable=self.cb_var7)
        self.cb8 = tkinter.Checkbutton(self.middlethree_frame, text='Large Italian Herbs Riserva Balsamic Vinegar at 19.95',variable=self.cb_var8)

        self.cb1.pack(anchor='w')
        self.cb2.pack(anchor='w')
        self.cb3.pack(anchor='w')
        self.cb4.pack(anchor='w')
        self.cb5.pack(anchor='w')
        self.cb6.pack(anchor='w')
        self.cb7.pack(anchor='w')
        self.cb8.pack(anchor='w')

        self.ok_button = tkinter.Button(self.bottom_frame, text='ok', command=self.total)
        self.quit_button = tkinter.Button(self.bottom_frame, text='quit', command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.middletwo_frame.pack()
        self.middlethree_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def total(self):
        self.outputText = ('your total is \n' + 'Results')
        self.total = 0.0

        if self.cb_var1.get() == 1:
            self.total += 9.95
        if self.cb_var2.get() == 1:
            self.total += 19.95
        if self.cb_var3.get() == 1:
            self.total += 36.50
        if self.cb_var4.get() == 1:
            self.total += 72.50
        if self.cb_var5.get() == 1:
            self.total += 8.85
        if self.cb_var6.get() == 1:
            self.total += 18.95
        if self.cb_var7.get() == 1:
            self.total += 9.95
        if self.cb_var8.get() == 1:
            self.total += 19.95



        self.value = tkinter.StringVar()
        self.results_label = tkinter.Label(self.middle_frame, text='Results: ')
        self.results = tkinter.Label(self.middle_frame, textvariable=self.total)
        tkinter.messagebox.showinfo('your total $', self.total)
        #self.results = outputText('the amount you owe is $' + self.total)


button = MarketGui()

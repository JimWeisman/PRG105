"""
jim weisman
python
spring 2019 @ mcc
"""
import tkinter
import tkinter.messagebox


tk = tkinter

class MarketGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("The Olive Tap, Crystal Lake")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        #self.grid = tkinter.Frame(self.main_window)

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

        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Spicy Tuscan Olive Oil at $18.95', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Jalapeño Habanero Olive Oil at $19.95', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Leek Agrumato Olive Oil at $19.95', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text = 'Red Apple White Balsamic Vinegar at $18.95', variable = self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='You Pick 4 100 ml. Sampler Set at $36.50',variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='Blood Orange Olive Oil at $18.95', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='Italian Herbs Riserva Balsamic Vinegar at $19.95',variable=self.cb_var7)
        self.cb8 = tkinter.Checkbutton(self.top_frame, text='Ascolano 100% Extra Virgin Olive Oil-Award Winner! at $20.95',variable=self.cb_var8)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        self.cb8.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text='ok', command=self.total)
        self.quit_button = tkinter.Button(self.bottom_frame, text='quit', command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def total(self):
        self.message = 'your total is \n'
        self.total = 0.0

        if self.cb_var1.get() == 1:
            self.total += 18.95
        if self.cb_var2.get() == 1:
            self.total += 19.95
        if self.cb_var3.get() == 1:
            self.total += 19.95
        if self.cb_var4.get() == 1:
            self.total += 18.95
        if self.cb_var5.get() == 1:
            self.total += 36.50
        if self.cb_var6.get() == 1:
            self.total += 18.95
        if self.cb_var7.get() == 1:
            self.total += 19.95
        if self.cb_var8.get() == 1:
            self.total += 20.95

        tkinter.messagebox.showinfo('selection', self.total)


button = MarketGui()

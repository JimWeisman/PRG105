import tkinter
import tkinter.messagebox
import pickle


# main (root) GUI menu
class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)

        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        elif self.radio_var.get() == 2:
            _ = AddGUI(self.master)
        elif self.radio_var.get() == 3:
            _ = ChangGUI(self.master)
        elif self.redio_var.get() == 4
            _ = Delete(self.master)
        else:
            DeleteGUI(self.master, self.input_file)

class ChangGUI:
    def __init__(self, master):
         try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
         except (FileNotFoundError, IOError):
            self.customers = {}

         self.change = tkinter.Toplevel(master)
         self.change.title('change customer email')

        #varibles
         self.statusVar = tkinter.StringVar()
         self.statusVar.set ('uncheck')
         self.currentVar = tkinter.StringVar()
         self.currentVar.set ('empty')
         self.currentName = tkinter.StringVar()a
         self.currentName.set ('empty')

        # serach frame
         self.search_frame = tkinter.Frame(self.change)
         self.search_frame_label = tkinter.Label(self.search_frame, text = 'entry customer name to change')
         self.search_frame_entry = tkinter.Entry(self.search_frame, width = 25)
         self.search_frame_label.pack(side = 'left')
         self.search_frame_entry.pack(side = 'right')
         self.search_frame.pack(side = 'top')

        # serach button frame
         self.search_button_frame = tkinter.Frame(self.change)
         self.search_button = tkinter.Button(self.search_button_frame, text = 'check', command = self.check)
         self.search_button.pack(side = 'top')
         self.search_button_frame.pack(side = 'top')
         #self.search_frame_entry.pack(side = 'top') #not sure what this is

        #locate frame
         self.locate_frame = tkinter.Frame(self.change)
         self.result_label = tkinter.Label(self.locate_frame, text = 'record status')
         self.status_label = tkinter.Label(self.locate_frame, textvariable = self.statusVar)
         self.result_label.pack(side = 'left')
         self.result_frame.pack(side = 'right')
         self.locate_frame.pack(side = 'top')

    def check(self):
        return


class AddGUI:
    def __init__(self, master):
         try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
         except (FileNotFoundError, IOError):
            self.customers = {}

         self.addGUI = tkinter.Toplevel(master)
         self.addGUI.title('add customer data')

         self.name_frame = tkinter.Frame(self.addGUI)
         self.email_frame = tkinter.Frame(self.addGUI)
         self.botton_frame = tkinter.Frame(self.addGUI)

         self.add_name_Label = tkinter.Label(self.name_frame, text = 'customer name')
         self.add_name_enrty = tkinter.Entry(self.name_frame, width = 25)

         self.add_name_Label.pack(side = 'left')
         self.add_name_enrty.pack(side = 'left')
         self.name_frame.pack(side = 'top')

         self.add_email_label = tkinter.Label(self.email_frame, text = 'customer email')
         self.add_email_entry = tkinter.Entry(self.email_frame, width = 25)

         self.add_email_label.pack(side = 'left')
         self.add_email_entry.pack(side = 'left')
         self.email_frame.pack(side = 'top')

         self.add_button = tkinter.Button(self.botton_frame, text = 'add', command = self.addbut)
         self.back_button = tkinter.Button(self.botton_frame, text = 'main menu', command = self.back)

         self.add_button.pack(side = 'left')
         self.back_button.pack(side ='right')
         self.botton_frame.pack(side = 'top')

    def addbut(self):
        name = self.add_name_enrty.get()
        email = self.add_email_entry.get()
        self.customers[name] = email
        tkinter.messagebox.showinfo('success', 'data enterd')


    def back(self):
        out_file = open ("customer_file.dat", 'wb')
        pickle.dump(self.customers, out_file)
        out_file.close()
        self.addGUI.destroy()



class LookGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        #current record fame
        self.current_frame = tkinter.Frame(self.change)
        self.current_Label =  tkinter.Label(self.current_frame, text = 'current entry')
        self.current_name_Label  = tkinter.Label(self.current_frame, textvarible = self.current.Name)
        self.current_data_Label  = tkinter.Label(self.current_frame, textvarible = self.current.Var)
        self.change_label.pack(side = 'top')
        self.current_name_Label.pack(side = 'let')
        self.current_data_Label.pack(side = 'right')
        self.current_frame.pack(side = 'top')


        #change frame
        self.change_frame = tkinter.Frame(self.change)
        self.change_label = tkinter.Label(self.change_frame, text = 'new email')
        self.change_entry = tkinter.Entry(self.change_frame, width = 25)
        self.change_label.pack(side = 'left')
        self.change_entry.pack(side = 'right')
        self.change_frame.pack(side = 'top')

        #button frame
        self.button_frame = tkinter.Frame(self.change)
        self.change_button = tkinter.Button(self.button_frame, text ='change', command = self.changeBut)
        self.back_button = tkinter.Button(self.button_frame, text = 'back', command = self.back)
        self.button_frame.pack(side = 'left')
        self.change_button.pack(side = 'right')
        self.back_button.pack(side = 'top')

    def check (self):
        name = self.search_frame_entry.get()
        result = self.customers.get(name, 'not found')

        if result == 'not found':
            self.statusVar.set('not found')
            self.currentVar.set ('not found')
            self.currentName.set
        else:
            self.statusVar.set('record found')
            self.currentVar.set (name)
            self.currentName.set (result)


    def changeBut(self):
        new = self.change_entry.get()
        name = self.search_frame_entry.get()
        self.customers[name] = new
        self.statusVar.set = ('change')
        self.currentVarset(new)


    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    # use _ as variable name because the variable will not be needed after instantiating GUI
    # the GUI itself will handles the remaining program logic
    _ = CrudGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()

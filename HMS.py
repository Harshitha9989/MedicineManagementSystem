import tkinter as tk
import sys
from tkinter import Frame,Button,Label,Entry,PhotoImage,Text,WORD,Toplevel
import re
from PIL import ImageTk, Image
window=tk.Tk()
window.title('MEDICINE MANAGEMENT SYSTEM')
window.configure(bg='#00ff00')
frame=Frame(window)
Medicine_id=0

f=open("Medicine_file.txt",'r+')
for line in f:
    Medicine_id+=1

img = ImageTk.PhotoImage(Image.open("Medicine.jpg"))

background_label = tk.Label(parent, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def win1():
    top=Toplevel()
    top.title('Insert Medicine Details')
    key=Create(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='black',bg='yellow')
    button.place(x=42,y=340)
    top.mainloop()

def win2():
    top = Toplevel()
    top.title('Search Medicine')
    key = Search(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='black',bg='yellow')
    button.place(x=42,y=170)
    top.mainloop()
def win3():
    top = Toplevel()
    top.title('Delete Medicine')
    key = Delete(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='black',bg='yellow')
    button.place(x=42,y=170)
    top.mainloop()

def win4():
    top = Toplevel()
    top.title('Edit Medicine Details')
    key = Edit(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='black',bg='white')
    button.place(x=50,y=300)
    top.mainloop()

def win5():
    top = Toplevel()
    top.title('Display Medicine Details')
    key = Display(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='black',bg='white')
    button.place(x=450,y=340)
    top.mainloop()



button1=Button(height=2,width=30,bg="red")
button1['text']='Insert Medicine Details'
button1['command']=win1
button1.place(x=100,y=90)

button1=Button(height=2,width=30,bg="blue")
button1['text']='Search Medicine'
button1['command']=win2
button1.place(x=200,y=180)

button1=Button(height=2,width=30,bg="pink")
button1['text']='Delete Medicine'
button1['command']=win3
button1.place(x=300,y=270)

button1=Button(height=2,width=30,bg="yellow")
button1['text']='Edit Medicine'
button1['command']=win4
button1.place(x=400,y=360)

button1=Button(height=2,width=30,bg="white")
button1['text']='Display Medicines'
button1['command']=win5
button1.place(x=500,y=450)

class Create(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.bikname = Label(self)
        self.bikname['text']='Enter Medicine Name:'
        self.bikname.grid(column=0,row=3)
        self.bname=Entry(self)
        self.bname.grid(column=0,row=4)
        self.bokcomp = Label(self)
        self.bokcomp['text'] = 'Enter Medicine Company:'
        self.bokcomp.grid(column=0,row=5)
        self.bcomp = Entry(self)
        self.bcomp.grid(column=0,row=6)
        self.bikorigin = Label(self)
        self.bikorigin['text'] = 'Enter Medicine Origin:'
        self.bikorigin.grid(column=0, row=9)
        self.borigin = Entry(self)
        self.borigin.grid(column=0, row=10)
        self.bikprice = Label(self)
        self.bikprice['text'] = 'Enter Medicine Price:'
        self.bikprice.grid(column=0,row=7)
        self.bprice = Entry(self)
        self.bprice.grid(column=0,row=8)
        self.button = Button(self)
        self.button['text']='Submit'
        self.button['command']=self.get_data
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=11, column=9)
        self.button.grid(column=0,row=15)
    def get_data(self):
        global Medicine_id
        Medicinedetails=get_Medicine_details()
        Medicinename = self.bname.get()
        MedicineIndex = search_Medicine(Medicinedetails, Medicinename)
        if MedicineIndex>=0:
            self.msg.insert(0.0, "Medicine already exists:")
        else:
            Medicine_id =Medicine_id+ 1
            f = open('Medicine_file.txt', 'a+')
            f.write("{Medicine_id}|{bname}|{bcomp}|{borigin}|{bprice}$\n".format(Medicine_id=Medicine_id, bname=self.bname.get(), bcomp=self.bcomp.get(), borigin=self.borigin.get(), bprice=self.bprice.get()))
            self.msg.insert(0.0, "your Medicine id is:" + str(Medicine_id ))
        print('success')

class Search(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.bikname = Label(self)
        self.bikname['text'] = 'Enter Medicine Name:'
        self.bikname.grid(column=0, row=1)
        self.bname = Entry(self)
        self.bname.grid(column=0, row=2)
        self.button = Button(self)
        self.button['text'] = 'Search'
        self.button['command'] = self.search_Medicine
        self.button.grid(column=0, row=11)
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.grid(row=3, column=1)
    def search_Medicine(self):
        global Medicine_id
        Medicinedetails = get_Medicine_details()
        bname = self.bname.get()
        self.msg.delete('1.0', tk.END)
        MedicineIndex = search_Medicine(Medicinedetails, bname)
        if(MedicineIndex >= 0):
            self.msg.insert(0.0, "Medicine name is: " + bname + "\nyour Medicine id is:" + str(Medicinedetails[MedicineIndex][0]) + '\n')
        else:
            self.msg.insert(0.0, "rec not found"'\n')

class Delete(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.bikname = Label(self)
        self.bikname['text'] = 'Enter Medicine Name:'
        self.bikname.grid(column=0, row=1)
        self.bname = Entry(self)
        self.bname.grid(column=0, row=2)
        self.button = Button(self)
        self.button['text'] = 'Delete'
        self.button['command'] = self.delete_Medicine
        self.button.grid(column=0, row=11)
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.grid(row=3, column=1)
    def delete_Medicine(self):
        global Medicine_id
        Medicinedetails = get_Medicine_details()
        bname = self.bname.get()
        self.msg.delete('1.0', tk.END)
        MedicineIndex = search_Medicine(Medicinedetails, bname)
        if MedicineIndex >= 0:
            del Medicinedetails[MedicineIndex]
            Medicine_id-=1
            save_Medicine_data(Medicinedetails)
            self.msg.insert(0.0, "Medicine deleted"'\n')
        else:
            self.msg.insert(0.0, "Medicine not found"'\n')
        return

def get_Medicine_details():
    f = open("Medicine_file.txt", 'r').read()
    f = re.split("[" + "\\".join("$\\n") + "]", f)[:-2]
    f = filter(None, f)
    MedicineDetails = [re.split("[" + "\\".join("|") + "]", Medicine) for Medicine in f]
    return MedicineDetails

def save_Medicine_data(Medicine_details):
    Medicine_details.append([])
    s="$\n".join(['|'.join(Medicines) for Medicines in Medicine_details])
    savefile=open("Medicine_file.txt", 'w')
    savefile.write(s)
    return s

def search_Medicine(Medicinedetails, bname):
    MedicineIndex = -1
    for index, Medicines in enumerate(Medicinedetails):
        if bname == Medicines[1]:
            MedicineIndex = index
    return MedicineIndex

class Edit(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.bikname = Label(self)
        self.bikname['text'] = 'Enter Medicine Name:'
        self.bikname.grid(column=0, row=1)
        self.bname = Entry(self)
        self.bname.grid(column=0, row=2)
        self.button = Button(self)
        self.button['text']='edit'
        self.button['command']=self.edit_widgets
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=12, column=1)
        self.button.grid(column=0, row=13)
    def edit_widgets(self):
        self.bokcomp = Label(self)
        self.bokcomp['text'] = 'Enter Medicine Company:'
        self.bokcomp.grid(column=0, row=5)
        self.bcomp = Entry(self)
        self.bcomp.grid(column=0, row=6)
        self.bikorigin = Label(self)
        self.bikorigin['text'] = 'Enter Medicine Origin:'
        self.bikorigin.grid(column=0, row=9)
        self.borigin = Entry(self)
        self.borigin.grid(column=0, row=10)
        self.bikprice = Label(self)
        self.bikprice['text'] = 'Enter Medicine Price:'
        self.bikprice.grid(column=0, row=7)
        self.bprice = Entry(self)
        self.bprice.grid(column=0, row=8)
        self.button = Button(self)
        self.button['text'] = 'Edit'
        self.button['command'] = self.get_data
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=12, column=1)
        self.button.grid(column=0, row=13)
    def get_data(self):
        global Medicine_id
        Medicinedetails = get_Medicine_details()
        bname = self.bname.get()
        self.msg.delete('1.0', tk.END)
        MedicineIndex = search_Medicine(Medicinedetails, bname)
        if (MedicineIndex >= 0):
            Medicinedetails[MedicineIndex] = [str(Medicine_id),self.bname.get(),self.bcomp.get(), self.borigin.get(), self.bprice.get()]
            save_Medicine_data(Medicinedetails)
            print(Medicinedetails)
            self.msg.insert(0.0, "the Medicine record edited is:" + str(Medicine_id))
        else:
            self.msg.insert(0.0, "rec not found"'\n')

def list_to_json(Medicine_details):
    Medicine_details_json = []
    for Medicine in Medicine_details:
        MedicineObj = {}
        MedicineObj['id'] = Medicine[0]
        MedicineObj['bname'] = Medicine[1]
        MedicineObj['bcomp'] = Medicine[2]
        MedicineObj['borigin'] = Medicine[3]
        MedicineObj['bprice'] = Medicine[4]
        Medicine_details_json.append(MedicineObj)
    return Medicine_details_json

def json_to_str_table(Medicine_details):
    table_content = "ID\t\tMedicine_Name\t\tMedicine_Company\t\tMedicine_Origin\t\tMedicine_Price\n"
    for Medicine in Medicine_details:
        table_content += "{Medicine_id}\t\t{bname}\t\t{bcomp}\t\t{borigin}\t\t{bprice}\n".format(Medicine_id=Medicine['id'],bname=Medicine['bname'], bcomp=Medicine['bcomp'], borigin=Medicine['borigin'], bprice=Medicine['bprice'])
    return table_content

class Display(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.msg = Text(self, width=90, height=10, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=12, column=1)
        self.msg['command']=self.display_Medicines()
    def display_Medicines(self):
        global Medicine_id
        Medicinedetails = get_Medicine_details()
        Medicinedetails=list_to_json(Medicinedetails)
        Medicinedetails=json_to_str_table(Medicinedetails)
        self.msg.insert(0.0, "the Medicine record details are: \n\n" + str(Medicinedetails)+'\n')

window.mainloop()

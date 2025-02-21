
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import string
import random
import time
from datetime import datetime
# from tkcalendar import DateEntry



root=Tk()
root.geometry('300x600+400+10')
root.title('Get Password')
root.config(background='#c6c2c3')

wel=ttk.Label(root,text='Welcom',anchor='center',foreground='blue',background='#6c6c6c',font=('Arial Greek',20,'bold'))
wel.pack(fill=X)


label_1=ttk.Label(root,text='Enter the len namber for get your password :',background='#c1c2c3')
label_1.place(x=27,y=70)

entry_1=Entry(root,width=30,justify='center')
entry_1.place(x=30,y=100)

# cal1=DateEntry(root, width=12)
# cal1.place(x=150,y=300)


label_2=Label(root,text='',width=26)
label_2.place(x=30,y=250)

stayl=ttk.Style()
stayl.configure('TButton',background='blue')

button_1=Button(root,text='√ Get my password',padx=1,pady=1)
button_1.place(x=30,y=150)

button_2=Button(root,text='Save Password')
button_2.place(x=30,y=300)

app_date = datetime.now()
x_date = app_date.strftime('%Y-%m-%d')
#  x_time = app_date.strftime('%H:%M:%S')

date_lbl =ttk.Label(root,text='Date : '+x_date,background='#c1c2c3',foreground='#E8FEFF',font=('Arial Greek',10,'bold'))
date_lbl.place(x=10,y=40)

time_label=ttk.Label(root,background='#c1c2c3',foreground='#E8FEFF',font=('Arial Greek',10,'bold'))
time_label.place(x=150,y=40)

def app_time(): 
    string = time.strftime('%H:%M:%S %p') 
    time_label.config(text ='Time : '+string)
    root.after(1000, app_time)
app_time()

Var_0 = StringVar()

def Get_Password():
    entry_namber='{}'.format(entry_1.get())
    try:
        entrynamber=int(entry_namber)
        if entrynamber >= 6:
            s1=list(string.ascii_lowercase)
            s2=list(string.ascii_uppercase)
            s3=list(string.digits)
            s4=list(string.punctuation)
            random.shuffle(s1)
            random.shuffle(s2)
            random.shuffle(s3)
            random.shuffle(s4)
            p1=round(entrynamber * 40/100)
            p2=round(entrynamber * 10/100)
            Password=[]
            for i in range(p1):
                Password.append(s1[i])
                Password.append(s2[i])
            for i in range(p2):
                Password.append(s3[i])
                Password.append(s4[i])
            random.shuffle(Password)
            Password1=''.join(Password[0:])
            label_2.config(text=Password1)
            Var_0.set(Password1)
            entry_1.delete(0,'end')

        else:
            label_2.config(text='')
            messagebox.showerror(title='Error',message='Your Nomber is not Enaf to get Password')
            entry_1.delete(0,'end')
    except:
        label_2.config(text='')
        messagebox.showerror(title='Error',message='plase enter only namber of Password len!')
        entry_1.delete(0,'end')

class db_Conect :
    def __init__(self):
        self.db=sqlite3.connect('Password Data.db')
        self.db.row_factory=sqlite3.Row
        self.db.execute('create table if not exists P_Data (Password text,Pass_id INTEGER primary key autoincrement ,Time text)')
        self.db.commit()
    def Add(self,Password,Time):
        self.db.execute('insert into P_Data(Password,Time) values(?,?)',(Password,Time))
        self.db.commit()
    def Data_Select(self):
        curser=self.db.execute('select * from P_Data')
        return curser ;

dbConect=db_Conect()

filter_date_frm =LabelFrame(root,width=280,height=210,bg='#c1c2c3',bd=3,fg='blue',text='Data Save')
filter_date_frm.place(x=10,y=380)

def Table():
    scroll_y=Scrollbar(filter_date_frm,orient=VERTICAL)
    scroll_y.place(x=258,y=2,width=13,height=186)

    TV=ttk.Treeview(filter_date_frm)
    TV.place(x=2,y=2)
    TV.config(columns=('#1','#2'),height=8,yscrollcommand=scroll_y.set)
    TV.heading('#0',text='ID')
    TV.heading('#1',text='Password')
    TV.heading('#2',text='Time')
    TV.column('#0',width=50)
    TV.column('#1',width=135)
    TV.column('#2',width=69)

    scroll_y.config(command=TV.yview)

    cor=dbConect.Data_Select()
    for row in cor:
        TV.insert('','end','#{}'.format(row['Pass_id']),text=row['Pass_id'])
        TV.set('#{}'.format(row['Pass_id']),'#1',row['Password'])
        TV.set('#{}'.format(row['Pass_id']),'#2',row['Time'])

Table()

def Save_B():
    var_0='{}'.format(Var_0.get())
    if var_0 == '' :
        messagebox.showerror(title='error',message='Get Password ferst')
    else:
        dbConect.Add(var_0,'{}'.format(x_date))
        label_2.config(text='')
        Var_0.set('')
        messagebox.showinfo(title='info',message='Password Saved')
        Table()
   
def light_theme():
    root.config(background='#c1c2c3') 
    filter_date_frm.config(background='#c1c2c3')
    label_1.config(background='#c1c2c3',foreground='black')
    date_lbl.config(background='#c1c2c3')
    time_label.config(background='#c1c2c3')
    wel.config(background='#6c6c6c')
    entry_1.config(background='white')
    button_1.config(background='white')
    button_2.config(background='white')
    label_2.config(background='white')
    style=ttk.Style()
    style.theme_use('vista')
    style.configure('Treeview', background='white',foreground='black',rowheight=21,)
    style.map('Treeview', background=[('selected','blue')])

def Darck_theme():   
    root.config(background='#0d0225')
    filter_date_frm.config(background='#0d0225')
    label_1.config(background='#0d0225',foreground='white')
    date_lbl.config(background='#0d0225')
    time_label.config(background='#0d0225')
    wel.config(background='#0d0225')
    entry_1.config(background='#2D7A87')
    button_1.config(background='#2D7A87')
    button_2.config(background='#2D7A87')
    label_2.config(background='#2D7A87')
    style=ttk.Style()
    style.theme_use('default')
    style.configure('Treeview', background='#0d0225',foreground='white',rowheight=21)
    style.map('Treeview', background=[('selected','green')])
 



menubarr =Menu(root)
root.config(menu=menubarr)

file_menu =Menu(menubarr,tearoff=0,border=1,cursor='hand2',disabledforeground='red',bg='#cecece',fg='blue',relief=RAISED,activebackground='red',activeforeground='white',activeborderwidth=0)
menubarr.add_cascade(label = "Themes", menu = file_menu)
file_menu.add_command(label = "Light Mode",command=light_theme)
file_menu.add_command(label = "Darck Mode",command=Darck_theme)



button_1.config(command=Get_Password)
button_2.config(command=Save_B)




root.mainloop()

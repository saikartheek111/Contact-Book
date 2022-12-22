import csv

def add(i):
    with open('d://data.csv','a+',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)

def view():
    data = []
    with open('d://data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data

def remove(i):

    def save(j):
        with open('d://data.csv','w',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(j)

    new_list=[]
    telephone=i

    with open('d://data.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element==telephone:
                    new_list.remove(row)
    save(new_list)
def update(i):
    def update_newlist(j):
        with open('d://data.csv','w',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(j)
    new_list=[]
    telephone=i[0]

    with open('d://data.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element==telephone:
                    name=i[1]
                    gender=i[2]
                    telephone=i[3]
                    email=i[4]
                    age=i[5]
                    hobbies=i[6]
                    data=[name,gender,telephone,email,age,hobbies]
                    index=new_list.index(row)
                    new_list[index]=data
    update_newlist(new_list)

def search(i):
    data=[]
    telephone=i

    with open('d://data.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            for element in row:
                if element==telephone:
                    data.append(row)
    print(data)
    return data
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#colors
co0 = '#494623'
co1 = '#c3892b'
co2 = '#8e883d'

console = Tk()
console.title("")
console.geometry('700x530')#window size
console.configure(background='white')
console.resizable(width=True,height=True)
#frames
frame_up = Frame(console,width=670,height=50,bg=co0)
frame_up.grid(row=0,column=0,padx=0,pady=1)#grid used to position the widget

frame_down = Frame(console,width=670,height=220,bg=co2)
frame_down.grid(row=1,column=0,padx=0,pady=1)

frame_table = Frame(console,width=2600,height=100,bg='white',relief='solid')
frame_table.grid(row=2,column=0, columnspan=2,padx=8,pady=0,sticky=NW)

#functions
def show():
    global tree
         
    listheader = ['Name','Relation','Number','Email','Age','Hobbies']

    demo_list = view()
    
    tree = ttk.Treeview(frame_table,selectmode = "extended",columns = listheader,show="headings")
    
    vsb = ttk.Scrollbar(frame_table,orient = 'vertical', command =tree.yview)
    hsb = ttk.Scrollbar(frame_table,orient="horizontal",command=tree.xview)
        
    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
    
    tree.grid(column=0,row=0, sticky = 'nsew')
    vsb.grid(column=1,row=0, sticky = 'ns')
    hsb.grid(column=0,row=1,sticky = 'ew')
    
    #tree listhead
    tree.heading(0,text='Name',anchor=NW)
    tree.heading(1,text='Relation',anchor=NW)
    tree.heading(2,text='Number',anchor=NW) 
    tree.heading(3,text='Email',anchor=NW)
    tree.heading(4,text = 'Age',anchor=NW)
    tree.heading(5,text='Hobbies',anchor=NW)
    
     
     #tree columns
    tree.column(0,width=150,anchor='nw')
    tree.column(1,width=60,anchor='nw')
    tree.column(2,width=80,anchor='nw')
    tree.column(3,width=200,anchor='nw')
    tree.column(4,width=50,anchor='nw')
    tree.column(5,width=130,anchor='nw')
    
    for i in demo_list:
        tree.insert('','end',values=i)
     
show()

def insert():
    name = e_name.get()
    Relation = c_relation.get()
    number = e_number.get()
    email = e_email.get()
    email=email.lower()
    age = c_age.get()
    hobbies=c_hobbies.get()

    data = [name,Relation,number,email,age,hobbies]

    if name == '' or Relation=='' or number==''or email=='' or  age=='' or hobbies=='':
        messagebox.showwarning('data','Please fill all fields')
    elif name.isalpha()==False:
        messagebox.showwarning('data','Please enter name with alphabets Only')
    elif number.isnumeric()==False or len(number)!=10:
        messagebox.showwarning('data','Please enter Valid Phone Number with 10 numbers')
    else:
        add(data)
        messagebox.showinfo('data','data added successfully')
        e_name.delete(0,'end')
        c_relation.delete(0,'end')
        e_number.delete(0,'end')
        e_email.delete(0,'end')
        c_age.delete(0,'end')
        c_hobbies.delete(0,'end')

        show()

def to_edit():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        name = str(tree_list[0])
        relation = str(tree_list[1])
        number = str(tree_list[2])
        email = str(tree_list[3])
        age = str(tree_list[4])
        hobbies = str(tree_list[5])

        e_name.insert(0,name)
        c_relation.insert(0,relation)
        e_number.insert(0,number)
        e_email.insert(0,email)
        c_age.insert(0,age)
        c_hobbies.insert(0,hobbies)

        def confirm():
            new_name = e_name.get()
            new_relation = c_relation.get()
            new_number = e_number.get()
            new_email = e_email.get()
            new_age = c_age.get()
            new_hobbies= c_hobbies.get()

            data = [new_number,new_name,new_relation,new_number,new_email,new_age,new_hobbies]

            update(data)
            messagebox.showinfo('success','data edited succesfully')

            e_name.delete(0,'end')
            c_relation.delete(0,'end')
            e_number.delete(0,'end')
            e_email.delete(0,'end')
            c_age.delete(0,'end')
            c_hobbies.delete(0,'end')

            for widget in frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()
        b_confirm = Button(frame_down,text= 'confirm',width=15,height=1,bg=co1,fg=co0,font = ('Ivy 10 bold'),command=confirm)
        b_confirm.place(x=290,y=110)
    except IndexError:
        messagebox.showerror('Error','Select one of them from the table')

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_number = str(tree_list[2])

        remove(tree_number)

        messagebox.showinfo('success','data has beeen deleted successfully')

        for widget in frame_table.winfo_children():
            widget.destroy()

        show()
    except IndexError:
        messagebox.showerror('Error','Select one of them from the table')

def to_search():
    number = e_search.get()

    data = search(number)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('', 'end',values = item) 
    e_search.delete(0,'end')

#frame_up widgets
app_name = Label(frame_up,text = 'CONTACT BOOK',height=1,font=('italic 19 bold'),bg ='#ffffff' ,fg = co2)
app_name.place(x=220,y=5)

#frame_down widgets
l_name = Label(frame_down,text = "Name  ",width=7,height=1,font=('Ivy,10'),bg='#c3892b',anchor=NW)
l_name.place(x=10,y=20)
e_name = Entry(frame_down,width=25,justify='left',highlightthickness=1,relief='solid')
e_name.place(x=80,y=20)

l_relation = Label(frame_down,text = "Relation ",width=7,height=1,font=('Ivy,10'),bg='#c3892b',anchor=NW)
l_relation.place(x=10,y=50)
c_relation = ttk.Combobox(frame_down,width=23)
c_relation['values']=['Friend','Family','Work','Others']
c_relation.place(x=80,y=50)

a = []
for i in range(1,101):
    a.append(i)
l_age = Label(frame_down,text='Age',width=6,height=1,font=('Ivy,10'),bg=co1)
l_age.place(x=10,y=140)
c_age = ttk.Combobox(frame_down,width=7)
c_age['values'] = a
c_age.place(x=70,y=140)

l_hobbies = Label(frame_down,text='Hobbies',width=7,height=1,font=('Ivy,10'),bg=co1)
l_hobbies.place(x=150,y=142)
c_hobbies = ttk.Combobox(frame_down,width=18)
c_hobbies['values']=['Art/Craft','Cooking','Dance','Music','Playing Games','Reading','Travel','TV/Mobile','Writing','Watching Movies','Others']
c_hobbies.place(x=220,y=142)

l_number = Label(frame_down,text = "Number  ",width=7,height=1,font=('Ivy,10'),bg='#c3892b',anchor=NW)
l_number.place(x=10,y=80)
e_number = Entry(frame_down,width=25,justify='left',highlightthickness=1,relief='solid')
e_number.place(x=80,y=80)

l_email = Label(frame_down,text = "Email  ",width=7,height=1,font=('Ivy,10'),bg='#c3892b',anchor=NW)
l_email.place(x=10,y=110)
e_email = Entry(frame_down,width=25,justify='left',highlightthickness=1,relief='solid')
e_email.place(x=80,y=110)

b_search = Button(frame_down,text= 'Search',width=15,height=1,bg=co1,fg=co0,font = ('Ivy 10 bold'),command=to_search)
b_search.place(x=290,y=20)
e_search = Entry(frame_down,width=13,justify='left',font=('Ivy,11'),highlightthickness=1,relief='solid')
e_search.place(x=450,y=20)

b_view = Button(frame_down,text= 'View All',width=15,height=1,bg=co1,fg=co0,font = ('Ivy 10 bold'),command=show)
b_view.place(x=290,y=50)

b_add = Button(frame_down,text= 'Add',width=15,height=1,bg=co1,fg=co0,font = ('Ivy 10 bold'),command=insert)
b_add.place(x=450,y=50)

b_update = Button(frame_down,text= 'Edit',width=15,height=1,bg=co1,fg=co0,font = ('Ivy 10 bold'),command=to_edit)
b_update.place(x=450,y=80)

b_delete = Button(frame_down,text= 'Delete',width=15,height=1,bg=co1,fg=co0,font = ('Ivy 10 bold'),command=to_remove)
b_delete.place(x=450,y=110)

console.mainloop()
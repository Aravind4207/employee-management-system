from re import search

from customtkinter import *
from PIL import Image
from customtkinter import CTkFrame
from tkinter import ttk,messagebox
import database


#functions

def delete_all():
    result=messagebox.askyesno('confirm','do you really want to delete all the records?')
    if result:
        database.deleteall_records()
    else:
        pass


def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchbox.set('Search By')

def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('error', 'enter value to search')
    elif searchbox.get()=='Search By':
        messagebox.showerror('error','please select an option')
    else:
        searched_data=database.search(searchbox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('',END,values=employee)






def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('error', 'select data to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('error', ' data is deleted')



def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('error','select data to update')
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('success','data is updated')


def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        rolebox.set(row[3])
        genderbox.set(row[4])
        salaryEntry.insert(0, row[5])


def clear(value=False):
        if value:
            tree.selection_remove(tree.focus())
        idEntry.delete(0,END)
        nameEntry.delete(0,END)
        phoneEntry.delete(0,END)
        rolebox.set('Web developer')
        genderbox.set('Male')
        salaryEntry.delete(0,END)

def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)


def add_employee():

    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('error','All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('error', 'Id already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('error', 'Invalid ID format.Use "EMP" followed by a number(e.g., "EMP1").')

    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('success','data is added')


#GUI part
window=CTk()
window.geometry('1068x580+100+100')
window.resizable(False,False)
window.title('employee management system')
window.configure(fg_color='#07042A')
logo=CTkImage(Image.open('bg.png'),size=(1068,158))
logolabel=CTkLabel(window,image=logo,text='')
logolabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(window,fg_color='#07042A')
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text='Id',font=('arial',18,'bold'),text_color='white')
idLabel.grid(row=0,column=0,padx=(20),pady=15,sticky='w')
idEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180,fg_color='white',text_color='#000000')
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=(20),pady=15,sticky='w')
nameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180,fg_color='white',text_color='#000000')
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text='Phone',font=('arial',18,'bold'),text_color='white')
phoneLabel.grid(row=2,column=0,padx=(20),pady=15,sticky='w')
phoneEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180,fg_color='white',text_color='#000000')
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text='role',font=('arial',18,'bold'),text_color='white')
roleLabel.grid(row=3,column=0,padx=(20),pady=15,sticky='w')
role_options=['Web Developer','Cloud Architect','Technical Writer','Network Engineer','Data Scientist','Business Analyst','IT consultant','UX/UI Designer','DevOps Engineer']
rolebox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'),state='readonly',fg_color='white',text_color='#000000')
rolebox.grid(row=3,column=1,padx=20,pady=15,sticky='w')
rolebox.set(role_options[0])

genderLabel=CTkLabel(leftFrame,text='Gender',font=('arial',18,'bold'),text_color='white')
genderLabel.grid(row=4,column=0,padx=(20),pady=15,sticky='w')
gender_options=['Male','Female']
genderbox=CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',15,'bold'),state='readonly',fg_color='white',text_color='#000000')
genderbox.grid(row=4,column=1,padx=20,pady=15,sticky='w')
genderbox.set(gender_options[0])

salaryLabel=CTkLabel(leftFrame,text='Salary',font=('arial',18,'bold'),text_color='white')
salaryLabel.grid(row=5,column=0,padx=(20),pady=15,sticky='w')
salaryEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180,fg_color='white',text_color='#000000')
salaryEntry.grid(row=5,column=1,padx=(20),pady=15,sticky='w')


rightFrame=CTkFrame(window,fg_color='#C7D4FA')
rightFrame.grid(row=1,column=1)

search_options=['Id','Name','Phone','Role','Gender','Salary']
searchbox=CTkComboBox(rightFrame,values=search_options,width=184,font=('arial',15,'bold'),state='readonly',fg_color='white',text_color='#000000')
searchbox.grid(row=0,column=0)
searchbox.set('Search By')

searchEntry=CTkEntry(rightFrame,fg_color='white',text_color='#000000')
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFrame,text='Show All',width=100,command=show_all)
showallButton.grid(row=0,column=3)


tree=ttk.Treeview(rightFrame,height=17)
tree.grid(row=1,column=0,columnspan=4)
tree['column']=('Id','Name','Phone','Role','Gender','Salary')
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('Id',width=140)
tree.column('Name',width=180)
tree.column('Phone',width=140)
tree.column('Role',width=180)
tree.column('Gender',width=100)
tree.column('Salary',width=130)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',15,'bold'))
style.configure('Treeview',font=('arial',13,'bold'),rowheight=20,background='#07042A',foreground='white')

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(window,fg_color='#07042A')
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda:clear(True))
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

DeleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
DeleteButton.grid(row=0,column=3,pady=5,padx=5)

DeleteAllButton=CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
DeleteAllButton.grid(row=0,column=4,pady=5,padx=5)

treeview_data()

window.bind('<ButtonRelease>',selection)








window.mainloop()

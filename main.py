from customtkinter import *
from PIL import Image
from customtkinter import CTk
from  tkinter import messagebox


def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('error','all fields are required')
    elif usernameEntry.get()=='aravind' and  passwordEntry.get()=='1234':
        messagebox.showerror('sucess','login is successful')
        root.destroy()
        import ems

    else:
        messagebox.showerror('erorr','wrong username and password')



#this a CTkinter creating
root=CTk()
root.geometry('930x478')
root.resizable(False,False)
root.title('login page')
image=CTkImage(Image.open('ems.jpg'),size=(930,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='employee management system',bg_color='#F9F9F9',text_color='dark blue',font=('Goudy old style',20,'bold'))
headinglabel.place(x=20,y=100)
#username creating
usernameEntry=CTkEntry(root,placeholder_text='Enter your username',width=180,bg_color='#F9F9F9')
usernameEntry.place(x=50,y=150)
#password creating
passwordEntry=CTkEntry(root,placeholder_text='Enter your password',width=180,bg_color='#F9F9F9' ,show='*')
passwordEntry.place(x=50,y=200)
#login button created
login_button = CTkButton(master=root, text="Login",bg_color='#F9F9F9',cursor='hand2',command=login)
login_button.place(x=70,y=250)

root.mainloop()

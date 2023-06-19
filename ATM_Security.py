from tkinter import *
from tkinter import messagebox
import subprocess

security = Tk()
security.configure(bg="aqua")
security.title("Security")
pin = 'aditya'
def submit():
    if p.get() == pin:
        messagebox.showinfo("information","Permission Granted")
        security.destroy()
        # Run the other script
        subprocess.run(["python", "D:\Python Projects\ATM\ATM_Menu.py"])
                
    elif p.get() == (None or ""):
        messagebox.showwarning("Warning","Please Enter Password")
    else:
        messagebox.showerror("Error","Invalid password !")

security.maxsize(800,500)
security.minsize(800,400)
msg = Label(security, text = " ATM Service Authentication ", fg = "blue", font=('Times New Roman', 20, 'bold'),padx=100)
msg.pack(side = TOP)
securitys = Label(security, text="password",bg="aqua", fg = "green", font=("arial",15))
securitys.place(x=340,y=170)
p = StringVar()
password = Entry(security,show="*",justify="center",fg="red",font=("arial",14,"bold"),width=20,textvariable=p)
password.place(x=270,y=200)
submit = Button(security,text="submit",command=submit, width=10, fg="white", font=(
            'arial', 15, 'bold'), bg="orange",activeforeground="red", activebackground="pink").place(x=320,y=300)

security.mainloop()

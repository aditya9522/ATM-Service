from tkinter import *
from tkinter import messagebox
import time
import cx_Oracle
from datetime import datetime

nowd = datetime.now()
cdate = nowd.strftime("%d-%m-%y")
ctime = nowd.strftime("%H:%M:%S")

root = Tk()
frame = Frame(root,bg="steel blue", bd=20)
frame.pack(side=LEFT,fill="y")
current = DoubleVar()
pino = StringVar()
pino.set("aditya")

def historyb():
    his = Toplevel()
    his.geometry("700x600")
    his.title("History")
    his.configure(bg="aqua")
    top = Label(his, text="History", fg="red",width=20, bg="white", font=("arial", 20, 'bold')).pack(side=TOP)
    info = Label(his,text="Transaction Details ➡️", fg="purple", bg="aqua", font=("vardana", 15, 'bold')).place(x=40,y=80)
    con = cx_Oracle.connect("your connection url")
    cursor = con.cursor()
    cursor.execute("select * from atm_data")
    data = cursor.fetchall()
    lst = ["Date","Time","Withdrawals","Deposites","Balance"]
    n = 70
    for i in lst:
        lstd = Label(his,text=i, fg="black",width=9, bg="pink", font=("vardana", 15,"bold")).place(x=n,y=130)
        n = n+120
        
    a = 70
    b = 162
    for i in data:
        for j in i:
            data = Label(his,text=j, bg="white",width=9, fg="steel blue", font=("vardana", 15,"bold")).place(x=a,y=b)
            a = a+120
        b = b+32
        a = 70
    cursor.close()
    con.close() 
    his.mainloop()

def aboutb():
    ab = Toplevel()
    ab.geometry("700x450")
    ab.title("About")
    ab.configure(bg="aqua")
    top = Label(ab, text="About", fg="red",width=20, bg="white", font=("arial", 20, 'bold')).pack(side=TOP)
    left = Label(ab,text="ATM Services ➡️", fg="purple", bg="aqua", font=("vardana", 15, 'bold')).place(x=40,y=80)
    data = """               The ATM service is a system. Developed by aditya 
              Patel. The main goal of this system is to
              make easy transaction for the end user.By this user can easily
              interact with the system because we have provided a very 
              interactive and user friendly interface for the user and also
              provides consistency,durability & atomacity of the transaction,
              So the user will feel good experience with the system.
              Thak-You """
    lab1 = Label(ab, text=data, fg="black",bg="aqua", font=("Calibri", 15)).place(x=20,y=110)
    l2 = Label(ab,text="Technology used ➡️", fg="purple", bg="aqua", font=("Calibri", 15, 'bold')).place(x=40,y=330)
    l2 = Label(ab,text="* Python Programming\n* Tkinter\n* Oracle SQL ", fg="black", bg="aqua", font=("calibri", 15)).place(x=200,y=360)

    ab.mainloop()

def curb():
    con = cx_Oracle.connect("your connection url")
    cursor = con.cursor()
    cursor.execute("select current_balance from atm_data")
    dt = cursor.fetchall()
    avb = dt[-1][0]
    current.set(avb)
    cursor.close()
    con.close()

def balance():
    bal = Toplevel()
    bal.geometry("500x400")
    bal.title("Balance Check")
    bal.configure(bg="aqua")
    current_bal = StringVar()
    curb()
    def show():
        lb = Entry(bal, text=current_bal,bd=0 ,width=20, fg="purple", font=('vardana', 15, 'bold'), bg="aqua").place(x=300, y=250)
        b =  "{}/-".format(current.get())
        current_bal.set(b)

    top = Label(bal, text="Balance Inquiry", fg="red", bg="aqua", font=("arial", 20, 'bold'), pady=10).pack(side=TOP)
    lab = Label(bal, text="Account Information ►",fg="purple", bg="aqua", font=("arial", 15, 'bold')).place(x=10, y=110)
    balance1 = Label(bal, text="Your Account Number :       xxxxxxxxx786", fg="green", font=('ariel', 15, 'bold'), bg="aqua").place(x=80, y=150)
    balance = Button(bal, text="Show", width=10, fg="white", font=('ariel', 15, 'bold'), bg="blue", command=show).place(x=180, y=200)
    lab1 = Label(bal, text="Available amount :     ₹", fg="green",bg="aqua", font=("arial", 15, 'bold')).place(x=80, y=250)
    
    bal.mainloop()


def exit():
    root.destroy()

def deposite():
    dep = Toplevel()
    dep.geometry("600x400")
    dep.title("Deposite")
    dep.configure(bg="aqua")
    deposite_amount = DoubleVar()
    def submit():
        if (deposite_amount.get()).is_integer and deposite_amount.get() > 0.0:
            now = current.get() + deposite_amount.get()
            con = cx_Oracle.connect("your connection url")
            cursor = con.cursor()
            depa = deposite_amount.get()
            cursor.execute("insert into atm_data values(:tdate, :ttime, 0.0, :deposits, :current_balance)",(cdate, ctime, depa, now))
            con.commit()
            cursor.close()
            con.close()
            text = "₹{}/- successfully deposited.".format(deposite_amount.get())
            messagebox.showinfo("Information", text)
            dep.destroy()
        else:
            dep.destroy()
            messagebox.showwarning("Warning","Enter valid amount")

    top = Label(dep, text="Deposite Money", fg="red", bg="aqua",font=("arial", 20, 'bold'), pady=10).pack(side=TOP)
    lbl = Label(dep, text="Enter amount to Deposite »", font=('arial', 15, 'bold'), fg="blue", bg="aqua").place(x=50, y=100)
    entry = Entry(dep,textvariable=deposite_amount, width=20, fg="green", font=('arial', 15, 'bold'), bg="white").place(x=350, y=100)
    btn = Button(dep, text="submit", width=10, fg="white", font=('vardana', 15, 'bold'), bg="orange", command=submit).place(x=220, y=150)
    dep.mainloop()

def withdraw():
    withd = Toplevel()
    withd.geometry("600x400")
    withd.title("Withdraw")
    withd.configure(bg="aqua")
    withdraw_amount = DoubleVar()
    
    def submit2():
        if withdraw_amount.get() > current.get():
            withd.destroy()
            messagebox.showerror("Invalid Operation","You have not sufficient amount, Please Try Again!")
        elif withdraw_amount.get() == 0.0 or withdraw_amount.get().is_integer == False :
            withd.destroy()
            messagebox.showwarning("Warning","Enter valid amount")
        else:     
            now = current.get() - withdraw_amount.get()
            con = cx_Oracle.connect("your connection url")
            cursor = con.cursor()
            witha = withdraw_amount.get()
            cursor.execute("insert into atm_data values(:tdate, :ttime, :withdrawals, 0.0, :current_balance)",(cdate, ctime, witha, now))
            con.commit()
            cursor.close()
            con.close()
            txt = "₹{}/-  successfully Withdraw.".format(withdraw_amount.get())
            messagebox.showinfo("Information", txt)
            withd.destroy()

    top = Label(withd, text="Withdraw Money", fg="red", bg="aqua",font=("arial", 20, 'bold'), pady=10).pack(side=TOP)
    lbl = Label(withd, text="Enter amount to Withdraw »", font=( 'arial', 15, 'bold'), fg="blue", bg="aqua").place(x=50, y=100)
    entry = Entry(withd,textvariable=withdraw_amount, width=20, fg="green", font=('arial', 15, 'bold'), bg="white").place(x=350, y=100)
    btn = Button(withd, text="submit", width=10, fg="white", font=('arial', 15, 'bold'), bg="orange", command=submit2).place(x=220, y=150)
    withd.mainloop()

def changePin():
    pin = Toplevel()
    pin.geometry("600x400")
    pin.title("Change PIN")
    pin.configure(bg="aqua")
    pinn = StringVar()

    def confirm():
        if pinn.get() == "" or pinn.get() == None:
            messagebox.showwarning("Empty Field","Please enter pin number !")
        else:
            new = pinn.get() 
            pino.set(new)
            messagebox.askquestion("Confirmation","Are you sure, You want to continue it.")
            messagebox.showinfo("Information","PIN number has updated")
            pin.destroy()

    p = StringVar()
    top = Label(pin, text="Change ATM PIN Number", fg="red", bg="aqua", font=("arial", 20, 'bold'), pady=10).pack(side=TOP)
    lbl = Label(pin, text="Current PIN Number »", font=('arial', 15, 'bold'), fg="blue", bg="aqua").place(x=50, y=100)
    entry = Entry(pin, width=20,textvariable=p, fg="green", font=('arial', 15, 'bold'), bg="white").place(x=350, y=100)
    p.set(pino.get())
    lbl2 = Label(pin, text="New PIN Number »", font=('arial', 15, 'bold'), fg="blue", bg="aqua").place(x=50, y=150)
    entry2 = Entry(pin,textvariable=pinn, width=20, fg="red", font=('arial', 15, 'bold'), bg="white").place(x=350, y=150)
    lbl3 = Label(pin, text="Confirm PIN Number »", font=('arial', 15, 'bold'), fg="blue", bg="aqua").place(x=50, y=200)
    entry3 = Entry(pin, width=20, fg="red", font=('arial', 15, 'bold'), bg="white").place(x=350, y=200)
    btn = Button(pin, text="submit", width=10, fg="white", font=('arial', 15, 'bold'), bg="orange", command=confirm).place(x=250, y=250)

    pin.mainloop()


history = Button(frame,fg="black",bd=1,bg="white",width=6,font=("arial", 13, 'bold'), text="History",activebackground="pink",relief=SUNKEN, command=historyb)
history.pack(pady=8)
about = Button(frame,fg="black",bd=1,bg="white",width=6,font=("arial", 13, 'bold'), text="About",activebackground="pink",relief=SUNKEN, command=aboutb)
about.pack(pady=9)
exitb = Button(frame,fg="black",bd=1,bg="white",width=6,font=("arial", 13, 'bold'), text="Exit",activebackground="pink",relief=SUNKEN, command=exit)
exitb.pack(pady=10)
root.geometry("950x600")
root.title("Menu")
root.configure(bg="aqua")
top = Label(root, text="Welcome To ATM Service", fg="black",width=100, bg="blue",font=("arial", 20, 'bold'), pady=20)
top.pack(side=TOP)
localtime = time.asctime(time.localtime(time.time()))
time = Label(root, font=('calibri', 15, 'bold'), text=localtime,fg="red",bg="aqua", pady=10)
time.pack()
top = Label(root, text="  Select options ➡️",fg="purple",bg="aqua", font=("arial", 18,'bold'))
top.place(x=220, y=138)

# Operation buttons
frame3 = Frame(root,bg="pink", width = 600, height=350,padx=50, pady=30,highlightthickness=5)
frame3.pack(anchor=CENTER,pady=50)

enquiry = Button(frame3, padx=10, pady=15, bd=10, width=13, fg="white", font=('arial', 15, 'bold'), text="Balance Inquiry", bg="blue", command=balance)
enquiry.grid(row=0, column=0, padx=20, pady=10)
withdrawm = Button(frame3, padx=10, pady=15, bd=10, width=13, fg="white", font=('arial', 15, 'bold'), text="Money Withdraw", bg="blue", command=withdraw)
withdrawm.grid(row=1, column=0, padx=20, pady=10)
depositem = Button(frame3, padx=10, pady=15, bd=10, width=13, fg="white", font=('arial', 15, 'bold'), text="Money Deposite", bg="blue", command=deposite)
depositem.grid(row=0, column=1, padx=20, pady=10)
changep = Button(frame3, padx=10, pady=15, bd=10, width=13, fg="white", font=('arial', 15, 'bold'), text="Change PIN", bg="blue", activebackground="pink",command=changePin)
changep.grid(row=1, column=1, padx=20, pady=10)
l = Label(root, text = "ThankYou, Visit Again", pady=20,bg="blue",width=100, fg = "black", font=('Times New Roman', 20,'bold')) 
l.pack(side = BOTTOM)
root.mainloop()

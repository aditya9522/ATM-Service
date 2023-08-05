from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import subprocess

security = Tk()
security.title("Security")
pin = 'aditya'

def on_entry_click(event):
    """Function to handle the event when the entry field is clicked"""
    if password.get() == "Enter system password":
        password.delete(0, END)  # Remove the temporary text

def submit():
    if p.get() == pin:
        messagebox.showinfo("Information", "Permission Granted")
        # security.destroy()
        # Run the other script
        subprocess.run(["python", "D:\Python Projects\ATM\ATM_Menu.py"])
    elif p.get() == "":
        messagebox.showwarning("Warning", "Please Enter Password")
    else:
        messagebox.showerror("Error", "Invalid password!")

image1 = Image.open("security.png")
image1 = image1.resize((800, 400))  # Optional: Resize the image
photo = ImageTk.PhotoImage(image1)

security.maxsize(800, 400)
security.minsize(800, 400)

# Create a label and set the image as its background
background_label = Label(security, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

msg = Label(security, text=" ATM Service Authentication ", fg="blue", font=('Times New Roman', 20, 'bold'), bg='light gray', width=100)
msg.pack(side=TOP)

# securitys = Label(security, text="password", bg="aqua", fg="green", font=("arial", 15))
# securitys.place(x=340, y=170)

p = StringVar()
password = Entry(security, justify="center", fg="red", relief="flat",font=("arial", 14, "bold"), width=20, textvariable=p)
password.insert(0, "Enter system password")  # Set temporary text
password.bind('<FocusIn>', on_entry_click)  # Bind event to remove temporary text
password.place(x=140, y=150)

submit = Button(security, text="submit", command=submit, width=10, fg="white", font=(
    'arial', 15, 'bold'), bg="orange", activeforeground="red", activebackground="pink")
submit.place(x=190, y=250)

security.mainloop()

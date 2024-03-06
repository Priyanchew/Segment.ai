import mysql.connector
from tkinter import *
from tkinter import messagebox

def Ok():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="123456789", database="login_info")
    mycursor = mysqldb.cursor()
    uname = e1.get()
    password = e2.get()
    sql = "SELECT * FROM users WHERE uname = %s AND password = %s"
    mycursor.execute(sql, [(uname),( password)])
    results = mycursor.fetchall()

    if results:
        messagebox.showinfo("", "Login Success")
        root.destroy()
        # Call other functions or perform additional tasks after successful login
        return True
    else:
        messagebox.showerror("", "Login Failed")
        # You may handle login failure here or perform additional tasks
        return False

# Assuming 'root' is defined somewhere in your code
root = Tk()
root.title("Login")
root.geometry("300x200")

global e1
global e2

Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

# Assuming 'e1' and 'e2' are Entry widgets for username and password respectively
e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root, show="*")  # Use 'show' to hide the entered characters for passwords
e2.place(x=140, y=40)


Button(root, text="Login", command=Ok, height=3, width=13).place(x=10, y=100)

# Start the main loop
root.mainloop()
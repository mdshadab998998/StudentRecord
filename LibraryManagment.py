from tkinter import *
import mysql.connector
import tkinter.messagebox

main=Tk()
main.geometry("1800x800")

def p2():
    def adddb():
        mydb = mysql.connector.connect(host="localhost", user="root", password="Khan786786@", database="shadab")
        mycursor = mydb.cursor()
        nm = "INSERT INTO lib (Bookname,Authorname) VALUES(%s,%s)"
        val = (f"{p2_bookname.get()}", f"{p2_authoname.get()}")
        mycursor.execute(nm, val)
        mydb.commit()
        tkinter.messagebox.showinfo("Successful", "Added Successfully")

    p1_main_frame.place_forget()
    global p2_main_frame
    p2_main_frame=Frame(main, width=5000, height=995,bg="#17343A")
    p2_main_frame.place(x=1, y=1)
    p2_button=Button(p2_main_frame,text="Back",command=p21,width=17,height=2,font=("Arial","19"),bg="#CCB57F",fg="black")
    p2_button.place(x=60,y=60)
    p2_label=Label(p2_main_frame,text="Add New Book",font=("Arial","32"),bg="#17343A",fg="#CCB57F")
    p2_label.place(x=650,y=10)
    p2_bookname=StringVar()
    p2_authoname=StringVar()

    p2_bookname_label=Label(p2_main_frame,text="Enter Book Name",font=("Arial","22"),bg="#17343A",fg="#CCB57F")
    p2_bookname_label.place(x=400,y=200)
    p2_book_name_entry=Entry(p2_main_frame,width=30,textvariable=p2_bookname,font=("Arial",19))
    p2_book_name_entry.place(x=700,y=200,height=50)
    p2_authoname_label = Label(p2_main_frame, text="Enter Author Name", font=("Arial", "22"),bg="#17343A",fg="#CCB57F")
    p2_authoname_label.place(x=400, y=300)
    p2_autho_name_entry = Entry(p2_main_frame, width=30, textvariable=p2_authoname, font=("Arial", 19))
    p2_autho_name_entry.place(x=700, y=300, height=50)
    p2_button_add=Button(p2_main_frame,text="Add",width=17,height=2,font=("Arial","19"),bg="#CCB57F",fg="black",command=adddb)
    p2_button_add.place(x=700,y=400)


def p3():
    p1_main_frame.place_forget()
    global p3_main_frame
    p3_main_frame=Frame(main, width=5000, height=995,bg="#17343A")
    p3_main_frame.place(x=1, y=1)
    p3_button=Button(p3_main_frame,text="Back",command=p31,width=17,height=2,font=("Arial","19"),bg="#CCB57F",fg="black")
    p3_button.place(x=60,y=60)
    p3_label=Label(p3_main_frame,text="Availabel Book",font=("Arial","32"),bg="#17343A",fg="#CCB57F")
    p3_label.place(x=650,y=10)
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Khan786786@",
        database="shadab"
    )
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT * FROM lib")
    i = 0


    sb=Scrollbar(p3_main_frame,orient=VERTICAL)
    sb.place(x=1260,y=100,height=600)
    mylist=Listbox(p3_main_frame,yscrollcommand=sb.set,width=50,font=("Arial","20"))
    for student in my_conn:
        mylist.insert(END, f"{i+1}. {student[0] }"+"-"*10+"by"+"-"*10+ f"{student[1]}  ")
        i=i+1
    mylist.place(x=500,y=100,height=600)
    sb.config(command=mylist.yview)
def p4():
    def issue():
        l=[]
        mydb = mysql.connector.connect(host="localhost", user="root", password="Khan786786@", database="shadab")
        mycursor= mydb.cursor()
        nm = "INSERT INTO issue (Bookname,Authorname,studname,dat) VALUES(%s,%s,%s,%s)"
        val = (f"{p4_bookname.get()}", f"{p4_authoname.get()}", f"{p4_studname.get()}", f"{p4_dateissue.get()}")
        mycursor.execute(nm, val)
        mycursor.execute("SELECT * FROM lib")
        for i in mycursor:
            for j in i:
                l.append(j)
        print(l)
        p = f"DELETE FROM lib WHERE Bookname='{p4_bookname.get()}';"
        q= f"DELETE FROM lib WHERE Authorname='{p4_authoname.get()}';"
        if p4_bookname.get() in l and p4_authoname.get() in l :
            mycursor.execute(p)
            mydb.commit()
            tkinter.messagebox.showinfo("Successful", "Issue Successfully")
        else:
            tkinter.messagebox.showinfo("Successful", "error bookname or author name incorrect!!!")

    p1_main_frame.place_forget()
    global p4_main_frame
    p4_main_frame=Frame(main, width=5000, height=995,bg="#17343A")
    p4_main_frame.place(x=1, y=1)
    p4_button=Button(p4_main_frame,text="Back",command=p41,width=17,height=2,font=("Arial","19"),bg="#CCB57F",fg="black")
    p4_button.place(x=60,y=60)
    p4_label=Label(p4_main_frame,text="Issue Book",font=("Arial","32"),bg="#17343A",fg="#CCB57F")
    p4_label.place(x=650,y=10)

    p4_bookname = StringVar()
    p4_authoname = StringVar()
    p4_studname = StringVar()
    p4_dateissue = StringVar()

    p4_bookname_label = Label(p4_main_frame, text="Enter Book Name", font=("Arial", "22"), bg="#17343A", fg="#CCB57F")
    p4_bookname_label.place(x=400, y=200)
    p4_book_name_entry = Entry(p4_main_frame, width=30, textvariable=p4_bookname, font=("Arial", 19))
    p4_book_name_entry.place(x=700, y=200, height=50)
    p4_authoname_label = Label(p4_main_frame, text="Enter Author Name", font=("Arial", "22"), bg="#17343A",
                               fg="#CCB57F")
    p4_authoname_label.place(x=400, y=300)
    p4_autho_name_entry = Entry(p4_main_frame, width=30, textvariable=p4_authoname, font=("Arial", 19))
    p4_autho_name_entry.place(x=700, y=300, height=50)
    p4_studname_label = Label(p4_main_frame, text="Enter Student Name", font=("Arial", "22"), bg="#17343A", fg="#CCB57F")
    p4_studname_label.place(x=400, y=400)
    p4_studname_entry = Entry(p4_main_frame, width=30, textvariable=p4_studname, font=("Arial", 19))
    p4_studname_entry.place(x=700, y=400, height=50)

    p4_date_label = Label(p4_main_frame, text="Date", font=("Arial", "22"), bg="#17343A", fg="#CCB57F")
    p4_date_label.place(x=400, y=500)
    p4_dateissue_entry = Entry(p4_main_frame, width=30, textvariable=p4_dateissue, font=("Arial", 19))
    p4_dateissue_entry.place(x=700, y=500, height=50)

    p4_button_add = Button(p4_main_frame, text="Issue", width=17, height=2, font=("Arial", "19"), bg="#CCB57F",
                           fg="black",command=issue)
    p4_button_add.place(x=700, y=600)

def p5():
    p1_main_frame.place_forget()
    global p5_main_frame
    p5_main_frame = Frame(main, width=5000, height=995, bg="#17343A")
    p5_main_frame.place(x=1, y=1)
    p5_button = Button(p5_main_frame, text="Back", command=p51, width=17, height=2, font=("Arial", "19"), bg="#CCB57F",
                       fg="black")
    p5_button.place(x=60, y=60)
    p5_label = Label(p5_main_frame, text="List Of Issue Book", font=("Arial", "32"), bg="#17343A", fg="#CCB57F")
    p5_label.place(x=650, y=10)
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Khan786786@",
        database="shadab"
    )
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT * FROM issue limit 0,10")
    i = 0
    global sb
    global mylist
    sb=Scrollbar(orient=VERTICAL)
    sb.place(x=1260,y=150,height=600)
    mylist=Listbox(yscrollcommand=sb.set,width=50,font=("Arial","20"))
    mylist.place(x=500,y=150,height=600)
    Label(p5_main_frame,width=58,text="BookName" + " " * 13 + "Author" + " " * 13 + " STudent" + " " * 13 + " Date", font="Arial,20",
          bg="#17343A",fg="#CCB57F").place(x=500, y=100)
    for student in my_conn:
        for j in range(len(student)):
            e = Entry(mylist,width=15, font="Arisal,15")
            e.grid(row=200+i, column=200+j)
            e.insert(END, student[j])
        i = i + 1
def p6():
    def Return():
        l=[]
        mydb = mysql.connector.connect(host="localhost", user="root", password="Khan786786@", database="shadab")
        mycursor = mydb.cursor()
        nm = "INSERT INTO lib (Bookname,Authorname) VALUES(%s,%s)"
        val = (f"{p6_bookname.get()}", f"{p6_authoname.get()}")
        mycursor.execute(nm, val)
        mycursor.execute("SELECT * FROM issue")
        for i in mycursor:
            for j in i:
                l.append(j)
        p = f"DELETE FROM issue WHERE Bookname='{p6_bookname.get()}';"
        # q= f"DELETE FROM lib WHERE Authorname='{p4_authoname.get()}';"
        if p6_bookname.get() in l and p6_authoname.get() in l and   p6_studname.get() in l and p6_dateissue.get() in l :
            mycursor.execute(p)
            mydb.commit()
            tkinter.messagebox.showinfo("Successful", "Return Successfully")
        else:
            tkinter.messagebox.showinfo("Successful", "error bookname or author name or student name or date incorrect!!!")


        # pass
    p1_main_frame.place_forget()
    global p6_main_frame
    p6_main_frame = Frame(main, width=5000, height=995, bg="#17343A")
    p6_main_frame.place(x=1, y=1)
    p6_button = Button(p6_main_frame, text="Back", command=p61, width=17, height=2, font=("Arial", "19"), bg="#CCB57F",
                       fg="black")
    p6_button.place(x=60, y=60)
    p6_label = Label(p6_main_frame, text="Return Book", font=("Arial", "32"), bg="#17343A", fg="#CCB57F")
    p6_label.place(x=650, y=10)
    p6_bookname = StringVar()
    p6_authoname = StringVar()
    p6_studname = StringVar()
    p6_dateissue = StringVar()
    p6_bookname_label = Label(p6_main_frame, text="Enter Book Name", font=("Arial", "22"), bg="#17343A", fg="#CCB57F")
    p6_bookname_label.place(x=400, y=200)
    p6_book_name_entry = Entry(p6_main_frame, width=30, textvariable=p6_bookname, font=("Arial", 19))
    p6_book_name_entry.place(x=700, y=200, height=50)
    p6_authoname_label = Label(p6_main_frame, text="Enter Author Name", font=("Arial", "22"), bg="#17343A",
                               fg="#CCB57F")
    p6_authoname_label.place(x=400, y=300)
    p6_autho_name_entry = Entry(p6_main_frame, width=30, textvariable=p6_authoname, font=("Arial", 19))
    p6_autho_name_entry.place(x=700, y=300, height=50)
    p6_studname_label = Label(p6_main_frame, text="Enter Student Name", font=("Arial", "22"), bg="#17343A",
                              fg="#CCB57F")
    p6_studname_label.place(x=400, y=400)
    p6_studname_entry = Entry(p6_main_frame, width=30, textvariable=p6_studname, font=("Arial", 19))
    p6_studname_entry.place(x=700, y=400, height=50)

    p6_date_label = Label(p6_main_frame, text="Date", font=("Arial", "22"), bg="#17343A", fg="#CCB57F")
    p6_date_label.place(x=400, y=500)
    p6_dateissue_entry = Entry(p6_main_frame, width=30, textvariable=p6_dateissue, font=("Arial", 19))
    p6_dateissue_entry.place(x=700, y=500, height=50)

    p6_button_add = Button(p6_main_frame, text="Return", width=17, height=2, font=("Arial", "19"), bg="#CCB57F",
                           fg="black", command=Return)
    p6_button_add.place(x=700, y=600)



def p21():
    p1_main_frame.place(x=1,y=1)
    p2_main_frame.place_forget()
def p31():
    p1_main_frame.place(x=1,y=1)
    p3_main_frame.place_forget()
def p41():
    p1_main_frame.place(x=1,y=1)
    p4_main_frame.place_forget()
def p51():
    p1_main_frame.place(x=1,y=1)
    p5_main_frame.place_forget()
    mylist.place_forget()
    sb.place_forget()
def p61():
    p1_main_frame.place(x=1,y=1)
    p6_main_frame.place_forget()
def home():
    if p1_login_username.get()=="shadab" and p1_login_password.get()=="khan123":
        p1_login_frame.place_forget()
        p1_main_frame.place(x=1,y=1)
    else:
        tkinter.messagebox.showinfo("Encorrect!!", "user name or password incorect!!")


def logout():
    p1_main_frame.place_forget()
    p1_login_frame.place(x=1, y=1)


p1_main_frame=Frame(main,width=5000,height=995,bg="#17343A")
p1_main_frame.place(x=1,y=1)
p1_label=Label(p1_main_frame,text="WELCOME TO BOOK SYSTEM ",font=("Arial","32"),bg="#17343A",fg="#CCB57F")
p1_label.place(x=450,y=10)
p1_frame=Frame(p1_main_frame,highlightbackground="black",bd=1,width=266,bg="black",height=78)
p1_frame.place(x=600,y=110)
p1_bt1=Button(p1_frame,text="Add Books",width=17,height=2,font=("Arial","19"),command=p2,bg="#CCB57F",fg="black")
p1_bt1.place(x=1,y=1)

p1_frame2=Frame(p1_main_frame,highlightbackground="black",bd=1,width=266,bg="black",height=78)
p1_frame2.place(x=600,y=210)
p1_bt2=Button(p1_frame2,text="View Books",width=17,height=2,font=("Arial","19"),bg="#CCB57F",fg="black",command=p3)
p1_bt2.place(x=1,y=1)

p1_frame3=Frame(p1_main_frame,highlightbackground="black",bd=1,width=266,bg="black",height=78)
p1_frame3.place(x=600,y=310)
p1_bt3=Button(p1_frame3,text="Issue Books",width=17,height=2,font=("Arial","19"),bg="#CCB57F",fg="black",command=p4)
p1_bt3.place(x=1,y=1)

p1_frame4=Frame(p1_main_frame,highlightbackground="black",bd=1,width=266,bg="black",height=78)
p1_frame4.place(x=600,y=410)
p1_bt4=Button(p1_frame4,text="View Issued Books",width=17,height=2,font=("Arial","19"),bg="#CCB57F",fg="black",command=p5)
p1_bt4.place(x=1,y=1)

p1_frame5=Frame(p1_main_frame,highlightbackground="black",bd=1,width=266,bg="black",height=78)
p1_frame5.place(x=600,y=510)
p1_bt5=Button(p1_frame5,text="Return Book",width=17,height=2,font=("Arial","19"),bg="#CCB57F",fg="black",command=p6)
p1_bt5.place(x=1,y=1)

p1_frame6=Frame(p1_main_frame,highlightbackground="black",bd=1,width=266,bg="black",height=78)
p1_frame6.place(x=600,y=610)
p1_bt6=Button(p1_frame6,text="Logout",width=17,height=2,font=("Arial","19"),bg="#CCB57F",fg="black",command=logout)
p1_bt6.place(x=1,y=1)
p1_main_frame.place_forget()
p1_login_frame=Frame(main,width=5000,height=995,bg="#17343A")
p1_login_frame.place(x=1,y=1)
p1_login=Label(p1_login_frame,text="LIBRARY MANAGMENT SYSTEM ",font=("Arial","32"),bg="#17343A",fg="#CCB57F")
p1_login.place(x=450,y=10)
p1_login_username=StringVar()
p1_login_password=StringVar()

p1_login_username_label=Label(p1_login_frame,text="Enter User Name",font=("Arial","22"),bg="#17343A",fg="#CCB57F")
p1_login_username_label.place(x=400,y=200)
p1_login_username_entry=Entry(p1_login_frame,width=30,textvariable=p1_login_username,font=("Arial",19))
p1_login_username_entry.place(x=700,y=200,height=50)
p1_login_password_label = Label(p1_login_frame, text="Enter Password", font=("Arial", "22"),bg="#17343A",fg="#CCB57F")
p1_login_password_label.place(x=400, y=300)
p1_login_password_entry = Entry(p1_login_frame, width=30, textvariable=p1_login_password, font=("Arial", 19))
p1_login_password_entry.place(x=700, y=300, height=50)
p1_login_button=Button(p1_login_frame,text="Login",width=17,height=2,font=("Arial","19"),bg="#CCB57F",fg="black",command=home)
p1_login_button.place(x=700,y=400)

main.mainloop()
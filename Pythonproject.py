from tkinter import *
import mysql.connector
import tkinter.messagebox


main=Tk()
main.configure(bg="#f58793")
frame=Frame(main,bg="#f58793")
frame.place(x=500,y=350)

def Show() :
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Khan786786@",
        database="shadab"
    )
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT * FROM Newstudent limit 0,10")
    i = 0
    Label(text="Name"+" "*13+"ID"+" "*13 +" Course"+" "*13+" Fee",font="Arial,20",bg="#f58793").place(x=500,y=320)
    for student in my_conn:
        for j in range(len(student)):
            e = Entry(frame, width=10, fg='green',font="Arisal,15",bg="#f58793")
            e.grid(row=99 + i, column=99 + j)
            e.insert(END, student[j])
        i = i + 1

def Add() :
    mydb = mysql.connector.connect(host="localhost", user="root", password="Khan786786@", database="shadab")
    mycursor = mydb.cursor()
    nm = "INSERT INTO Newstudent (Name,id,course,fee) VALUES(%s,%s,%s,%s)"
    val = (f"{e1.get()}",f"{e2.get()}",f"{e3.get()}",f"{e4.get()}")
    mycursor.execute(nm, val)
    mydb.commit()
    tkinter.messagebox.showinfo("Successful","Added Successfully")


def Delete() :

    mydb = mysql.connector.connect(host="localhost", user="root", password="Khan786786@", database="shadab")
    mycursor = mydb.cursor()
    # nm = "SET SQL_SAFE_UPDATES = 0;"
    p=f"DELETE FROM Newstudent WHERE id='{e2.get()}';"
    mycursor.execute(p)
    mydb.commit()
    tkinter.messagebox.showinfo("Successful","Deleted Successfully")


    # Label(s,text=f"{uvalue.get()} successfully Deletd").grid(row=2,column=2)
def Reset() :

    # frame.destroy()
    # frame = Frame(main)
    # frame.place(x=10, y=250)
    for widget in frame.winfo_children():
       widget.destroy()
    # if e1entry:
    #     e1entry.delete(0, END)
    # if e2entry:
    #         e2entry.delete(0, END)
    # if e3entry:
    #     e3entry.delete(0, END)
    # if e4entry:
    #     e4entry.delete(0, END)


    e1entry.delete(0, END)
    e2entry.delete(0, END)
    e3entry.delete(0, END)
    e4entry.delete(0, END)



Label(main,text="Student_Name",font="Arial,30",bg="#f58793").place(x=500,y=10)
Label(main,text="Student_Id",font="Arial,30",bg="#f58793").place(x=500,y=50)
Label(main,text="Course",font="Arial,30" ,bg="#f58793").place(x=500,y=90)
Label(main,text="Fee",font="Arial,30",bg="#f58793").place(x=500,y=130)
e1=StringVar()
e2=StringVar()
e3=StringVar()
e4=StringVar()
e1entry=Entry(main,textvariable=e1,font="Arial,30")
e1entry.place(x=680,y=10)
e2entry=Entry(main,textvariable=e2,font="Arial,30")
e2entry.place(x=680,y=50)
e3entry=Entry(main,textvariable=e3,font="Arial,30")
e3entry.place(x=680,y=90)
e4entry=Entry(main,textvariable=e4,font="Arial,30")
e4entry.place(x=680,y=130)
Button(main,text="ADD",command=Add,font="Arial,10",width=10,bg="#f58793").place(x=400,y=230)
Button(main,text="DELETE",command=Delete,font="Arial,10",width=10,bg="#f58793").place(x=600,y=230)
Button(main,text="SHOW/REFRESH",command=Show,font="Arial,10",width=14,bg="#f58793").place(x=800,y=230)
Button(main,text="RESET",command=Reset,font="Arial,10",width=10,bg="#f58793").place(x=1000,y=230)

Label(text="**For delete  enter only id",font="Arial,6",bg="#f58793").place(x=560,y=190)




main.mainloop()
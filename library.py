from msilib.schema import ListBox
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import datetime
import tkinter



class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #============================================variable======================================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.middlename_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finalprice=StringVar()

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="black",fg="Lime",bd=10,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6) 
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=110,width=1360,height=400)

        #===========================================DataFrameLeft=================================================================
        DataFrameLeft=LabelFrame(frame,text="LIBRARY Member Information",bg="Powder blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
        DataFrameLeft.place(x=0,y=5,width=810,height=360)
        
        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin","Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN No",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        lblPRN_No=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.prn_var,width=29)
        lblPRN_No.grid(row=1,column=1)

        ID_No=Label(DataFrameLeft,bg="powder blue",text="ID No",font=("arial",12,"bold"),padx=2,pady=6)
        ID_No.grid(row=2,column=0,sticky=W)
        lD_No=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.id_var,width=29)
        lD_No.grid(row=2,column=1)
        
        First_name=Label(DataFrameLeft,bg="powder blue",text="First name",font=("arial",12,"bold"),padx=2,pady=6)
        First_name.grid(row=3,column=0,sticky=W)
        First_name=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.firstname_var,width=29)
        First_name.grid(row=3,column=1)
        
        Middle_name=Label(DataFrameLeft,bg="powder blue",text="Middle name",font=("arial",12,"bold"),padx=2,pady=6)
        Middle_name.grid(row=4,column=0,sticky=W)
        Middle_name=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.middlename_var,width=29)
        Middle_name.grid(row=4,column=1)
        
        Last_name=Label(DataFrameLeft,bg="powder blue",text="Last name",font=("arial",12,"bold"),padx=2,pady=6)
        Last_name.grid(row=5,column=0,sticky=W)
        Last_name=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.lastname_var,width=29)
        Last_name.grid(row=5,column=1)
        
        Address=Label(DataFrameLeft,bg="powder blue",text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        Address.grid(row=6,column=0,sticky=W)
        Address=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.address_var,width=29)
        Address.grid(row=6,column=1)
        
        Post_code=Label(DataFrameLeft,bg="powder blue",text="Post code",font=("arial",12,"bold"),padx=2,pady=6)
        Post_code.grid(row=7,column=0,sticky=W)
        Post_code=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.postcode_var,width=29)
        Post_code.grid(row=7,column=1)
        
        Mobile=Label(DataFrameLeft,bg="powder blue",text="Mobile",font=("arial",12,"bold"),padx=2,pady=6)
        Mobile.grid(row=8,column=0,sticky=W)
        Mobile=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.mobile_var,width=29)
        Mobile.grid(row=8,column=1)
        

        Book_ID=Label(DataFrameLeft,bg="powder blue",text="Book ID",font=("arial",12,"bold"),padx=2,pady=6)
        Book_ID.grid(row=0,column=2,sticky=W)
        Book_ID=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        Book_ID.grid(row=0,column=3)
        
        Book_title=Label(DataFrameLeft,bg="powder blue",text="Book Title",font=("arial",12,"bold"),padx=2,pady=6)
        Book_title.grid(row=1,column=2,sticky=W)
        Book_title=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        Book_title.grid(row=1,column=3)
        
        AutName=Label(DataFrameLeft,bg="powder blue",text="Auther Name",font=("arial",12,"bold"),padx=2,pady=6)
        AutName.grid(row=2,column=2,sticky=W)
        AutName=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.auther_var,width=29)
        AutName.grid(row=2,column=3)
        
        Dtborr=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed",font=("arial",12,"bold"),padx=2,pady=6)
        Dtborr.grid(row=3,column=2,sticky=W)
        Dtborr=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        Dtborr.grid(row=3,column=3)
        
        Dtdue=Label(DataFrameLeft,bg="powder blue",text="Date Due",font=("arial",12,"bold"),padx=2,pady=6)
        Dtdue.grid(row=4,column=2,sticky=W)
        Dtdue=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        Dtdue.grid(row=4,column=3)
        
        Dys=Label(DataFrameLeft,bg="powder blue",text="Days on Book",font=("arial",12,"bold"),padx=2,pady=6)
        Dys.grid(row=5,column=2,sticky=W)
        Dys=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.daysonbook,width=29)
        Dys.grid(row=5,column=3)
        
        fine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine",font=("arial",12,"bold"),padx=2,pady=6)
        fine.grid(row=6,column=2,sticky=W)
        fine=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.latereturnfine_var,width=29)
        fine.grid(row=6,column=3)
        
        dod=Label(DataFrameLeft,bg="powder blue",text="Date over Due",font=("arial",12,"bold"),padx=2,pady=6)
        dod.grid(row=7,column=2,sticky=W)
        dod=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.dateoverdue,width=29)
        dod.grid(row=7,column=3)

        price=Label(DataFrameLeft,bg="powder blue",text="Actual Price",font=("arial",12,"bold"),padx=2,pady=6)
        price.grid(row=8,column=2,sticky=W)
        price=Entry(DataFrameLeft,bg="pink",font=("arial",12,"bold"),textvariable=self.finalprice,width=29)
        price.grid(row=8,column=3)

        #===========================================DataFrameRight================================================================
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="Powder blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
        DataFrameRight.place(x=820,y=5,width=480,height=360)

        
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=26,height=15,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBook=['Head Firt Book','Python for Begners','java for begners','C programming','C++ programming','Linux for Begners','Learn HTML','Learn CSS','Learn JavaScript','Computer Organisation','DBMS','MySQL Database','Computer Science','PHP Programming','Learn JQuery','Advance java','Web developement guide']

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=='Head Firt Book'):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("python Manual")
                self.auther_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.788")


            elif (x=='Python for Begners'):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("python Basic")
                self.auther_var.set("Mr.John")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.950")

            
            elif (x=='java for begners'):
                self.bookid_var.set("BKID6585")
                self.booktitle_var.set("java Basic")
                self.auther_var.set("Mr.Mickle")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.650")


            elif (x=='C programming'):
                self.bookid_var.set("BKID6655")
                self.booktitle_var.set("C Basic")
                self.auther_var.set("Mr.Anurag")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.700")
            
            
            elif (x=='C++ programming'):
                self.bookid_var.set("BKID6695")
                self.booktitle_var.set("C++ Basic")
                self.auther_var.set("Mr.A.K.Verma")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.900")


        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBook:
            listBox.insert(END,item)


        #===========================================ButtonsFrame=================================================================
        FrameButton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameButton.place(x=0,y=510,width=1360,height=50)
        
        Btn=Button(FrameButton,command=self.add_data,font=("arial",10,"bold"),text='Add Data',bg="red",fg="black",width=30)
        Btn.grid(row=0,column=0)
        
        Btn=Button(FrameButton,command=self.showData,font=("arial",10,"bold"),text='Show Data',bg="red",fg="black",width=26)
        Btn.grid(row=0,column=1)
        
        Btn=Button(FrameButton,command=self.update,font=("arial",10,"bold"),text='Update',bg="red",fg="black",width=26)
        Btn.grid(row=0,column=2)
        
        Btn=Button(FrameButton,command=self.delete,font=("arial",10,"bold"),text='Delete',bg="red",fg="black",width=26)
        Btn.grid(row=0,column=3)
       
        Btn=Button(FrameButton,command=self.reset,font=("arial",10,"bold"),text='Reset',bg="red",fg="black",width=26)
        Btn.grid(row=0,column=4)
       
        Btn=Button(FrameButton,command=self.iExit,font=("arial",10,"bold"),text='Exit',bg="red",fg="black",width=23)
        Btn.grid(row=0,column=5)


        #===========================================InformationsFrame=============================================
        
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=560,width=1360,height=140)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1310,height=110)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","middlename","lastname","address","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=xscroll.set)
 
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        
        self.library_table.heading("membertype",text="Member type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First name")
        self.library_table.heading("middlename",text="Middle name")
        self.library_table.heading("lastname",text="Last name")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Bookid")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("middlename",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anuveer@1997",database="librarydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                         self.member_var.get(),
                                                         self.prn_var.get(),
                                                         self.id_var.get(),
                                                         self.firstname_var.get(),
                                                         self.middlename_var.get(),
                                                         self.lastname_var.get(),
                                                         self.address_var.get(),
                                                         self.postcode_var.get(),
                                                         self.mobile_var.get(),
                                                         self.bookid_var.get(),
                                                         self.booktitle_var.get(),
                                                         self.auther_var.get(),
                                                         self.dateborrowed_var.get(),
                                                         self.datedue_var.get(),
                                                         self.daysonbook.get(),
                                                         self.latereturnfine_var.get(),
                                                         self.dateoverdue.get(),
                                                         self.finalprice.get()
                                                      ))
        conn.commit()
        self.fatch_data()
        conn.close()
        
        messagebox.showinfo("Success","Member has been inserted successfully")
        self.reset()
        

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anuveer@1997",database="librarydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,MiddleName=%s,LastName=%s,Address=%s,PostID=%s,Mobile=%s,BookID=%s,BookTitle=%s,Auther=%s,DateBorrowed=%s,DateDue=%s,DaysOnBook=%s,LateReturnFine=%s,DateOverDue=%s,FinalPrice=%s where PRN_No=%s",(
                                                        self.member_var.get(),
                                                        self.id_var.get(),
                                                        self.firstname_var.get(),
                                                        self.middlename_var.get(),
                                                        self.lastname_var.get(),
                                                        self.address_var.get(),
                                                        self.postcode_var.get(),
                                                        self.mobile_var.get(),
                                                        self.bookid_var.get(),
                                                        self.booktitle_var.get(),
                                                        self.auther_var.get(),
                                                        self.dateborrowed_var.get(),
                                                        self.datedue_var.get(),
                                                        self.daysonbook.get(),
                                                        self.latereturnfine_var.get(),
                                                        self.dateoverdue.get(),
                                                        self.finalprice.get(),
                                                        self.prn_var.get(),                                       
                                                        ))

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Updated")


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anuveer@1997",database="librarydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.middlename_var.set(row[4]),
        self.lastname_var.set(row[5]),
        self.address_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finalprice.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() +"\n")    
        self.txtBox.insert(END,"PRN No:\t\t"+ self.prn_var.get() +"\n")    
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get() +"\n")    
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() +"\n")    
        self.txtBox.insert(END,"MiddleName:\t\t"+ self.middlename_var.get() +"\n")    
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() +"\n")    
        self.txtBox.insert(END,"Address:\t\t"+ self.address_var.get() +"\n")    
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() +"\n")    
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() +"\n")    
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() +"\n")    
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() +"\n")    
        self.txtBox.insert(END,"Auther:\t\t"+ self.auther_var.get() +"\n")    
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() +"\n")    
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() +"\n")    
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook.get() +"\n")    
        self.txtBox.insert(END,"LateReturnFine:\t\t"+ self.latereturnfine_var.get() +"\n")    
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue.get() +"\n")    
        self.txtBox.insert(END,"FinalPrice:\t\t"+ self.finalprice.get() +"\n")    

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.middlename_var.set(""),
        self.lastname_var.set(""),
        self.address_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue.set(""),
        self.finalprice.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return


    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Anuveer@1997",database="librarydata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")


class Mydata (LibraryManagementSystem):
    def __init__(self,root):
        self.root=root
        self.root.title("Developer --> Anurag Kumar Verma")
        self.root.geometry("1550x800+0+0")

        self.username=StringVar()
        self.password=StringVar()

        img=Image.open("Images/LoginImage.jpg")
        img=img.resize((700,400),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        lb1_img=Label(self.root,image=self.photoimg,bd=10,relief=RIDGE)
        lb1_img.place(x=330,y=150,width=700,height=400)
        
        name=Entry(self.root,font=("arial",17,"bold"),textvariable=self.username,bg="black",fg="lime")
        name.place(x=705,y=253,width=200,height=35)
        
        pasw=Entry(self.root,font=("arial",17,"bold"),textvariable=self.password,bg="black",fg="lime")
        pasw.place(x=705,y=312,width=200,height=35)

        btn1=Button(self.root,text="Login",command=self.ok,font=("arial",15,"bold"),bd=0,bg="orange")
        btn1.place(x=642,y=398,width=118,height=29)
        
        btn2=Button(self.root,text="Register",font=("arial",15,"bold"),bd=0,bg="orange")
        btn2.place(x=782,y=398,width=118,height=29)


    def ok(self):

        if self.username.get() == "Anurag" and self.password.get() == "598330":
           # root=Tk()
            obj=LibraryManagementSystem(root)
            root.mainloop() # for keep stop the window using mainloop()
            self.root.destroy()
        else:
            messagebox.showerror("Error","Username or Password wrong")
            self.username.set("")
            self.password.set("")
            
        

if __name__=="__main__":
    root=Tk()
    obj=Mydata(root)
    root.mainloop()            





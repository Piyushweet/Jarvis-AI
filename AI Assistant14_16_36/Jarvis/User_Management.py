from tkinter import*
from tkinter import ttk,messagebox
import time
import os
import pymysql

class User:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("USER Management System")
        self.root.config(bg="#074463")
        title=Label(self.root,pady=5,bg="white",fg="navy",text="User Management System",font=("times new roman",30,"bold"),bd=5,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        self.root.focus_force()
        #====================All Variables======================================
        self.var_uno=StringVar()
        self.var_fname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
#=======================================================================
        fg_e="white"
        bg_e="crimson"
        fg_btn_e="white"
        bg_btn_e="#074463"
        User_Manage_Frame=Frame(self.root,bd=4,relief=GROOVE,bg="crimson" )#"#074463")
        User_Manage_Frame.place(x=50,y=70,width=500,height=600)

        lbl=Label(User_Manage_Frame,text="Manage USER",bg=bg_e,fg=fg_e,font=("Comic Sans MS",20,"bold"),pady=0).grid(row=0,columnspan=5,pady=20)

        lblId=Label(User_Manage_Frame,text="USER No.",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblId.grid(row=2,column=0,padx=30,pady=3,sticky="w")
        txtId=Entry(User_Manage_Frame,bd=5,relief=GROOVE,textvariable=self.var_uno,width=20,font=("times new roman",18))
        txtId.grid(row=2,column=1,padx=20,pady=3)
        
        lblName=Label(User_Manage_Frame,text="Name",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblName.grid(row=3,column=0,padx=30,pady=3,sticky="w")
        txtName=Entry(User_Manage_Frame,bd=5,relief=GROOVE,textvariable=self.var_fname,width=20,font=("times new roman",18))
        txtName.grid(row=3,column=1,padx=20,pady=3)

        lblContact=Label(User_Manage_Frame,text="Contact No",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblContact.grid(row=4,column=0,padx=30,pady=3,sticky="w")
        txtContact=Entry(User_Manage_Frame,bd=5,relief=GROOVE,width=20,textvariable=self.var_contact,font=("times new roman",18))
        txtContact.grid(row=4,column=1,padx=20,pady=3)

        lblEmail=Label(User_Manage_Frame,text="Email",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblEmail.grid(row=5,column=0,padx=30,pady=3,sticky="w")
        txtEmail=Entry(User_Manage_Frame,bd=5,relief=GROOVE,width=20,textvariable=self.var_email,font=("times new roman",18))
        txtEmail.grid(row=5,column=1,padx=20,pady=3)


        '''
        combogender=ttk.Combobox(User_Manage_Frame,textvariable=self.var_email,font=("times new roman",18),width=19,state='readonly')
        combogender['values']=("Male","Female","Other")
        combogender.set("Select Gender")
        combogender.grid(row=5,column=1,padx=20,pady=3)'''

        lblSecurityQ=Label(User_Manage_Frame,text="Security Question",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblSecurityQ.grid(row=6,column=0,padx=30,pady=3,sticky="w")
        comboSecurityQ=ttk.Combobox(User_Manage_Frame,textvariable= self.var_securityQ,font=("times new roman",18),width=19,state='readonly')
        comboSecurityQ['values']=("Select","Your Birth Place","Your Nickname","Your Pet Name")
        comboSecurityQ.set("Select Question")
        comboSecurityQ.grid(row=6,column=1,padx=20,pady=3)
        '''
        txtContact=Entry(User_Manage_Frame,bd=5,textvariable=self.var_securityQ,relief=GROOVE,width=20,font=("times new roman",18))
        txtContact.grid(row=6,column=1,padx=20,pady=3)'''

        lblSecurityA=Label(User_Manage_Frame,text="Security Answer",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblSecurityA.grid(row=7,column=0,padx=30,pady=3,sticky="w")
        txtSecurityA=Entry(User_Manage_Frame,textvariable= self.var_SecurityA,bd=5,relief=GROOVE,width=20,font=("times new roman",18))
        txtSecurityA.grid(row=7,column=1,padx=20,pady=3)
        '''
        lblAddress=Label(User_Manage_Frame,text="Address",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblAddress.grid(row=11,column=0,padx=30,pady=3,sticky="nw")
        self.txtAddress=Text(User_Manage_Frame,width=28,height=5,font=("",13))
        self.txtAddress.grid(row=11,column=1,padx=20,pady=3,sticky="w")'''

        pswd=Label(User_Manage_Frame,text="Password ",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        pswd.grid(row=8,column=0,padx=30,pady=3,sticky="w")
        txt_pswd=Entry(User_Manage_Frame,textvariable=self.var_pass,bd=5,relief=GROOVE,width=20,font=("times new roman",18))
        txt_pswd.grid(row=8,column=1,padx=20,pady=3)
        #self.txt_pswd.place(x=300,y=310,width=250)
        '''
        confirm_pswd=Label(User_Manage_Frame,text="Re-eneterd Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=300,y=400)

        self.txt_confirm_pswd=ttk.Entry(User_Manage_Frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=300,y=400,width=250)
        '''
        OptionBtn=Frame(User_Manage_Frame,bd=4,relief=GROOVE,bg="white")
        OptionBtn.place(x=10,y=500,width=475)

        AddBtn=Button(OptionBtn,text="Add",width=8,bg=bg_btn_e,fg=fg_btn_e ,cursor="hand2",command=self.Add_User,font=("times new roman",15,"bold"),pady=4)
        AddBtn.grid(row=0,column=0,padx=5,pady=5)

        UpdateBtn=Button(OptionBtn,text="Update",bg=bg_btn_e,fg=fg_btn_e ,cursor="hand2",command=self.update_details,width=8,font=("times new roman",15,"bold"),pady=4)
        UpdateBtn.grid(row=0,column=1,padx=5,pady=5)

        DeleteBtn=Button(OptionBtn,text="Delete",bg=bg_btn_e,fg=fg_btn_e ,cursor="hand2",command=self.delete_details,width=8,font=("times new roman",15,"bold"),pady=4)
        DeleteBtn.grid(row=0,column=2,padx=5,pady=5)

        ClearBtn=Button(OptionBtn,text="Clear",bg=bg_btn_e,fg=fg_btn_e ,cursor="hand2",command=self.clear_details,width=8,font=("times new roman",15,"bold"),pady=4)
        ClearBtn.grid(row=0,column=3,padx=5,pady=5)

        
#=======================User Frame=======================================================

        self.UserDetail_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="crimson")
        self.UserDetail_Frame.place(x=560,y=70,width=750,height=600)

        self.SearchKeyword=StringVar()
        self.searchtxt=StringVar()
        lblSearchBy=Label(self.UserDetail_Frame,bg="crimson",fg="white",text="Search By",font=("times new roman",20,"bold")).grid(row=0,column=0,padx=10,pady=10)

        self.comboSearchBy=ttk.Combobox(self.UserDetail_Frame,textvariable=self.SearchKeyword,width=12,font=("times new roman",13),state='readonly')
        self.comboSearchBy["values"]=("USER No.","Name","Contact No","Email")
        self.comboSearchBy.set("Select Options")
        self.comboSearchBy.grid(row=0,column=1,padx=10,pady=10)
        
        txtSearch=Entry(self.UserDetail_Frame,textvariable=self.searchtxt,width=15,bd=4,relief=GROOVE,font=("times new roman",12)).grid(row=0,column=2,padx=10)

        btnsearch=Button(self.UserDetail_Frame,command=self.SearchBy,text="Search",width=12,font=("times new roman",12,"bold")).grid(row=0,column=3,padx=5)
        btnShow=Button(self.UserDetail_Frame,text="Show All",command=self.showDetails,width=12,font=("times new roman",12,"bold")).grid(row=0,column=4,padx=5)


        EmptTableFrame=Frame(self.UserDetail_Frame,bd=4,relief=GROOVE)
        EmptTableFrame.place(x=10,y=60,width=720,height=520)

        scroll_x=Scrollbar(EmptTableFrame,orient=HORIZONTAL)
        scroll_y=Scrollbar(EmptTableFrame,orient=VERTICAL)

        self.UserTable=ttk.Treeview(EmptTableFrame,columns=("USER No.","Name","Contact No","Email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.UserTable.xview)
        scroll_y.config(command=self.UserTable.yview)
        self.UserTable.heading("USER No.",text="USER No.")
        self.UserTable.heading("Name",text="Name")
        self.UserTable.heading("Contact No",text="Contact No")
        self.UserTable.heading("Email",text="Email")
        '''
        self.UserTable.heading("Gender",text="Gender")
        self.UserTable.heading("Contact",text="Contact")
        self.UserTable.heading("Address",text="Address")'''
        
        self.UserTable['show']='headings'
        self.UserTable.column("USER No.",width=50)
        self.UserTable.column("Name",width=100)
        self.UserTable.column("Contact No",width=100)
        self.UserTable.column("Email",width=100)
        '''
        self.UserTable.column("Gender",width=100)
        self.UserTable.column("Contact",width=100)
        self.UserTable.column("Address",width=100)'''
        self.UserTable.pack(fill=BOTH,expand=1)
        self.showDetails()
        self.UserTable.bind("<ButtonRelease-1>",self.get_cursor)

    def get_cursor(self,ev):
        cursor_row=self.UserTable.focus()
        contents=(self.UserTable.item(cursor_row))
        row = contents['values']
        con=pymysql.connect(host="localhost",user='root',password="1234",database="mydata")
        cur=con.cursor()
        try:
            cur.execute("select * from user where user_no=%s",str(row[0]))
            rows=cur.fetchone()
            self.var_uno.set(rows[0])
            self.var_fname.set(rows[1])
            self.var_contact.set(rows[2])
            self.var_email.set(rows[3])
            self.var_securityQ.set(rows[4])
            self.var_SecurityA.set(rows[5])
            '''
            self.txtAddress.delete('1.0',END)
            self.txtAddress.insert(END,rows[6])'''
            con.close()
        except Exception as es:
            messagebox.showerror("Error",f"error due to {str(es)}",parent=self.root)
    
    def SearchBy(self):
        con=pymysql.connect(host="localhost",user='root',password="1234",database="mydata")
        cur=con.cursor()
        try:
            if self.SearchKeyword.get()=="Select Options":
                messagebox.showerror("Error","Please select any search by option",parent=self.root)
            elif self.searchtxt.get()=="":
                messagebox.showerror("Error","Search Area should not be emplty",parent=self.root)
            else:
                cur.execute("select * from user where "+self.SearchKeyword.get()+" LIKE '%"+self.searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.UserTable.delete(*self.UserTable.get_children())
                    for row in rows:
                        self.UserTable.insert('',END,values=row)
                    con.commit()
                    con.close()
                else:
                    messagebox.showerror("Error","No record Found !!!",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"error due to {str(es)}",parent=self.root)
    


    def Add_User(self):
        con=pymysql.connect(host="localhost",user='root',password="1234",database="mydata")
        cur=con.cursor()
        try:
            if self.var_uno.get()==""or self.var_email.get()=="" or self.var_fname.get()=="" or self.var_contact.get()=="": #self.class_.get()=="Select Class" or self.gender.get()=="Select Gender" or self.txtAddress.get('1.0',END)=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from user where user_no=%s",self.var_uno.get())
                emp_exist=cur.fetchone()
                if emp_exist!=None:
                    messagebox.showerror("Error","USER Id Already Exists",parent=self.root)
                else:    
                    cur.execute("insert into user values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_uno.get(),
                                                                                    self.var_fname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_SecurityA.get(),
                                                                                    self.var_pass.get(),
                                                                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("User","Record  added Successfully!!!",parent=self.root)
                    self.clear_details()
                   
        except Exception as es:
            messagebox.showerror("Error",f"error due to {str(es)}",parent=self.root)

    def showDetails(self):
        con=pymysql.connect(host="localhost",user='root',password="1234",database="mydata")
        cur=con.cursor()
        try:
            cur.execute("select * from user")
            rows=cur.fetchall()
            if rows!=None:
                self.UserTable.delete(*self.UserTable.get_children())
                for row in rows:
                    self.UserTable.insert('',END,values=row)
                con.close()
        except Exception as es:
            messagebox.showerror("Error",f"error due to {str(es)}",parent=self.root)

    def update_details(self):
        con=pymysql.connect(host="localhost",user='root',password="1234",database="mydata")
        cur=con.cursor()
        try:
            if self.var_uno.get()=="" or self.var_email.get()=="" or self.var_fname.get()=="" or self.var_contact.get()=="":
                #or self.txtAddress.get('1.0',END)=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select * from user where user_no=%s",self.var_uno.get())
                fetch_e=cur.fetchone()
                if fetch_e!=None:
                    cur.execute("update user set Name=%%,Contact=%%,Email=%%,securityQ=%%,SecurityA=%%,pass=%% where user_no=%%"(
                                                                                    self.var_fname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_SecurityA.get(),
                                                                                    self.var_pass.get(),
                                                                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("User","Record  updated Successfully!!!",parent=self.root)
                    self.showDetails()
                else:
                    messagebox.showerror("Error","Invalid User Id ",parent=self.root)
        except Exception as es:
            con.close()
            messagebox.showerror("Error",f"error due to {str(es)}",parent=self.root)
    def clear_details(self):
        self.var_uno.set("")
        self.var_fname.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_securityQ.set("Select Question")
        self.var_SecurityA.set("")
        self.var_pass.set("")
        self.showDetails()
    
    def delete_details(self):
        con=pymysql.connect(host="localhost",user='root',password="1234",database="mydata")
        cur=con.cursor()
        try:
            if self.var_uno.get()=="":
                messagebox.showerror("Error","User Id must be required",parent=self.root)
            else:
                cur.execute("select * from user where user_no=%s",self.var_uno.get())
                row=cur.fetchone()
                if row!=None:
                    yes_no=messagebox.askyesno("Delete Record",f"Are you sure do Delete the Record of \nUser ID : {self.var_uno.get()}\nName : {str(row[1])}",parent=self.root)
                    if yes_no>0:
                        cur.execute("delete from user where user_no=%s",self.var_uno.get())    
                        con.commit()
                        con.close()
                        messagebox.showinfo("USER","Record  deleted Successfully!!!",parent=self.root)
                        self.clear_details()
                        self.showDetails()
                    else:
                        return
                else:
                    con.close()
                    messagebox.showerror("Error","Invalid USER ID",parent=self.root)
        except Exception as es:
            con.close()
            messagebox.showerror("Error",f"error due to {str(es)}")
root=Tk()
ob=User(root)
root.mainloop()

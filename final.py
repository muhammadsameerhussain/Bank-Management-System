#import all the modules
from tkinter import *
import tkinter.messagebox
import datetime
import sqlite3
import math
import os
import random
from prettytable import PrettyTable


conn = sqlite3.connect("BMS.db")
c = conn.cursor()

############################################################################INSERTION###########################################################################
class insertion:
    def insert(self):
        self.name=self.acc_name_e.get()
        self.num=self.acc_num_e.get()
        self.emadd=self.email_e.get()
        self.bid=self.branch_e.get()
        self.balance=self.bal_e.get()
        self.nic=self.cnic_e.get()
        self.mf=self.gender_e.get()
        self.ag=self.age_e.get()
        self.phone=self.contact_e.get()
        
        conn = sqlite3.connect("BMS.db")
        with conn:
            c = conn.cursor()
            if self.name=='':
                tkinter.messagebox.showinfo("ERROR", "PLEASE ENTER ACCOUNT NAME")
            elif self.num=='':
                tkinter.messagebox.showinfo("ERROR", "PLEASE ENTER ACCOUNT NUMBER")
            elif self.bid=='':
                tkinter.messagebox.showinfo("ERROR", "PLEASE ENTER BRANCH ID")
            elif self.balance=='':
                tkinter.messagebox.showinfo("ERROR", "PLEASE ENTER AMOUNT")
  
            elif self.nic=='':
                tkinter.messagebox.showinfo("ERROR", "PLEASE ENTER CNIC")
            elif self.mf=='':
                tkinter.messagebox.showinfo("ERROR", "PLEASE ENTER YOUR GENDER")
            elif self.ag=='':
                tkinter.messagebox.showinfo("ERROR", "PLEASE ENTER CNIC")
            elif self.phone=='':
                tkinter.messagebox.showinfo("ERROR", "PLEASE ENTER contact")
               
            else:
                c.execute('INSERT INTO ACCINFO (ACCNO,ACCNAME,EMAIL,BALANCE, BRANCH_ID,CNIC,GENDER,AGE,CONTACT) VALUES (?,?,?,?,?,?,?,?,?)',(self.num,self.name,self.emadd,self.balance,self.bid,self.nic,self.mf,self.ag,self.phone))
                tkinter.messagebox.showinfo("Success", "Successfully added to the database")
#########################################################################DELETE ACC##################################################################
class deleteacc:
    def remove(self):
        self.a=self.anum.get()
        conn = sqlite3.connect("BMS.db")
        with conn:
            c = conn.cursor()
            if self.a=='':
                tkinter.messagebox.showinfo("ERROR", "PLEASE ENTER ACCOUNT NUMBER")
            else:
                c.execute('DELETE FROM ACCINFO WHERE ACCNO=?',(self.a,))
                tkinter.messagebox.showinfo("SUCCESS", "ACCOUNT DELETED")

######################################################################OLDLOGIN###########################################################################
class oldlogin:
    def login(self):
        self.accno=self.password.get()
        self.accname=self.username.get()
        conn = sqlite3.connect("BMS.db")
        with conn:
            c=conn.cursor()
            c.execute('SELECT * FROM ACCINFO WHERE ACCNO=? AND ACCNAME=?',(self.accno,self.accname))
            results = c.fetchall()

            if results:
                root5 = Toplevel(self.master)
                transace_Gui=transaction(root5)
            else:
                tkinter.messagebox.showinfo("ERROR", "WRONG USERNAME OR ACC NUMBER")
#####################################################################WITHDRAWL###############################################################################
class withsub:
    def subt(self):
        self.acct=self.no.get()
        self.amt=self.deposit.get()
        conn = sqlite3.connect("BMS.db")
        with conn:
            c=conn.cursor()
            a=c.execute('SELECT * FROM ACCINFO WHERE ACCNO=?',(self.acct,))
            for self.r in a:
                self.get_accno = self.r[0]
                self.get_accname = self.r[1]
                self.get_email = self.r[2]
                self.get_branchid = self.r[3]
                self.get_balance = self.r[4]
            self.newbal=float(self.get_balance)-float(self.amt)
            if self.newbal<0:
                tkinter.messagebox.showinfo("ERROR", "NOT ENOUGH BALANCE")
            else:
                c.execute("UPDATE ACCINFO SET balance=? WHERE balance=?",(self.newbal,self.get_balance))
                tkinter.messagebox.showinfo("SUCCESS", "AMOUNT WITHDRAWN")
#####################################################################DEPOSIT####################################################################################
class depadd:
    def add(self):
        self.acct=self.no.get()
        self.amt=self.deposit.get()
        conn = sqlite3.connect("BMS.db")
        with conn:
            c=conn.cursor()
            a=c.execute('SELECT * FROM ACCINFO WHERE ACCNO=?',(self.acct,))
            for self.r in a:
                self.get_accno = self.r[0]
                self.get_accname = self.r[1]
                self.get_email = self.r[2]
                self.get_branchid = self.r[3]
                self.get_balance = self.r[4]

            self.newbal=int(self.get_balance)+int(self.amt)
            if self.newbal>10000000:
                tkinter.messagebox.showinfo("ALERT", "TAX KON DEGA??")
            else:
                c.execute("UPDATE ACCINFO SET balance=? WHERE balance=?",(self.newbal,self.get_balance))
                tkinter.messagebox.showinfo("SUCCESS", "AMOUNT DEPOSITED")
###############################################################################EMPLOYEE DETAILS####################################################################
class details:
    def get_details(self):
        self.name=self.username.get()
        self.num=self.password.get()
        conn = sqlite3.connect("BMS.db")
        with conn:
            c=conn.cursor()
            if self.name == '' or self.num == '':
                tkinter.messagebox.showinfo("Error", "Please fill all the entries")
            else:
                c.execute('SELECT * FROM employee where empno=?',(self.num,))
                
                col_names = [cn[0] for cn in c.description]
                rows = c.fetchall()
 
                q = PrettyTable(col_names)
                q.align[col_names[1]] = "l"
                q.align[col_names[2]] = "r"
                q.padding_width = 1
                for row in rows:
                    q.add_row(row)
 
                print (q)
                tabstring = q.get_string()
#############################################################################MAIN PAGE#######################################################################                
class Welcome():
    def __init__(self,master):    
        self.master = master
        self.master.geometry("600x400")
        self.master.title("WELCOME")
        self.master.configure(bg="black")
        window_pic=PhotoImage(file='bank.gif')
        self.window_label=Label(self.master,image=window_pic)
        self.window_label.image=window_pic
        self.window_label.pack()
    
        #TITLE
        self.heading = Label(self.master, text ="WELCOME TO BANK", font=('myraid 20 bold'), fg="white",bg="black")
        self.heading.place(x=180, y=10)

        #BUTTON MANAGER
        self.manager_btn= Button(self.master, text="MANAGER",font=('Fuzzco 12 bold'), width=22, height=2, fg='black',command= self.new_manager )
        self.manager_btn.place(x=60, y=90)

        #BUTTON NEW ACC
        self.emp_btn= Button(self.master, text="NEW ACCOUNT",font=('Fuzzco 12 bold'), width=22, height=2, fg='black', command = self.new_acc)
        self.emp_btn.place(x=60, y=155)

        #BUTTON OLD ACC
        self.about_btn= Button(self.master, text="OLD ACCOUNT",font=('Fuzzco 12 bold'), width=22, height=2, fg='black',command = self.old_acc)
        self.about_btn.place(x=60, y=220)

        #BUTTON about us
        self.about_btn= Button(self.master, text="ABOUT US",font=('Fuzzco 12 bold'), width=22, height=2, fg='black',command = self.about)
        self.about_btn.place(x=60, y=285)

        
    def new_manager(self):
        
        root2 = Toplevel(self.master)
        manager_Gui=manager(root2)
    


    def new_acc(self):
        root3 = Toplevel(self.master)
        new_Gui=new_account(root3)

    def old_acc(self):
        root4 = Toplevel(self.master)
        old_Gui=old_account(root4)

    def about(self):
        root9 = Toplevel(self.master)
        about_gui = about_us(root9)
        
############################################################################ABOUT US###########################################################################
class about_us():
    def __init__(self,master):

        self.master = master
        self.master.geometry("600x400")
        self.master.title("OLD ACCOUNT")
        self.master.configure(bg="black")

        
        window_pic=PhotoImage(file='bank.gif')
        self.window_label=Label(self.master,image=window_pic)
        self.window_label.image=window_pic
        self.window_label.pack()

        self.text=Label(self.master,text="Welcome to the MyBank info site..... \n      This bank is sponserd by SHF group.inc \n          founders of this bank is \n    HUZAIFA SULTAN RollNo # 69 \n     SAMEER HUSSAIN RollNo #127 \n      FAIZAN HUSSAIN KHAN RollNo #59 \n     CONTACT details# 03345655489 \n       Email Address # \n      www.SHFgroupstech@gmail.com \n   Visit Our Website # SHF group of tech \n Please give us the feedback so we can improve",font=("centaur 17"),fg='white',bg="black")
        self.text.place(x=100,y=50)

        #home button
        self.home_btn= Button(self.master, text="BACK",font=('Fuzzco 12 bold'), width=14, height=1, fg='black',command = self.back)
        self.home_btn.place(x=420, y=350)
        
    def back(self):
        self.master.destroy()
        
############################################################################TRANSACTION######################################################################
class transaction():    
    def __init__(self,master):
        self.master = master
        self.master.geometry("600x400")
        self.master.title("OLD ACCOUNT")
        self.master.configure(bg="black")

        
        window_pic=PhotoImage(file='bank.gif')
        self.window_label=Label(self.master,image=window_pic)
        self.window_label.image=window_pic
        self.window_label.pack()

         
        #TITLE
        self.heading = Label(self.master, text ="SELECT YOUR DESIRED TRANSACTION", font=('myraid 20 bold'), fg="white",bg="black")
        self.heading.place(x=30, y=10)

        #withdrawl button
        self.submit_btn= Button(self.master, text="WITHDRAWL",font=('Fuzzco 12 bold'), width=22, height=2, fg='black',command = self.withdrawl)
        self.submit_btn.place(x=25, y=70)

        #deposit button
        self.deposit_btn= Button(self.master, text="DEPOSIT",font=('Fuzzco 12 bold'), width=22, height=2, fg='black',command = self.deposit)
        self.deposit_btn.place(x=25, y=130)

        #details button
        self.deposit_btn= Button(self.master, text="DETAILS",font=('Fuzzco 12 bold'), width=22, height=2, fg='black',command = self.detail)
        self.deposit_btn.place(x=25, y=190)

        #delete button
        self.deposit_btn= Button(self.master, text="DELETE",font=('Fuzzco 12 bold'), width=22, height=2, fg='black',command = self.dele)
        self.deposit_btn.place(x=25, y=250)

        
        
        #home button
        self.home_btn= Button(self.master, text="BACK",font=('Fuzzco 12 bold'), width=14, height=1, fg='black',command = self.Home2)
        self.home_btn.place(x=420, y=350)
        
    def Home2(self):
        self.master.destroy()

    def deposit(self):
        root6 = Toplevel(self.master)
        deposit_Gui=deposit_amount(root6)

    def withdrawl(self):
        root7 = Toplevel(self.master)
        withdrawl_Gui=withdrawl_amount(root7)

    def detail(self):
        root8 = Toplevel(self.master)
        detail_gui = detail_user(root8)
    def dele(self):
        root9 = Toplevel(self.master)
        del_gui = delete_user(root9)
        
###########################################################################DELETE USER########################################################################
class delete_user(deleteacc):
    def __init__(self,master):
        self.master = master
        self.master.geometry("600x400")
        self.master.title("OLD ACCOUNT")
        self.master.configure(bg="black")

        
        window_pic=PhotoImage(file='bank.gif')
        self.window_label=Label(self.master,image=window_pic)
        self.window_label.image=window_pic
        self.window_label.pack()

        self.anum = StringVar()

        #title
        self.heading = Label(self.master, text ="PLEASE ENTER ACCOUNT NUMBER TO DELETE ACCOUNT", font=('myraid 16 bold'), fg="white",bg="black")
        self.heading.place(x=0, y=20)

        self.no_l = Label(self.master, text="Enter your account number ", width=20,height=1,font=("bold",10))
        self.no_l.place(x=110,y=92)

        self.no_e = Entry(self.master,bd=5,textvariable=self.anum,width=30)
        self.no_e.place(x=280,y=90)

        
        #deposit button
        self.deposit_btn= Button(self.master, text="DELETE",font=('Fuzzco 12 bold'), width=22, height=2, fg='black',command = self.remove)
        self.deposit_btn.place(x=210, y=140)

        #back button
        self.home_btn= Button(self.master, text="BACK",font=('Fuzzco 12 bold'), width=14, height=1, fg='black',command = self.back3)
        self.home_btn.place(x=420, y=350)
    def back3(self):
        self.master.destroy()

        


#################################################################################class det########################################################################
class det:
    def get_det(self):
        #self.name=self.username.get()
        self.num=self.no_e.get()
        conn = sqlite3.connect("BMS.db")
        with conn:
            c=conn.cursor()
            if self.no_e == '' :#or self.num == '':
                tkinter.messagebox.showinfo("Error", "Please fill all the entries")
            else:
                c.execute('SELECT * FROM accinfo where accno=?',(self.num,))
                
                col_names = [cn[0] for cn in c.description]
                rows = c.fetchall()
 
                q = PrettyTable(col_names)
                q.align[col_names[1]] = "l"
                q.align[col_names[2]] = "r"
                q.padding_width = 1
                for row in rows:
                    q.add_row(row)
 
                print (q)
                tabstring = q.get_string()


        
#######################################################################USER DETAIL#########################################################################   

class detail_user(det):
    def __init__(self,master):

        self.master = master
        self.master.geometry("600x400")
        self.master.title("OLD ACCOUNT")
        self.master.configure(bg="black")

        
        window_pic=PhotoImage(file='bank.gif')
        self.window_label=Label(self.master,image=window_pic)
        self.window_label.image=window_pic
        self.window_label.pack()

        self.no = StringVar()
        #self.deposit = StringVar()
        #TITLE
        self.heading = Label(self.master, text ="PLEASE PROVIDE YOUR AMOUNT", font=('myraid 20 bold'), fg="white",bg="black")
        self.heading.place(x=60, y=20)
        
        #entry ACCNO
        self.no_l = Label(self.master, text="Enter your account number ", width=20,height=1,font=("bold",10))
        self.no_l.place(x=110,y=92)

        self.no_e = Entry(self.master,bd=5,textvariable=self.no,width=30)
        self.no_e.place(x=280,y=90)

        #details button
        self.deposit_btn= Button(self.master, text="VIEW",font=('Fuzzco 12 bold'), width=22, height=2, fg='black',command = self.get_det)
        self.deposit_btn.place(x=210, y=140)

        #back button
        self.home_btn= Button(self.master, text="BACK",font=('Fuzzco 12 bold'), width=14, height=1, fg='black',command = self.back2)
        self.home_btn.place(x=420, y=350)

    def back2(self):
        self.master.destroy()


     
        

########################################################################deposit classs##########################################################################
class deposit_amount(depadd):
    def __init__(self,master):

        self.master = master
        self.master.geometry("600x400")
        self.master.title("OLD ACCOUNT")
        self.master.configure(bg="black")

        
        window_pic=PhotoImage(file='bank.gif')
        self.window_label=Label(self.master,image=window_pic)
        self.window_label.image=window_pic
        self.window_label.pack()

        self.no = StringVar()
        self.deposit = StringVar()
        #TITLE
        self.heading = Label(self.master, text ="PLEASE PROVIDE YOUR AMOUNT", font=('myraid 20 bold'), fg="white",bg="black")
        self.heading.place(x=60, y=20)
        
        #entry ACCNO
        self.no_l = Label(self.master, text="Enter your account number ", width=20,height=1,font=("bold",10))
        self.no_l.place(x=110,y=92)

        self.no_e = Entry(self.master,bd=5,textvariable=self.no,width=30)
        self.no_e.place(x=280,y=90)

        #entry depoSIT
        self.deposit_l = Label(self.master, text="Enter your deposit amount ", width=20,height=1,font=("bold",10))
        self.deposit_l.place(x=110,y=152)

        self.deposit_e = Entry(self.master,bd=5,textvariable=self.deposit,width=30)
        self.deposit_e.place(x=280,y=148)



        #deposit button
        self.deposit_btn= Button(self.master, text="DEPOSIT",font=('Fuzzco 12 bold'), width=22, height=2, fg='black',command = self.add)
        self.deposit_btn.place(x=210, y=240)


        

        #home button
        self.home_btn= Button(self.master, text="BACK",font=('Fuzzco 12 bold'), width=14, height=1, fg='black',command = self.Home3)
        self.home_btn.place(x=420, y=350)
    def Home3(self):
        self.master.destroy()

        

##############################################################withdrawl class#####################################################################################    
class withdrawl_amount(withsub):
        def __init__(self,master):

            self.master = master
            self.master.geometry("600x400")
            self.master.title("OLD ACCOUNT")
            self.master.configure(bg="black")

            
            window_pic=PhotoImage(file='bank.gif')
            self.window_label=Label(self.master,image=window_pic)
            self.window_label.image=window_pic
            self.window_label.pack()

            self.no = StringVar()
            self.deposit = StringVar()
            #TITLE
            self.heading = Label(self.master, text ="PLEASE PROVIDE YOUR AMOUNT", font=('myraid 20 bold'), fg="white",bg="black")
            self.heading.place(x=60, y=20)
            
            #entry accno
            self.no_l = Label(self.master, text="Enter your accountnumber ", width=20,height=1,font=("bold",10))
            self.no_l.place(x=108,y=92)

            self.no_e = Entry(self.master,bd=5,textvariable=self.no,width=30)
            self.no_e.place(x=280,y=90)

            #amount
            self.deposit_l = Label(self.master, text="Enter your withdrawl amount ", width=20,height=1,font=("bold",10))
            self.deposit_l.place(x=108,y=152)

            self.deposit_e = Entry(self.master,bd=5,textvariable=self.deposit,width=30)
            self.deposit_e.place(x=280,y=150)


            #deposit button
            self.deposit_btn= Button(self.master, text="WITHDRAWL",font=('Fuzzco 12 bold'), width=22, height=2, fg='black',command=self.subt)
            self.deposit_btn.place(x=210, y=240)
            

            #home button
            self.home_btn= Button(self.master, text="BACK",font=('Fuzzco 12 bold'), width=14, height=1, fg='black',command = self.Home4)
            self.home_btn.place(x=420, y=350)
        def Home4(self):
            self.master.destroy()



#################################################################old account class###########################################################################        
class old_account(oldlogin):
    def __init__(self,master):
        self.master = master
        self.master.geometry("600x400")
        self.master.title("OLD ACCOUNT")
        self.master.configure(bg="black")
        
        window_pic=PhotoImage(file='bank.gif')
        self.window_label=Label(self.master,image=window_pic)
        self.window_label.image=window_pic
        self.window_label.pack()
    
        
        #TITLE
        self.heading = Label(self.master, text ="PLEASE PROVIDE YOUR DETAILS", font=('myraid 20 bold'), fg="white",bg="black")
        self.heading.place(x=80, y=20)

        #entry box
        self.username = StringVar()
        self.password = StringVar()

        #label and entry
        self.emp_name_label = Label(self.master,bg="light grey", text = "ACC NAME * ",font="myraid 12").place(x=266,y=85)
        self.acc_name_e = Entry(self.master,bg="lightgrey",textvariable=self.username,bd=10,width=25).place(x=235,y=115)

        self.emp_no_label = Label(self.master,bg="light grey", text = "ACC NUM * ",font="myraid 12").place(x=270,y=170)
        self.acc_no_e = Entry(self.master,bg="lightgrey",textvariable=self.password,bd=10,width=25).place(x=235,y=200)

        #submit button
        self.submit_btn= Button(self.master, text="SUBMIT",font=('Fuzzco 12 bold'), width=14, height=2, fg='black',command = self.login)
        self.submit_btn.place(x=245, y=260)

        #home button
        self.home_btn= Button(self.master, text="BACK",font=('Fuzzco 12 bold'), width=14, height=1, fg='black',command = self.home)
        self.home_btn.place(x=420, y=350)
    def home(self):
        self.master.destroy()            
        


###########################################################################new account class######################################################################
class new_account(insertion):

    def __init__(self,master):

        

        self.master = master
        self.master.geometry("600x400")
        self.master.title("NEW ACCOUNT")
        self.master.configure(bg="black")

        window_pic=PhotoImage(file='bank.gif')
        self.window_label=Label(self.master,image=window_pic)
        self.window_label.image=window_pic
        self.window_label.pack() 

        #TITLE
        self.heading = Label(self.master, text ="REGISTRATION FORM", font=('myraid 20 bold'), fg="white",bg="BLACK")
        self.heading.place(x=180, y=20)

        #entry ACC NAME
        self.acc_name_l = Label(self.master, text="ACC NAME", width=20,height=1,font=("bold",7))
        self.acc_name_l.place(x=35,y=90)

        self.acc_name_e = Entry(self.master,bd=3)
        self.acc_name_e.place(x=170,y=90)

        #entry acc num
        self.acc_num_l = Label(self.master,text="Account NUM",width=20,height=1,font=("bold",7))
        self.acc_num_l.place(x=35,y=140)

        self.acc_num_e = Entry(self.master,bd=3)
        self.acc_num_e.place(x=170,y=140)

        #acc contact
        self.email_l = Label(self.master, text="EMAIL",width=20,height=1,font=("bold",7))
        self.email_l.place(x=190,y=285)

        self.email_e = Entry(self.master,bd=3)
        self.email_e.place(x=320,y=280)

        #branch id
        self.branch_l = Label(self.master, text="BRANCH ID",width=20,height=1,font=("bold",7))
        self.branch_l .place(x=325,y=90)

        self.branch_e = Entry(master,bd=3)
        self.branch_e.place(x=460,y=90)

        #cnic
        self.cnic_l = Label(self.master, text="CNIC",width=20,height=1,font=("bold",7))
        self.cnic_l .place(x=325,y=140)

        self.cnic_e = Entry(master,bd=3)
        self.cnic_e.place(x=460,y=140)


        #gender
        self.gender_l = Label(self.master, text="GENDER",width=20,height=1,font=("bold",7))
        self.gender_l .place(x=35,y=190)

        self.gender_e = Entry(master,bd=3)
        self.gender_e.place(x=170,y=190)

        #age
        self.age_l = Label(self.master, text="AGE",width=20,height=1,font=("bold",7))
        self.age_l .place(x=35,y=245)

        self.age_e = Entry(master,bd=3)
        self.age_e.place(x=170,y=240)

        #CONTACT
        self.contact_l = Label(self.master, text="CONTACT",width=20,height=1,font=("bold",7))
        self.contact_l .place(x=325,y=195)

        self.contact_e = Entry(master,bd=3)
        self.contact_e.place(x=460,y=190)

        #balance
        self.bal_l = Label(self.master, text="STARTING AMOUNT",width=20,height=1,font=("bold",7))
        self.bal_l .place(x=325,y=245)

        self.bal_e = Entry(master,bd=3)
        self.bal_e.place(x=460,y=240)


        #submit button
        self.submitbtn_l = Label(self.master, text = "").pack()
        self.submitbtn = Button(self.master, text = "Submit", width = 14, height = 2,command=self.insert).place(x=190,y=330)

        #home button
        self.home_btn_l = Label(self.master, text = "").pack()
        self.home_btn = Button(self.master, text = "BACK", width = 14, height = 2,command = self.Home).place(x=330,y=330)

    def Home(self):
        self.master.destroy()

 ###########################################################################classs manager##################################################################       
class manager(details):
    def __init__(self,master):
        self.master = master
        self.master.geometry("600x400")
        self.master.title("WELCOME MANAGER")
        self.master.configure(bg="black")
        
        window_pic=PhotoImage(file='bank.gif')
        self.window_label=Label(self.master,image=window_pic)
        self.window_label.image=window_pic
        self.window_label.pack()

        #TITLE
        self.heading = Label(self.master, text ="WELCOME MANAGER", font=('myraid 20 bold'), fg="white",bg="BLACK")
        self.heading.place(x=180, y=20)

        #entry box
        self.username = StringVar()
        self.password = StringVar()

        #label and entry
        self.emp_name_label = Label(self.master,bg="light grey", text = "EMP NAME * ",font="myraid 12").place(x=266,y=85)
        self.empname_entry = Entry(self.master,bg="lightgrey",textvariable= self.username,bd=10,width=25).place(x=235,y=115)

        self.emp_no_label = Label(self.master,bg="light grey", text = "EMP NUM * ",font="myraid 12").place(x=270,y=170)
        self.empno_entry = Entry(self.master,bg="lightgrey",textvariable= self.password,bd=10,width=25).place(x=235,y=200)

        #submit button
        self.submit_btn= Button(self.master, text="SUBMIT",font=('Fuzzco 12 bold'), width=14, height=2, fg='black',command=self.get_details)
        self.submit_btn.place(x=150, y=280)


        #back home
        self.back_btn= Button(self.master, text="BACK",font=('Fuzzco 12 bold'), width=14, height=2, fg='black',command = self.Home1)
        self.back_btn.place(x=340, y=280)
    def Home1(self):
        self.master.destroy()
        
def main():
    root = Tk()
    mygui = Welcome(root)
    root.mainloop()



if __name__ == '__main__':
    main()

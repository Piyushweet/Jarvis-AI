from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk    #pip install pillow
from tkinter import messagebox
import random
import time
import datetime

#import sys
#sys.path.insert(0, '/Users/aakar/Downloads/Python/Others/')
import User_login
import Admin_login
# Note:import main project file
# from main_project import FaceRecognitionSystem

def call_GUI1():
    win1 = Toplevel(root)
    Admin_login.Login_Window(win1)
    return

def call_GUI2():
    win2 = Toplevel(root)
    User_login.Login_Window(win2)
    return
'''
def main():
    root=Tk()
    app=Login_Window(root)
    root.mainloop()'''


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # self.bg=ImageTk.PhotoImage(file="images/SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        img1 = Image.open("images/2-AI-invades-automobile-industry-in-2019.jpeg")
        img1 = img1.resize((1530,800), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl=Label(self.root,image=self.photoImg1)
        bg_lbl.place(x=0,y=0,width=1530,height=800)

        title=Label(bg_lbl,text="JARVIS SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title.place(x=0,y=120,width=1550,height=45)

         # ==================== Project buttom(description) ==================================================
        # downtitle=Label(self.root,text="Note:Enter valid username and valid password",font=("times new roman",20,"bold"),bd=2,relief=RAISED,bg="white",fg="blue")
        # downtitle.place(x=0,y=740,width=1600,height=35)

        myname=Label(self.root,text="Developed By:KPA",fg="black",bg="white",font=("times new roman",18,"bold"))
        myname.place(x=0,y=0)
        
        img10 = Image.open("images/facial-recognition_0.jpg")
        img10 = img10.resize((500,120), Image.ANTIALIAS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        bg_lbl1=Label(bg_lbl,image=self.photoImg10)
        bg_lbl1.place(x=0,y=0,width=500,height=120)

        img11 = Image.open("images/facialrecognition.png")
        img11 = img11.resize((500,120), Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        bg_lbl22=Label(bg_lbl,image=self.photoImg11)
        bg_lbl22.place(x=500,y=0,width=500,height=120)

        img13 = Image.open("images/smart-attendance.jpg")
        img13 = img13.resize((550,120), Image.ANTIALIAS)
        self.photoImg13= ImageTk.PhotoImage(img13)
        bg_lbl12=Label(bg_lbl,image=self.photoImg13)
        bg_lbl12.place(x=1000,y=0,width=550,height=120)


        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=200,width=340,height=430)

        img1=Image.open("images/LoginIconAppl.png")
        img1=img1.resize((90,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=200,width=90,height=90)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=85)

        img4=Image.open("images/admin_login.jpg")
        img4=img4.resize((90,90),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lblimg4=Label(image=self.photoimage4,borderwidth=0)
        lblimg4.place(x=650,y=330,width=100,height=100)

        img2=Image.open("images/user_login.png")
        img2=img2.resize((90,90),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,borderwidth=0)
        lblimg2.place(x=650,y=470,width=100,height=100)

  

        # LoginButton
        btn_login=Button(frame,text="ADMIN Login",borderwidth=3,relief=RAISED,command=call_GUI1,cursor="hand2",font=("times new roman",16,"bold"),fg="white",bg="red" ,activebackground="#B00857")
        btn_login.place(x=150,y=160,width=150,height=35)

        btn_login1=Button(frame,text="USER Login",borderwidth=3,relief=RAISED,command=call_GUI2,cursor="hand2",font=("times new roman",16,"bold"),fg="white",bg="red" ,activebackground="#B00857")
        btn_login1.place(x=150,y=300,width=150,height=35)

    def return_login(self):
        self.root.destroy()
            



if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()
    '''main()
root = Tk()
root.title('Caller GUI')
root.minsize(720, 600)
button_1 = Button(root, text = 'Call GUI1', width = '20', height = '20', command = call_GUI1)
button_1.pack()
button_2 = Button(root, text = 'Call GUI2', width = '20', height = '20', command = call_GUI2)
button_2.pack()
root.mainloop()'''
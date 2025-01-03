from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tktimepicker import AnalogPicker, AnalogThemes
from PIL import ImageTk, Image
import mysql.connector
from tkcalendar import *
import re
import datetime
import mysql.connector


mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Divya@123', database = 'twinstop')
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE TwinStop")
#mycursor.execute("CREATE TABLE user_details(user_name VARCHAR(50), password VARCHAR(50))")
# mycursor.execute("CREATE TABLE travel_details( City VARCHAR(50),Date1 VARCHAR(50), Time1 VARCHAR(10))")

fonts=('Gabriola',25,'bold')
fonts2=('Palatino Linotype',15,'bold')
fonts1=('Gabriola',15,'bold')
root = Tk()
root.geometry("1399x758+100+58")
background_color = "lightblue"
root.configure(bg=background_color)
root.title("TWIN STOP")



def set_background(root, frame, image_path, width, height):
    # Load the image and resize it
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))

    image = ImageTk.PhotoImage(resized_image)

    label = Label(frame, image=image)
    label.image = image 

    label.place(relwidth=1, relheight=1)
class first_page:
    def __init__(self, root):
        self.root = root
        self.first_page_frame = Frame(self.root, width=1399, height=758, bg='#c3e8e1')
        self.first_page_frame.place(x=0, y=0)
        set_background(root, self.first_page_frame, "first.jpg", 1399, 758)
        
        # self.label = Label(self.first_page_frame, text="HOME PAGE", font=("Times", 35, 'bold'), fg="black",bg="#c3e8e1")
        # self.label.place(x=300, y=240)

        self.enter_details_btn = Button(self.first_page_frame, text='LOGIN', bg='#8581ef', fg='white',command=lambda:Login(self.root),height=1,width=15 ,font="Times",cursor='hand2', borderwidth=0, highlightthickness=0,activebackground='blue')
        self.enter_details_btn.place(x=870, y=16)

        self.show_details_btn = Button(self.first_page_frame, text='SIGN UP', bg='#8581ef', fg='white',command=lambda:SignUp(self.root),height=1,width=15,borderwidth=0, highlightthickness=0,cursor='hand2',font="Times", activebackground='blue')
        self.show_details_btn.place(x=1000, y=16)
class Login:
    def __init__(self, root):
        self.root = root
        self.login_frame = Frame(self.root, width=1399, height=758, bg='#aaa')
        self.login_frame.place(x=0, y=0)
        set_background(root, self.login_frame, "TS.png", 1399, 758)
        
        self.left_arrow = Image.open("left_arrow.png")
        self.left_arrow = self.left_arrow.resize((25, 25))  # Resize image if necessary
        self.left_arrow = ImageTk.PhotoImage(self.left_arrow)

        self.left_arrow_button = Button(self.login_frame, text=" ", image=self.left_arrow,command=lambda:first_page(self.root), compound=LEFT,bg="#e0f9e9",borderwidth=0, highlightthickness=0)
        self.left_arrow_button.pack(side=LEFT)
        self.left_arrow_button.place(x = 0, y = 0)

        self.user_name_entry = Entry(self.login_frame, width=13,border=0, font=fonts2,bg="#fdfaef")
        self.user_name_entry.place(x=880, y=320)
        self.user_name_entry.insert(0,"USERNAME")
        Frame(self.login_frame,width=295,height=2,bg='black').place(x=870,y=350)
        self.user_name_entry.bind("<FocusIn>",self.user_enter)
        self.user_name_entry.bind("<FocusOut>",self.user_leave)
        

        self.user_pass_entry = Entry(self.login_frame, width=13,border=0, font=fonts2,bg="#fdfaef")
        self.user_pass_entry.place(x=880, y=400)
        self.user_pass_entry.insert(0,"PASSWORD")
        Frame(self.login_frame,width=295,height=2,bg='black').place(x=870,y=430)
        self.user_pass_entry.bind("<FocusIn>",self.pass_enter)
        self.user_pass_entry.bind("<FocusOut>",self.pass_leave)
        self.user_pass_entry.bind("<Key>", self.on_key_press)



        self.submit_btn = Button(self.login_frame, text='LOGIN', bg='white', fg='steel blue', font=fonts2,command=self.check_function, cursor='hand2', activebackground='blue', width=15)
        self.submit_btn.place(x=920, y=490)

        self.signup_btn = Button(self.login_frame, text='SIGNUP', bg="white", fg='steel blue', font=fonts2,command= lambda:SignUp(self.root), cursor='hand2', activebackground='blue',width=15)
        self.signup_btn.place(x=1000, y=650)

        self.create = Label(self.login_frame, text='Dont have an account?', font=('Mixa-Trial Bold',15,'bold'), bg="#fdfaef",fg='black', width=25)
        self.create.place(x=940, y=599)
    
    
    def on_key_press(self, event):
        if self.user_pass_entry.get() == "PASSWORD":
            self.user_pass_entry.delete(0, END)
            self.user_pass_entry.config(show="*")
        else:
            self.user_pass_entry.config(show="*")


    def check_function(self):
        a = self.user_name_entry.get()
        b = self.user_pass_entry.get()
        if self.user_name_entry.get() == "" or self.user_pass_entry.get() == "":
            messagebox.showerror("Error", "ALL fields are required", parent=self.root)
        else:
            mycursor.execute("SELECT * FROM user_details")
            res = mycursor.fetchall()
            if((a, b) in res):
                messagebox.showinfo("Welcome", f"Welcome {self.user_name_entry.get()}")
                home=home_page(self.root)
            else:
                messagebox.showerror("Error","Invalid user name or password",parent=self.root)

    def user_enter(self, event):
        if self.user_name_entry.get()=="USERNAME":
            self.user_name_entry.delete(0,END)

    def pass_enter(self,event):
        if self.user_pass_entry.get()=="PASSWORD":
            self.user_pass_entry.delete(0,END)

    def user_leave(self,event):
        if self.user_name_entry.get() == "":
            self.user_name_entry.insert(0, "USERNAME")
    
    def pass_leave(self,event):
        if self.user_pass_entry.get() == "":
            self.user_pass_entry.insert(0, "PASSWORD")



class SignUp:
    def __init__(self, root):
        self.root = root

        self.signup_frame = Frame(self.root, width=1399, height=758, bg='#bbb')
        self.signup_frame.place(x=0, y=0)

        set_background(root, self.signup_frame, "logo1.png", 1399, 758)

        # set_background(root, self.signup_frame, "bg.png")

        # self.label = Label(self.signup_frame, text="", font=("Times", 35, 'bold'), fg="black", bg="white")
        # self.label.place(x=700, y=38)

        

        self.user_name = Label(self.signup_frame, text='USER NAME', font=fonts2, bg='white', fg='steel blue', width=10)
        self.user_name.place(x=770, y=200)
        self.user_name_entry = Entry(self.signup_frame, width=13, font=fonts2, bg='white')
        self.user_name_entry.place(x=1000, y=200)

        self.user_pass = Label(self.signup_frame, text='PASSWORD', font=fonts2, bg='white', fg='steel blue', width=10)
        self.user_pass.place(x=770, y=350)
        self.user_pass_entry = Entry(self.signup_frame, width=13, font=fonts2, bg='white', show="*")
        self.user_pass_entry.place(x=1000, y=350)

        self.con_user_pass = Label(self.signup_frame, text='CONFIRM\nPASSWORD', font=('Forte Regular',10,'bold'), bg='white', fg='steel blue', width=20)
        self.con_user_pass.place(x=770, y=500)
        self.con_user_pass_entry = Entry(self.signup_frame, width=13, font=fonts2, bg='white', show="*")
        self.con_user_pass_entry.place(x=1000, y=500)

        self.signup_btn = Button(self.signup_frame, text='SIGNUP', bg='white', fg='steel blue', font=fonts2,command=self.check_function, cursor='hand2', activebackground='blue')
        self.signup_btn.place(x=1100, y=600)

        # self.change_pwd_btn = Button(self.home_page_frame, text='Change pwd', bg='#93bce8', fg='black',command=lambda:change_pwd(self.root), font=fonts, cursor='hand2', activebackground='blue', borderwidth=0, highlightthickness=0)
        # self.change_pwd_btn.place(x=850, y=500)

    def check_function(self):
        a=self.user_name_entry.get()
        b=self.user_pass_entry.get()
        if self.user_name_entry.get() == "" or self.user_pass_entry.get() == "":
            messagebox.showerror("Error", "ALL fields are required", parent=self.root)
        elif self.user_pass_entry.get() == self.con_user_pass_entry.get():
            sql = "INSERT INTO user_details(user_name, password)VALUES(%s, %s)"
            val = (a,b)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Welcome", f"Welcome {self.user_name_entry.get()}")
            self.signup_btn = Button(self.signup_frame, text='SIGNUP', bg='white', fg='steel blue', font=fonts,command=home_page(self.root), cursor='hand2', activebackground='blue')
           # messagebox.showerror("Error","Re-enter password",parent=self.root)
        else:
            messagebox.showerror("Error", "Re-enter password", parent=self.root)
            #messagebox.showinfo("Welcome", f"Welcome {self.user_name_entry.get()}")
           # self.signup_btn = Button(self.signup_frame, text='SIGNUP', bg='white', fg='steel blue', font=fonts,command=Login(self.root), cursor='hand2', activebackground='blue')

class change_pwd:
    def __init__(self, root):
        self.root = root
        self.root.title('CHANGE PASSWORD')
        self.pwd_frame = Frame(self.root, width=1399, height=758, bg='#ccc')
        self.pwd_frame.place(x=0, y=0)

        self.old_label = Label(self.pwd_frame, text="CURRENT PASSWORD", font=("Times", 35, 'bold'), fg="black",bg="#c3e8e1")
        self.old_label.place(x=100, y=200)

        self.old_entry = Entry(self.pwd_frame, width=13, font=fonts, bg='white')
        self.old_entry.place(x=300, y=200)

        self.new_label = Label(self.pwd_frame, text="NEW PASSWORD", font=("Times", 35, 'bold'), fg="black",bg="#c3e8e1")
        self.new_label.place(x=100, y=250)

        self.new_entry = Entry(self.pwd_frame, width=13, font=fonts, bg='white')
        self.new_entry.place(x=300, y=250)

        self.con_new_label = Label(self.pwd_frame, text="NEW PASSWORD", font=("Times", 35, 'bold'), fg="black",bg="#c3e8e1")
        self.con_new_label.place(x=100, y=300)

        self.con_new_entry = Entry(self.pwd_frame, width=13, font=fonts, bg='white')
        self.con_new_entry.place(x=300, y=350)

        self.change_btn = Button(self.pwd_frame, text='CHANGE', bg='white', fg='steel blue',command=self.check, font=fonts, cursor='hand2', activebackground='blue')
        self.change_btn.place(x=450, y=440)

    def check(self):
        global current_user, current_user_pwd
        a = self.old_entry.get()
        b = self.new_entry.get()
        c = self.con_new_entry.get()
        # current_user = ""
        # current_user_pwd = ""
        if(b == c):
            # mycursor.execute("SELECT * FROM user_details")
            if(a == current_user_pwd):
                mycursor.execute("UPDATE user_details SET password = %s WHERE user_name = %s",(b, current_user))
                mydb.commit()
                messagebox.showinfo("", "password has been changed successfully", parent=self.root)
            else:
                print(a, current_user_pwd)
                messagebox.showerror("Error", "user name and password doesnt match", parent=self.root)
        else:
            messagebox.showerror("Error", "re-enter password", parent=self.root)


# UPDATE Customers
# SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
# WHERE CustomerID = 1;


class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title('WELCOME TO THE DASHBOARD')
        self.login_frame = Frame(self.root, width=1399, height=758, bg='#ccc')
        self.login_frame.place(x=0, y=0)

        set_background(root, self.login_frame, "b1.png", 1399, 758)
        

        # set_background(root, self.login_frame, ".png")
       
        self.left_arrow = Image.open("left_arrow.png")
        self.left_arrow = self.left_arrow.resize((25, 25))  # Resize image if necessary
        self.left_arrow = ImageTk.PhotoImage(self.left_arrow)

        self.left_arrow_button = Button(self.login_frame, text=" ", image=self.left_arrow,command=lambda:home_page(self.root), compound=LEFT,bg='#f0f4ec',borderwidth=0, highlightthickness=0)
        self.left_arrow_button.pack(side=LEFT)
        self.left_arrow_button.place(x = 0, y = 0)

        # self.right_arrow = Image.open("right_arrow.png")
        # self.right_arrow = self.right_arrow.resize((25, 25))  # Resize image if necessary
        # self.right_arrow = ImageTk.PhotoImage(self.right_arrow)

        # self.right_arrow_button = Button(self.login_frame, text=" ", image=self.right_arrow,compound=LEFT)
        # self.right_arrow_button.pack(side=LEFT)
        # self.right_arrow_button.place(x = 30, y = 0)
    

        self.label = Label(self.login_frame, text="ENTER DETAILS", font=("Times", 40, 'bold'), fg="black",bg="#c3e8e1")
        self.label.place(x=360, y=200)

        self.user_city = Label(self.login_frame, text='SEARCH FOR CITY', font=fonts, bg='#c3e8e1', fg='steel blue', width=20)
        self.user_city.place(x=360, y=270)
        # self.user_city_entry = Entry(self.login_frame, width=13, font=fonts, bg='white')
        # self.user_city_entry.insert(0, "select dae")
        # self.user_date_entry.bind("<<ComboboxSelected>>",self)
        self.lists=['Amalapuram','Bhimavaram','Eluru','Hyberabad','Palakollu','Rajamundry','Vijayawada']
        self.citylist=StringVar(root)
        self.citylist.set("Select City")
        self.menu=OptionMenu(root,self.citylist,*self.lists)
        self.menu.place(x=700,y=270,width=185,height=60)
        self.menu.config(bg="white",font=fonts)


        self.city_icon = Image.open("city_icon.jpg")
        self.city_icon = self.city_icon.resize((55, 55))  # Resize image if necessary
        self.city_icon = ImageTk.PhotoImage(self.city_icon)

        self.city_button = Button(self.login_frame, text=" ", image=self.city_icon, compound=LEFT)
        self.city_button.pack(side=LEFT, padx=5, pady=5)
        self.city_button.place(x = 850, y = 270)

        self.user_date = Label(self.login_frame, text='DATE', font=fonts, bg='#c3e8e1', fg='steel blue', width=10)
        self.user_date.place(x=450, y=450)
        self.user_date_entry = Entry(self.login_frame, width=13, font=fonts, bg='white')
        self.user_date_entry.place(x=800, y=450)
        self.user_date_entry.insert(30, "    Select Date")
        self.user_date_entry.bind("<1>",self.pick_date)

        # Load calendar icon image
        self.calendar_icon = Image.open("calendar_icon.jpg")
        self.calendar_icon = self.calendar_icon.resize((55, 55))  # Resize image if necessary
        self.calendar_icon = ImageTk.PhotoImage(self.calendar_icon)

        self.calendar_button = Button(self.login_frame, text=" ", image=self.calendar_icon, compound=LEFT, command=self.pick_date)
        self.calendar_button.pack(side=LEFT, padx=5, pady=5)
        self.calendar_button.place(x = 1000, y = 450)



        self.con_user_time = Label(self.login_frame, text='CONVENIENT TIME', font=fonts,bg='#c3e8e1', fg='steel blue',width=20)
        self.con_user_time.place(x=450, y=550)
        self.con_user_time_entry = Entry(self.login_frame, width=13, font=('Gabriola',25,'bold'), bg='white')
        self.con_user_time_entry.place(x=800, y=550)
        self.con_user_time_entry.insert(0, "    Select Time")
        self.con_user_time_entry.bind("<1>",self.pick_time)

        self.user_mail = Label(self.login_frame, text='EMAIL', font=fonts,bg='#c3e8e1', fg='steel blue',width=20)
        self.user_mail.place(x = 400, y = 650)
        self.user_mail_entry = Entry(self.login_frame, width=13, font=fonts, bg='white')
        self.user_mail_entry.place(x = 750, y = 650)

        self.clock_icon = Image.open("clock_icon.jpg")
        self.clock_icon = self.clock_icon.resize((55, 55))  # Resize image if necessary
        self.clock_icon = ImageTk.PhotoImage(self.clock_icon)

        self.clock_button = Button(self.login_frame, text=" ", image=self.clock_icon, compound=LEFT, command=self.pick_time)
        self.clock_button.pack(side=LEFT, padx=5, pady=5)
        self.clock_button.place(x = 1000, y = 550)

        self.enter_btn = Button(self.login_frame, text='ENTER', bg='white', fg='steel blue',font=('Times',20,'bold'), command =self.enter_function, cursor='hand2', activebackground='blue')
        self.enter_btn.place(x=600, y=650)



    def enter_function(self):
        a=self.citylist.get()
        b=self.user_date_entry.get()
        c=self.con_user_time_entry.get()
        sql = "INSERT INTO travel_details(city,date1,time1)VALUES(%s,%s, %s)"
        val = (a,b,c)
        mycursor.execute(sql, val)
        mydb.commit()
        student_details(self.root)

    def pick_date(self, event = None):
        global cal,date_window
        date_window = Toplevel()
        date_window.grab_set()
        date_window.title("Chose date")
        date_window.geometry("250x220+1200+380")
        date_window.resizable(False, False)
        
        cal = Calendar(date_window, selectmode = "day", date_pattern = "mm/dd/yyyy")
        cal.place(x=0, y=0)

        done_btn = Button(date_window, text = "Submit", command = self.grab_date)
        done_btn.place(x=80, y=190)

    def grab_date(self):
        self.user_date_entry.delete(0, END)
        self.user_date_entry.insert(0, cal.get_date())
        date_window.destroy()

    def pick_time(self, event = None):
        global time_window, time_picker

        time_window = Toplevel()
        time_window.grab_set()
        time_window.title("Chose time")
        time_window.geometry("380x410+1100+360")
        time_window.resizable(False, False)

        time_picker = AnalogPicker(time_window)
        # time_picker.pack(expand=False, fill="both")
        time_picker.place(x=0, y=0)

        theme = AnalogThemes(time_picker)
        theme.setNavyBlue()

        update_button = Button(time_window, text="Update", command=self.update_selected_time)
        update_button.pack(pady=5)
        update_button.place(x=175, y=375)

    def update_selected_time(self):
        selected_time = time_picker.time()
        self.con_user_time_entry.delete(0, END)
        self.con_user_time_entry.insert(0, selected_time)
        time_window.destroy()
        


class home_page:
    def __init__(self, root):
        self.root = root
        self.home_page_frame = Frame(self.root, width=1399, height=758, bg='#93bce8')
        self.home_page_frame.place(x=0, y=0)
        
        set_background(root, self.home_page_frame, "home.jpg", 1399, 758)

        self.left_arrow = Image.open("left_arrow.png")
        self.left_arrow = self.left_arrow.resize((25, 25))  # Resize image if necessary
        self.left_arrow = ImageTk.PhotoImage(self.left_arrow)

        self.left_arrow_button = Button(self.home_page_frame, text=" ", image=self.left_arrow,command=lambda:first_page(self.root), compound=LEFT,bg="#93bce8",borderwidth=0, highlightthickness=0)
        self.left_arrow_button.pack(side=LEFT)
        self.left_arrow_button.place(x = 0, y = 0)
        
        
        
        self.label = Label(self.home_page_frame, text="HOME PAGE", font=("Times", 35, 'bold'), fg="black",bg="#93bce8")
        self.label.place(x=850, y=235)

        self.enter_details_btn = Button(self.home_page_frame, text='Enter Details', bg='#93bce8', fg='black',command=lambda:Dashboard(self.root),borderwidth=0, highlightthickness=0, font=fonts, cursor='hand2', activebackground='blue')
        self.enter_details_btn.place(x=850, y=330)

        self.show_details_btn = Button(self.home_page_frame, text='Show Details', bg='#93bce8', fg='black',command=lambda:student_details(self.root),font=fonts ,borderwidth=0, highlightthickness=0, cursor='hand2', activebackground='blue')
        self.show_details_btn.place(x=850, y=415)
class student_details:
    def __init__(self, root):
        self.root = root
        # self.root.title('TWINSTOP')
        self.details_frame = Frame(self.root, width=1399, height=758, bg='#c3e8e1')
        self.details_frame.place(x=0, y=0)

        set_background(root, self.details_frame, "bg.jpg", 1399, 758)

        self.left_arrow = Image.open("left_arrow.png")
        self.left_arrow = self.left_arrow.resize((25, 25))  # Resize image if necessary
        self.left_arrow = ImageTk.PhotoImage(self.left_arrow)

        self.left_arrow_button = Button(self.details_frame, text=" ", image=self.left_arrow,command=lambda:home_page(self.root), compound=LEFT, bg="#93bce8",borderwidth=0, highlightthickness=0)
        self.left_arrow_button.pack(side=LEFT)
        self.left_arrow_button.place(x = 5, y = 5)

        self.current_date = str(datetime.datetime.now())[0:11]  # Get current date
        self.delete_query = "DELETE FROM travel_details WHERE date1 < %s"
        mycursor.execute(self.delete_query, (self.current_date,))
        mydb.commit()

        self.search_entry = Entry(self.details_frame, font=('verdana',12), width = 40)
        self.search_entry.place(x = 500, y = 250)
        self.search_entry.bind("<KeyRelease>", self.find)

        self.search_btn = Button(self.details_frame, text='Search', font=('verdana',12), bg='#0984e3',fg="#ffffff", command = self.find)
        self.search_btn.place(x = 400, y = 250)


        self.trv = ttk.Treeview(self.details_frame, columns=(1,2,3, 4), height=8, show="headings", selectmode = "browse", style = "Custom.Treeview")
        self.trv.place(x = 400, y = 300)
        self.trv.bind("<Motion>", self.on_hover)
        # self.trv.grid(row = 1, column = 1, padx = 20, pady = 20)

        # self.trv["columns"] = ("1", "2", "3")


        self.trv.column(1, anchor=CENTER, stretch=NO, width=100)
        self.trv.column(2, anchor=CENTER, stretch=NO, width=100)
        self.trv.column(3, anchor=CENTER, stretch=NO, width=100)
        self.trv.column(4, anchor=CENTER, stretch=NO, width=200)

        self.trv.heading(1, text='CITY')
        self.trv.heading(2, text='DATE')
        self.trv.heading(3, text='TIME')
        self.trv.heading(4, text='MAIL')

        self.style = ttk.Style()
        self.style.theme_use("default")  # Use the default theme# Define custom style for the Treeview
        self.style.configure("Custom.Treeview", background="#c3e8e1", foreground="black", rowheight=30, fieldbackground="#c3e8e1", font=("verdana", 10))

    
        self.vertical_scroll = ttk.Scrollbar(self.details_frame, orient = "vertical", command = self.trv.yview)
        self.trv.configure(yscrollcommand = self.vertical_scroll.set)
        self.vertical_scroll.place(x = 900, y = 300, height = 260)

        mycursor.execute('SELECT * FROM travel_details')

        for i2 in mycursor:
            i = list(i2)
            i[1] = i[1].strftime('%d/%m/%Y')
            start_of_day = datetime.datetime.combine(datetime.date.today(), datetime.time(0, 0, 0))
            result_datetime = start_of_day + i[2]
            i[2] = result_datetime.strftime('%I:%M:%S %p')
            # i[2] = i[2].strftime('%H:%M:%S')
            self.trv.insert("", "end", values = (i[0], i[1], i[2], i[3]))

        

    def on_hover(self, event):
        """Function to handle hover effect"""
        # Identify the item being hovered over
        item = self.trv.identify_row(event.y)
        
        # Reset background color for all items
        for child in self.trv.get_children():
            self.trv.item(child, tags=())
        
        # Apply hover effect by changing the item's background color
        self.trv.item(item, tags=("hover",))
        self.trv.tag_configure("hover", background="lightblue")


    def find(self, event = None):
        # Clear the current treeview content
        for item in self.trv.get_children():
            self.trv.delete(item)
        
        # Get the search term from the entry widget
        val = self.search_entry.get()
        
        # Update the SQL query to use the LIKE operator with a wildcard
        mycursor.execute("SELECT * FROM travel_details WHERE City LIKE %s or Date1 LIKE %s", (val + '%', val + '%'))
        users = mycursor.fetchall()

        # Insert the matching rows into the treeview
        for row in users:
            self.trv.insert('', END, values=row)

root.resizable(False,False)
initial = first_page(root)
root.mainloop()
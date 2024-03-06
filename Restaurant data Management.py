from tkinter import *
from tkinter import ttk
from datetime import *
from tkinter import messagebox
import mysql.connector

def enter():
     if nameofthecustomer.get()=='' and aadhar.get()=='':
          messagebox.showerror("Field Mandatory",'All Fields Are Mandatory')
     else:
          messagebox.showinfo('Enter Status','Successfully Entered')

def add():
    try:
        if food_code.get() == '' and nameofthecustomer.get()=='':
            messagebox.showerror('Field Error', 'Please Enter The Food Code')
        else:
            connection = mysql.connector.connect(host='localhost', username='root', password='iamadhitya', database='hotel_management')
            cursor = connection.cursor()
            name_values = str(nameofthecustomer.get())
            food = str(food_code.get())
            aadhar_value = aadhar.get()[:20]  # Adjusting the length
            room_number_value = roomnuber.get()
            current_date_value = Date.get()

            query = 'INSERT INTO FOOD_CUSTOMER VALUES(%s,%s,%s,%s,%s);'
            values = (name_values, aadhar_value, room_number_value, current_date_value, food)
            cursor.execute(query, values)

            cursor.execute("SELECT * FROM food_MENU WHERE food_CODE=%s", (food,))
            items = cursor.fetchall()

            for i in items:
                restaurant_billing.insert("", END, values=i)

            messagebox.showinfo('Add Status', "Product Added Successfully")
            connection.commit()

    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')
 
def clear():

    connection = mysql.connector.connect(host='localhost', username='root', password='iamadhitya', database='hotel_management')
    cursor = connection.cursor()

    query = "DELETE FROM FOOD_CUSTOMER WHERE FOOD_CODE = %s;"
    value = (str(food_code.get()),)
    cursor.execute(query,value)

    messagebox.showinfo('Clear Status','Sucessfully Cleared')

    connection.commit()
    connection.close()

def bill():

    if nameofthecustomer.get()=='' and aadhar.get()=='':
        messagebox.showerror("Field Error","Please Enter The Name And Aadhaar")
    else:

        search = Tk()
        search.title("Bill")

        scrollx = ttk.Scrollbar(search,orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(search,orient=VERTICAL)
        supermarket_billing =ttk.Treeview(search,columns=('name','room','date','dish','price'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx = ttk.Scrollbar(command=supermarket_billing.xview)
        scrolly = ttk.Scrollbar(command=supermarket_billing.yview)

        supermarket_billing.heading('name',text='Name')
        supermarket_billing.heading('room',text='Room')
        supermarket_billing.heading('date',text='Date')
        supermarket_billing.heading('dish',text='Dish')
        supermarket_billing.heading('price',text='Price(Rs.)')
        supermarket_billing['show'] = 'headings'
        supermarket_billing.pack(fill=BOTH,expand=1)

        connection = mysql.connector.connect(host='localhost',username ='root', password='iamadhitya', database ='hotel_management')
        cursor = connection.cursor()
        query = "SELECT B.BOARDERS_NAME 'NAME' ,B.ROOM 'ROOM',B.DATE_ 'DATE',F.FOOD_NAME 'DISH',F.PRICE 'PRICE(RS.)' FROM FOOD_CUSTOMER B JOIN FOOD_MENU F ON B.FOOD_CODE = F.FOOD_CODE WHERE AADHAR=%s;"
        value = (str(aadhar.get()),)
        cursor.execute(query,value)
        items = cursor.fetchall()
        query2 = "SELECT SUM(P.BILL) AS 'TOTAL AMOUNT' FROM (SELECT P.PRICE AS BILL FROM FOOD_MENU P JOIN FOOD_CUSTOMER S ON P.FOOD_CODE = S.FOOD_CODE WHERE AADHAR = %s) AS P;"
        cursor.execute(query2,value)
        total_bill = cursor.fetchall()
        for i in items:
            supermarket_billing.insert("",END,values=i)
        for j in total_bill:
            label_value = Label(search,text= 'Total Bill',font =('Arial Bond',20,'bold'), bg ='orange red', fg= 'gold', relief=GROOVE).pack()
            label_value = Label(search,text=  j,font =('Arial Bond',20,'bold')).pack()
        connection.commit()
        connection.close()

def food_menu_details():
    
    search_result =Tk()
    search_result.title('FOOD_MENU')
    scrollx = ttk.Scrollbar(search_result,orient=HORIZONTAL)
    scrolly = ttk.Scrollbar(search_result,orient=VERTICAL)
    supermarket_billing =ttk.Treeview(search_result,columns=('Pro Code','prod','Price'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)

    scrollx = ttk.Scrollbar(command=supermarket_billing.xview)
    scrolly = ttk.Scrollbar(command=supermarket_billing.yview)

    supermarket_billing.heading('Pro Code',text='Food Code')
    supermarket_billing.heading('prod',text='Price')
    supermarket_billing.heading('Price',text='Dish Name')
    supermarket_billing['show'] = 'headings'
    supermarket_billing.pack(fill=BOTH,expand=1)

    connenction = mysql.connector.connect(host='localhost',username='root',password='iamadhitya',database='hotel_management')
    cursor_object = connenction.cursor()
    cursor_object.execute('SELECT * FROM FOOD_MENU')
    items = cursor_object.fetchall()
    for i in items:
        supermarket_billing.insert("",END,values=i)
    connenction.commit()
    connenction.close()    

window = Tk()
window.geometry('1275x675')
window.title('Nirvana Restaurant')
window.config(bg ='bisque')

nameofthecustomer=StringVar()
aadhar=StringVar()
roomnuber=StringVar()

#Top frame

labelt1 = Label(window, text ='Nirvana Welcomes You', width =10, height =2, fg='gold', bg ='gray20', font =('times new roman',20,'bold'), relief= GROOVE, bd =12).pack(side=TOP,fill=X)
labelt2 = Label(window, text ='Place Your Order', width =10, height =2, bg ='orange red', fg= 'gold', font =('times new roman',20,'bold'), relief= GROOVE, bd= 10 ).pack(side=TOP,fill=X)

#Boarders details

#boarders_frame = LabelFrame(window).pack()

details = Label(window, text ='           Boarder Details            ', font =('times new roman',20,'bold'), fg= 'gold', bg= 'gray20', relief=GROOVE, bd=10, height =2).place(x=2, y=170)

name_label1 = Label(window, text ='Name :', font =('Arial Bond',15,'bold'), fg= 'gold', bg='gray20',relief=GROOVE,bd=8).place(x=6,y=260)
name_entry1 = Entry(window, textvariable=nameofthecustomer, bg ='gray20', fg= 'gold',font =('Arial Bond',15,'bold'),relief=GROOVE,bd=8).place(x=100,y=260)

aadhar_label1 = Label(window, text ='Aadhar :', font =('Arial Bond',15,'bold'), fg= 'gold', bg='gray20',relief=GROOVE,bd=8).place(x=6,y=320)
aadhar_entry1 = Entry(window, textvariable=aadhar ,bg ='gray20', fg= 'gold',font =('Arial Bond',15,'bold'),relief=GROOVE,bd=8).place(x=110,y=320)

room_label2 = Label(window, text ='Room :', font =('Arial Bond',15,'bold'),bg= 'gray20', fg='gold',relief=GROOVE,bd=8).place(x=6,y=370)
room_entry2 = ttk.Combobox(window,textvariable=roomnuber,  font =('Arial Bond',15,'bold'),width =20,height=3)
room_entry2['values'] = ('1A-01','1A-02','1A-03','1A-04','1A-05','2A-01','2A-02','2A-03','2A-04','2A-05','3A-01','3A-02','3A-03','3A-04','3A-05')
room_entry2.place(x=110,y=370)

Date =StringVar()
today = date.today()
de1 = today.strftime('%d-%m-%Y')
date_label3 = Label(window, text =' Date :',font =('Arial Bond',15,'bold'),bg ='gray20', fg='gold',relief=GROOVE,bd=8).place(x=6,y=430)
date_entry3 = Entry(window, width =20, textvariable= Date, bg = 'gray20', fg='gold',font =('Arial Bond',15,'bold'),relief=GROOVE,bd=8).place(x=100,y=430)
Date.set(de1)

time_label4 = Label(window, text =' Time:',font =('Arial Bond',15,'bold'), bg = 'gray20', fg ='gold',relief=GROOVE,bd=8).place(x=6,y=500)
time_entry4 = Entry(window, width =25, bg = 'gray20', fg ='gold',font =('Arial Bond',12,'bold'),relief=GROOVE,bd=8).place(x=110,y=500)


#Food details
food_code = StringVar()
food_label = Label(window, text ='        Food Details        ', font =('times new roman',20,'bold'), fg= 'gold', bg= 'gray20', relief=GROOVE, bd=10, height =2).place(x=430, y=170)
food_code_label5 = Label(window, text ='Food Code :', font =('Arial Bond',15,'bold'), bg= 'gray20', fg ='gold', relief=GROOVE, bd=10).place(x=435,y=260)
food_entry5 = ttk.Combobox(window,textvariable=food_code, width =8, font =('times new roman',20,'bold'))
food_entry5['values'] = ('VB 001','CB 001','MB 001','EB 001','FB 001','VF 002','CNF 002','DS 003','DC 003','IC 003','RT 003','RTC 001','BP 001','CHI 001','MC 001','PBG 001')
food_entry5.place(x=580,y=260)


#Buttons below food details

add_bt1 = Button(window, text ='Add', command=add ,font=('Arial Bond',15,'bold'), fg ='gold', bg ='orange red', relief=GROOVE, padx=80, pady =2, bd =10).place(x=750,y=250)

food_menu = Button(window,text='Food Menu',command=food_menu_details,font=('times new roman',15,'bold'), fg ='gold', bg ='gray20',relief=RIDGE,bd=10, padx=60, pady =2).place(x=999,y=180)
#Bottom frame

bottom_frame = Label(window,bg='orange red',fg='gold',height =5,relief=GROOVE,bd=5).pack(side=BOTTOM,fill=X)

enter_bt3 = Button(window, text ='Enter',command=enter, padx =30, pady =2, fg ='gold', bg ='gray20', font =('Arial Bond',15,'bold'),relief=GROOVE, bd =10).place(x=50,y=580)

clear_bt2 = Button(window, text = 'Clear Previous',command=clear, font=('Arial Bond',15,'bold'), bg = 'gray20', fg = 'gold', relief=GROOVE, bd =10, padx =30, pady =2).place(x =400,y =580)

bill_bt3 = Button(window, text = 'Bill',command=bill,font=('Arial Bond',15,'bold'), bg = 'gray20', fg = 'gold', relief=GROOVE, bd =10, padx =30, pady =2).place(x =750,y =580)

update_bt4 = Button(window, text = 'Update', font=('Arial Bond',15,'bold'), bg = 'gray20', fg = 'gold', relief=GROOVE, bd =10, padx =30, pady =2).place(x =1050,y =580)

scrollx = ttk.Scrollbar(window,orient=HORIZONTAL)
scrolly = ttk.Scrollbar(window,orient=VERTICAL)
restaurant_billing =ttk.Treeview(window,columns=('Name','Price','fo code',),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

scrolly = ttk.Scrollbar(command=restaurant_billing.yview)

restaurant_billing.heading('Name',text=' Food Code')
restaurant_billing.heading('Price',text='Price(Rs)')
restaurant_billing.heading('fo code',text='Food Name')
restaurant_billing['show'] = 'headings'
restaurant_billing.place(x=420,y=330)

window.mainloop()
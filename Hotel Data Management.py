from tkinter import *
from tkinter import ttk                 #ComboBox And Scroll
from tkinter import messagebox
from datetime import *
import mysql.connector

def cab_details():

    search_result =Tk()
    search_result.title('CAB_DETAILS')
    scrollx = ttk.Scrollbar(search_result,orient=HORIZONTAL)
    scrolly = ttk.Scrollbar(search_result,orient=VERTICAL)
    supermarket_billing =ttk.Treeview(search_result,columns=('Pro Code','prod','Price'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)

    scrollx = ttk.Scrollbar(command=supermarket_billing.xview)
    scrolly = ttk.Scrollbar(command=supermarket_billing.yview)

    supermarket_billing.heading('Pro Code',text='Vehicle Number')
    supermarket_billing.heading('prod',text='Vehicle Type')
    supermarket_billing.heading('Price',text='Price Per Kilometer')
    supermarket_billing['show'] = 'headings'
    supermarket_billing.pack(fill=BOTH,expand=1)

    connenction = mysql.connector.connect(host='localhost',username='root',password='iamadhitya',database='hotel_management')
    cursor_object = connenction.cursor()
    cursor_object.execute('SELECT * FROM CAB_DETAILS')
    items = cursor_object.fetchall()
    
    for i in items:
        supermarket_billing.insert('',END,values=i)
    connenction.commit()
    connenction.close()

def supermarket_menu():

    search_result =Tk()
    search_result.title('SUPERMARKET')
    scrollx = ttk.Scrollbar(search_result,orient=HORIZONTAL)
    scrolly = ttk.Scrollbar(search_result,orient=VERTICAL)
    supermarket_billing =ttk.Treeview(search_result,columns=('Pro Code','prod','Price'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)

    scrollx = ttk.Scrollbar(command=supermarket_billing.xview)
    scrolly = ttk.Scrollbar(command=supermarket_billing.yview)

    supermarket_billing.heading('Pro Code',text='Product_code')
    supermarket_billing.heading('prod',text='Product_Name')
    supermarket_billing.heading('Price',text='Price(Rs)')
    supermarket_billing['show'] = 'headings'
    supermarket_billing.pack(fill=BOTH,expand=1)

    connenction = mysql.connector.connect(host='localhost',username='root',password='iamadhitya',database='hotel_management')
    cursor_object = connenction.cursor()
    cursor_object.execute('SELECT * FROM SUPERMARKET_MENU')
    items = cursor_object.fetchall()
    
    for i in items:
        supermarket_billing.insert('',END,values=i)
    connenction.commit()
    connenction.close()

def room_details():

    search_result =Tk()
    search_result.title('FOOD_MENU')
    scrollx = ttk.Scrollbar(search_result,orient=HORIZONTAL)
    scrolly = ttk.Scrollbar(search_result,orient=VERTICAL)
    supermarket_billing =ttk.Treeview(search_result,columns=('Pro Code','prod','Price'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)

    scrollx = ttk.Scrollbar(command=supermarket_billing.xview)
    scrolly = ttk.Scrollbar(command=supermarket_billing.yview)

    supermarket_billing.heading('Pro Code',text='Room Code')
    supermarket_billing.heading('prod',text='Room Type')
    supermarket_billing.heading('Price',text='Price')
    supermarket_billing['show'] = 'headings'
    supermarket_billing.pack(fill=BOTH,expand=1)

    connenction = mysql.connector.connect(host='localhost',username='root',password='iamadhitya',database='hotel_management')
    cursor_object = connenction.cursor()
    cursor_object.execute('SELECT * FROM ROOM_DETAILS;')
    items = cursor_object.fetchall()
    for i in items:
        supermarket_billing.insert("",END,values=i)
    connenction.commit()
    connenction.close()

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

def getting_boarders_details():

    if nameofthecustomer.get() == '' and aadhar.get()=='':
        messagebox.showerror('Error',"All details are mandatory")
    else:
        connenction = mysql.connector.connect(host='localhost',username='root',password='iamadhitya',database='hotel_management')
        cursor_object = connenction.cursor()
        values = (str(nameofthecustomer.get()),age.get(),aadhar.get(),phonenumber.get(),Date1.get(),room_entry6.get(),room_no_entry7.get())
        query = "INSERT INTO BOARDERS_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor_object.execute(query,values)
        connenction.commit()
        connenction.close()

        messagebox.showinfo('Successfully Booked','Welcome' +' '+ str(nameofthecustomer.get()))
    
def search():

    if search_boarder.get() =='':

        messagebox.showerror('Field Error','Please Enter The Name')

    else:
        search_result =Tk()
        search_result.title('Search Result')
        scrollx = ttk.Scrollbar(search_result,orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(search_result,orient=VERTICAL)
        supermarket_billing = ttk.Treeview(search_result,columns=('name','age','aad','ph','dat','romm','roomty'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx = ttk.Scrollbar(command=supermarket_billing.xview)
        scrolly = ttk.Scrollbar(command=supermarket_billing.yview)

        supermarket_billing.heading('name',text='NAME')
        supermarket_billing.heading('age',text='AGE')
        supermarket_billing.heading('aad',text='AADHAR')
        supermarket_billing.heading('ph',text='PHONE NO.')
        supermarket_billing.heading('dat',text='DATE')
        supermarket_billing.heading('romm',text='ROOM TYPE')
        supermarket_billing.heading('roomty',text='ROOM NO.')
        supermarket_billing['show'] = 'headings'
        supermarket_billing.pack(fill=BOTH,expand=1)

        connenction = mysql.connector.connect(host='localhost',username='root',password='iamadhitya',database='hotel_management')
        cursor_object = connenction.cursor()

        # COVERTING STR VAR TO STR AND THEN TUPLES
        
        s = (str(search_boarder.get()),)
        cursor_object.execute('SELECT * FROM BOARDERS_DETAILS WHERE BOARDER_NAME = %s',(s))
        datas = cursor_object.fetchall()
        for i in datas:
            supermarket_billing.insert("",END,values=i)
    connenction.commit()
    connenction.close()

def paid():

    if leave_name.get()=='' and leave_aadhar.get()=='':
        messagebox.showerror('Field Error','Please Enter The Name And Aadhar')
    else:
        messagebox.showinfo("Payment Success","Thank You" +" " + str(leave_name.get()))

def check_out_days():

    global no_stay
    connenction = mysql.connector.connect(host='localhost',username='root',password='iamadhitya',database='hotel_management')
    cursor_object = connenction.cursor()
    query4 = "SELECT * FROM BOARDERS_DETAILS WHERE AADHAR = %s;"
    a = (str(leave_aadhar.get()),)
    cursor_object.execute(query4,(a))
    items = cursor_object.fetchone()
    check_in_month = items[4]
    check_in_month= int(check_in_month[3:5])
    current_month = date.today()#YYYY-MM-DD Format
    tt = str(current_month)
    check_out_month = int(tt[5:7])
    check_in_date = items[4]
    check_in_date= int(check_in_date[0:2])
    tt = str(current_month)
    check_out_date = int(tt[8:])

    if check_in_month < check_out_month:
        if check_in_date <= check_out_date :
            no_stay = 31 - check_in_date
            check_out()
        else:
            no_stay = 30 - check_in_date
            check_out()
    else:
        no_stay = 0
        check_out()


def check_out():

    if (leave_name.get()=='' and leave_aadhar.get()==''):
        messagebox.showerror('Field Error','Please Enter The Name And Aadhar')
    else:
        bill_window =Tk()
        bill_window .title('Check Out')
        scrollx = ttk.Scrollbar(bill_window ,orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(bill_window ,orient=VERTICAL)
        supermarket_billing = ttk.Treeview(bill_window ,columns=('name','aad','romm','roomty','price'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx = ttk.Scrollbar(command=supermarket_billing.xview)
        scrolly = ttk.Scrollbar(command=supermarket_billing.yview)

        supermarket_billing.heading('name',text='NAME')
        supermarket_billing.heading('aad',text='AADHAR')
        supermarket_billing.heading('romm',text='ROOM NO.')
        supermarket_billing.heading('roomty',text='ROOM TYPE')
        supermarket_billing.heading('price',text='PRICE')
        supermarket_billing['show'] = 'headings'
        supermarket_billing.pack(fill=BOTH,expand=1)

        connenction = mysql.connector.connect(host='localhost',username='root',password='iamadhitya',database='hotel_management')
        cursor_object = connenction.cursor()
        a = (str(leave_aadhar.get()),)
        query1 = 'SELECT B.BOARDER_NAME,B.AADHAR,R.ROOM_TYPE,R.ROOM_NO,R.PRICE FROM BOARDERS_DETAILS AS B JOIN ROOM_DETAILS AS R ON B.ROOM_NO = R.ROOM_NO WHERE B.AADHAR =%s;'
        cursor_object.execute(query1,(a))
        datas = cursor_object.fetchmany()
        for o in datas:
            supermarket_billing.insert("",END,values=o)      
        
        #Supermarket Total Bill       
        
        query2 = "SELECT SUM(P.BILL) AS 'TOTAL AMOUNT' FROM (SELECT P.PRICE AS BILL FROM SUPERMARKET_MENU P JOIN SUPERMARKET_CUSTOMERS S ON P.PRODUCT_CODE = S.PRODUCT_CODE WHERE AADHAR = %s) AS P;"
        cursor_object.execute(query2,(a))
        total_price = cursor_object.fetchall()
        for i in total_price:
            int_total_bill = int(str(i[0])) # For calculating total
            label_value = Label(bill_window,text= 'Super Market Total Bill',font =('Arial Bond',20,'bold'), bg ='steel blue', fg ='gold', relief=GROOVE).pack()
            label_value = Label(bill_window,text="Rs." + str(i[0]),font =('Arial Bond',20,'bold')).pack()

        #Food Total Bill

        query3 = "SELECT SUM(P.BILL) AS 'TOTAL AMOUNT' FROM (SELECT P.PRICE AS BILL FROM FOOD_MENU P JOIN FOOD_CUSTOMER S ON P.FOOD_CODE = S.FOOD_CODE WHERE AADHAR = %s) AS P;"
        cursor_object.execute(query3,(a))
        total_food_bill = cursor_object.fetchall()
        for j in total_food_bill:
            int_super_price = int(j[0])# For calculating total
            label_value = Label(bill_window,text= 'Restaurant Total Bill',font =('Arial Bond',20,'bold'), bg ='orange red', fg= 'gold', relief=GROOVE).pack()
            label_value = Label(bill_window,text="Rs." + str(j[0]),font =('Arial Bond',20,'bold')).pack()

        query4 = "SELECT * FROM BOARDERS_DETAILS WHERE AADHAR = %s;"
        cursor_object.execute(query4,(a))
        items = cursor_object.fetchone()
        check_in_date = items[4]
        check_in_date= int(check_in_date[0:2])
        current_date = date.today()#YYYY-MM-DD Format
        tt = str(current_date)
        check_out_date = int(tt[8:])
        days = check_out_date - check_in_date
       
        query5 = 'SELECT B.BOARDER_NAME,B.AADHAR,R.ROOM_TYPE,R.ROOM_NO,R.PRICE FROM BOARDERS_DETAILS AS B JOIN ROOM_DETAILS AS R ON B.ROOM_NO = R.ROOM_NO WHERE B.AADHAR =%s;'
        cursor_object.execute(query5,(a))
        datas2 = cursor_object.fetchone()
        room_total = (no_stay + days) * int(datas2[4])
        label_value3 = Label(bill_window,text= 'Room Total Bill',font =('Arial Bond',20,'bold'), bg ='seagreen', fg ='gold', relief=GROOVE).pack()
        label_value3 = Label(bill_window,text="Rs." + str(room_total),font =('Arial Bond',20,'bold')).pack()

        #Total Check out Price including food,market and room
        
        final_bill = int_super_price+int_total_bill+room_total
        label_value = Label(bill_window,text= 'Check Out Bill',font =('Arial Bond',20,'bold'), bg ='dark green', fg= 'gold', relief=GROOVE).pack()
        label_value = Label(bill_window,text="Rs." + str(final_bill),font =('Arial Bond',20,'bold')).pack()
    
    connenction.commit()
    connenction.close()

window = Tk()
window.geometry('1275x675')
window.title('Hotel Registration')
window.config(bg ='wheat')

nameofthecustomer=StringVar()
aadhar=StringVar()
age=StringVar()
roomtype=StringVar()
roomnuber=StringVar()
phonenumber=StringVar()

# Top Frame

top_frame0 = Label(window, text ='Email : nirvana.hotelandservices@gmail.com', bg ='plum', fg='gray25', anchor='e', font=('times new roman',10), relief=RIDGE, bd=5, height=2)
top_frame0.pack(side=TOP,fill=X)

top_frame = Label(window, text = 'Nirvana Greets You ', font = ('Arial Bond',30,'bold'), relief=GROOVE,bd =10, bg ='gold', fg ='darkblue')
top_frame.pack(side=TOP,fill=X)

top_frame2 = Label(window, text = 'Enjoy Your Dream Vacation',font = ('times new roman',30,'bold'),relief=GROOVE, bd =10, bg='lightgoldenrod', fg ='purple')
top_frame2.pack(side=TOP,fill=X)

top_frame3 = Label(window, text ='                        Boarder Details                     ', font =('times new roman',20,'bold'), bg ='seagreen', fg ='gold2',relief=GROOVE, height=2, bd=10).place(x=2,y=175)

name_label = Label(window, text ='Name :', font =('times new roman',15,'bold'), relief=GROOVE, bg ='seagreen', fg='gold', bd =10).place(x=2,y=260)
name_entry = Entry(window, textvariable=nameofthecustomer, font =('times new roman',15,'bold'), width =14, bg ='seagreen', fg ='gold',relief=GROOVE,bd=8).place(x=95,y=260)

age_label2 = Label(window, text = '  Age :  ', font = ('times new roman',15,'bold'),relief=GROOVE, bg ='seagreen', fg='gold', bd=7).place(x=2,y=308)
age_entry = Entry(window, textvariable=age,font =('times new roman',15,'bold'), width =14, bg ='seagreen', fg ='gold',relief=GROOVE,bd=8).place(x=95,y=308)

phone_label = Label(window, text ='Ph No. :', font =('times new roman',15,'bold'), relief=GROOVE, bg ='seagreen', fg='gold', bd =10).place(x=2,y=353)
phone_entry = Entry(window, textvariable=phonenumber,font =('times new roman',15,'bold'), width =14, bg ='seagreen', fg ='gold',relief=GROOVE,bd=8).place(x=95,y=353)

aadhar_label = Label(window, text ='Aadhar:', font =('times new roman',15,'bold'), relief=GROOVE, bg ='seagreen', fg='gold', bd =10).place(x=265,y=260)
aadhar_entry = Entry(window,textvariable=aadhar, font =('times new roman',15,'bold'), width =14, bg ='seagreen', fg ='gold',relief=GROOVE,bd=8).place(x=363,y=260)

Date1 =StringVar()
today = date.today()
de1 = today.strftime('%d/%m/%Y')
date_label5 = Label(window, text =' Date : ',font =('times new roman',15,'bold'),relief=GROOVE,bg ='seagreen', fg='gold', bd =10).place(x=265,y=310)
date_entry = Entry(window, textvariable=Date1,font =('times new roman',15,'bold'), width =14, bg ='seagreen', fg ='gold',relief=GROOVE,bd=8).place(x=363,y=310)
Date1.set(de1)

room_label6 = Label(window, text ='Room: ',font =('times new roman',15,'bold'),relief=GROOVE,bg='seagreen', fg='gold', bd=10).place(x=265,y=360)
room_entry6 = ttk.Combobox(window,width=14,font =('times new roman',15,'bold'))
room_entry6['values'] = ('Luxury','Premium','Business','Economy','Palace')
room_entry6.place(x=363,y=360)

room_no_label7 = Label(window, text ='Room No.:',font =('times new roman',15,'bold'), relief=GROOVE, bg ='seagreen', fg ='gold', bd=10).place(x=265,y=410)
room_no_entry7 = ttk.Combobox(window, width =12,font=('times new roman',15,'bold'))
room_no_entry7['values'] = ('1A-01','1A-02','1A-03','1A-04','1A-05','2A-01','2A-02','2A-03','2A-04','2A-05','3A-01','3A-02','3A-03','3A-04','3A-05')
room_no_entry7.place(x=383,y=415)

time_label8 = Label(window, text=' Time :',font=('times new roman',15,'bold'), relief=GROOVE, bg='seagreen', fg='gold',bd=10).place(x=2,y=410)
time_entry8 = Entry(window,width=14,font=('times new roman',15,'bold'),bg='seagreen',fg='gold',relief=GROOVE,bd=10).place(x=95,y=410)

#Boarders leaving details

top_frame4 =  Label(window, text ='     Depature Boarder Details    ', font =('times new roman',20,'bold'),width=40, bg ='seagreen', fg ='gold2',relief=GROOVE, height=2, bd=10).place(x=555,y=175)

leave_name = StringVar()
name_labe2 = Label(window, text ='Name :', font =('times new roman',15,'bold'), relief=GROOVE, bg ='seagreen', fg='gold', bd =10).place(x=590,y=260)
name_entry2 = Entry(window, textvariable=leave_name, font =('times new roman',15,'bold'), width =14, bg ='seagreen', fg ='gold',relief=GROOVE,bd=8).place(x=690,y=260)

leave_aadhar = StringVar()
aadhar_labe2 = Label(window, text ='Aadhar:', font =('times new roman',15,'bold'), relief=GROOVE, bg ='seagreen', fg='gold', bd =10).place(x=890,y=260)
aadhar_entry2 = Entry(window,textvariable=leave_aadhar, font =('times new roman',15,'bold'), width =14, bg ='seagreen', fg ='gold',relief=GROOVE,bd=8).place(x=995,y=260)


#Bottom frame

bottom_frame = Label(window, bg ='plum', fg='gray25',relief=GROOVE,bd=7,height=4).pack(side=BOTTOM,fill=X)

#Buttons for boarders entry


Enter_button = Button(window, text ='Check-In', command=getting_boarders_details,font =('Arial Bond',20,'bold'),relief=GROOVE,bd=10, bg ='gold', fg ='dark green',padx=100,pady=2).place(x=130,y=480)

#Search boarder
search_boarder = StringVar()
Search_label = Label(window,text='Boarder Name:', font=('times new roman',15,'bold'),relief=GROOVE,bd=10,bg ='gold', fg ='dark green').place(x=5,y=587)
search_entry11 = Entry(window,textvariable=search_boarder, font=('times new roman',15,'bold'),relief=GROOVE,bd=10,bg ='mint cream').place(x=175,y=587)
search_button = Button(window,text ='Search', command=search,font=('times new roman',12,'bold'),relief=GROOVE,bd=10,bg ='gold', fg ='dark green').place(x=420,y=587)

payment_mode_label = Label(window,text='Mode of payment', font=('times new roman',12,'bold'),relief=GROOVE,bd=10,bg ='gold', fg ='dark green').place(x=550,y=590)
payment_entry = ttk.Combobox(window,width=12,font =('times new roman',15,'bold'))
payment_entry ['values'] = ("UPI","Apple Pay",'Cash',"Credit Card",'Debit Card')
payment_entry.place(x=700,y=595)

check_out_button = Button(window,text='Check Out', command=check_out_days, font=('times new roman',14,'bold'),relief=GROOVE,bd=10,bg ='gold', fg ='dark green',padx=35).place(x=860,y=584)

paid_button = Button(window,text='Paid',command=paid,font=('times new roman',13,'bold'),relief=GROOVE,bd=10,bg ='gold', fg ='dark green',padx=35).place(x=1100,y=587)

food_menu = Button(window,text='Food Menu',command=food_menu_details,font=('times new roman',15,'bold'), fg ='gold', bg ='gray20',relief=RIDGE,bd=10, padx=60, pady =2).place(x=920,y=350)

super_market_items = Button(window,text='Super Store',command=supermarket_menu,font=('times new roman',15,'bold'), fg ='gold', bg ='gray20',relief=RIDGE,bd=10, padx=60, pady =2).place(x=620,y=350)

cab = Button(window,text='Cab Details',command=cab_details,font=('times new roman',15,'bold'), fg ='gold', bg ='gray20',relief=RIDGE,bd=10, padx=60, pady =2).place(x=620,y=450)

rooms = Button(window,text='Room Details',command=room_details,font=('times new roman',15,'bold'), fg ='gold', bg ='gray20',relief=RIDGE,bd=10, padx=60, pady =2).place(x=910,y=450)

window.mainloop()

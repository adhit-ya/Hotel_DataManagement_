from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import *
import mysql.connector 

def enter():
     if name.get()=='' and aadhar.get()=='':
          messagebox.showerror("Field Mandatory",'Please Enter The Name And Aadhar')
     else:
          messagebox.showinfo('Enter Status','Successfully Entered')
            
#ADDING RECORDS IN THE TABLE WHAT CUSTOMER IS PURCHASING

def supermarket_customer():
    try:
        if product_code.get() == '':
            messagebox.showerror("Field Error", "Please Enter the Product Code")
        else:
            connection = mysql.connector.connect(host='localhost', username='root', password='iamadhitya',
                                                 database='HOTEL_MANAGEMENT')
            cursor = connection.cursor()
            
            product_code_value = str(product_code.get())
            name_value = str(name.get())
            aadhar_value = aadhar.get()[:20]  #Adjusting the length
            room_number_value = room_number.get()
            current_date_value = current_date.get()

            values = (name_value, aadhar_value, room_number_value, current_date_value, product_code_value)
            cursor.execute('INSERT INTO SUPERMARKET_CUSTOMERS VALUES(%s, %s, %s, %s, %s)', values)

            cursor.execute('SELECT * FROM SUPERMARKET_MENU WHERE PRODUCT_CODE =%s',(product_code_value,))
            data = cursor.fetchall()

            for i in data:
                supermarket_billing.insert("",END,values=i)
           
            messagebox.showinfo('Add Status', 'Product Added Successfully')
            connection.commit()
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')
    finally:
        cursor.close()
        connection.close()

def delete_previous():
     
     connection = mysql.connector.connect(host='localhost', username='root', password='iamadhitya',
                                                 database='HOTEL_MANAGEMENT')
     cursor = connection.cursor()
     query = "DELETE FROM SUPERMARKET_CUSTOMERS WHERE PRODUCT_CODE=%s"
     product_code_value = str(product_code.get())
     cursor.execute(query,(product_code_value,))
     messagebox.showinfo('Delete  Status', 'Product Erased Successfully')
     connection.commit()
     connection.close()



def bill():
 
    if name.get() == '' and aadhar.get() == '':
        messagebox.showerror("Field Error", "Please Enter the Name and Aadhar")

    else:
        search = Tk()
        search.title("Bill")

        scrollx = ttk.Scrollbar(search,orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(search,orient=VERTICAL)
        supermarket_billing =ttk.Treeview(search,columns=('name','room','date','product','price'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx = ttk.Scrollbar(command=supermarket_billing.xview)
        scrolly = ttk.Scrollbar(command=supermarket_billing.yview)

        supermarket_billing.heading('name',text='Name')
        supermarket_billing.heading('room',text='Room')
        supermarket_billing.heading('date',text='Date')
        supermarket_billing.heading('product',text='Product')
        supermarket_billing.heading('price',text='Price(Rs.)')
        supermarket_billing['show'] = 'headings'
        supermarket_billing.pack(fill=BOTH,expand=1)
        aadhar_value = aadhar.get()[:20]
        connection = mysql.connector.connect(host='localhost', username='root', password='iamadhitya',
                                                 database='HOTEL_MANAGEMENT')
        cursor = connection.cursor()
        query = "SELECT B.BOARDERs_NAME 'NAME' ,B.ROOM 'ROOM',B.DATE 'DATE',P.PRODUCT_NAME 'PRODUCT',P.PRICE 'PRICE(RS.)' FROM SUPERMARKET_CUSTOMERS B JOIN SUPERMARKET_MENU P ON B.PRODUCT_CODE = P.PRODUCT_CODE WHERE AADHAR=%s;"
        cursor.execute(query,(aadhar_value,))
        data = cursor.fetchall()
        query2 = "SELECT SUM(P.BILL) AS 'TOTAL AMOUNT' FROM (SELECT P.PRICE AS BILL FROM SUPERMARKET_MENU P JOIN SUPERMARKET_CUSTOMERS S ON P.PRODUCT_CODE = S.PRODUCT_CODE WHERE AADHAR = %s) AS P;"
        cursor.execute(query2,(aadhar_value,))
        total_price = cursor.fetchall()
        for i in data:
            supermarket_billing.insert("",END,values=i)
        for i in total_price:
            label_value = Label(search,text= 'Total Bill',font =('Arial Bond',20,'bold'), bg ='steel blue', fg ='gold', relief=GROOVE).pack()
            label_value = Label(search,text=  i,font =('Arial Bond',20,'bold')).pack()
        connection.commit()
        connection.close()

billing = Tk()
billing.title('Nirvana Super Store Billing')
billing.geometry('1275x675')
billing.config(bg ='light cyan')

#Head Frame

top1 = Label(billing, text ='Niravana Welcomes You', font=('Arial Bond',20,'bold'), bg='sky blue', fg ='hotpink', height =2, bd=10, relief=RIDGE)
top1.pack(side=TOP, fill=X)

top2 = Label(billing, text ='Sales Billing', font =('Arial Bond',20,'bold'), bg ='steel blue', fg ='gold', relief=GROOVE, height=2, bd =10)
top2.pack(side=TOP,fill=X)

#Invisible Frame

top3 = Label(billing,bg='light cyan',height=3).pack(side=TOP,fill=X)

#Frame above invisible frame

top4 = Label(billing,relief=RIDGE,bd=10,bg='steel blue',height=3).pack(side=TOP,fill=X)

product_code = StringVar()
label_product = Label(billing, text ='Product Code', font =('Arial Bond',13,'bold'), bg ='sky blue', fg ='red',relief=GROOVE, bd=5).place(x=340,y=240)
label_product_entry = ttk.Combobox(billing,textvariable=product_code,width=12,font=('Arial Bond',13,'bold'))
label_product_entry['values'] =('PA 001','PAG 001','PAB 001','PAP 001','PAHG 001','DR 002','ML 002','CK 002','PS 002','LS 002','SC 003','DM 002','CP 002','LS 001','IC 002','CG 002','SA 002')
label_product_entry.place(x=490,y=243)

#Add Button

add_button = Button(billing,text='Add',command=supermarket_customer,font=('Arial Bond',13,'bold'), bg ='seagreen', fg ='gold',relief=GROOVE, bd=5).place(x=690,y=240)

#Bottom Frame

bottomframe = Label(billing,bg ='sky blue', height =3, bd=10).pack(side=BOTTOM,fill=X)

#Boarders Deatils

name = StringVar()
label_name = Label(billing, text =' Name : ', font =('Arial Bond',13,'bold'), bg ='sky blue', fg ='red',relief=GROOVE, bd=5).place(x=2,y=182)
entry_name = Entry(billing,textvariable=name, font =('Arial Bond',13,'bold'), width= 18, bg='sky blue', fg ='darkorange3', relief=GROOVE, bd =5).place(x=85,y=182)

aadhar =StringVar()
label_aadhar = Label(billing, text ='Aadhar Number :', font =('Arial Bond',13,'bold'), bg ='sky blue', fg ='red', relief=GROOVE, bd=5).place(x=280,y=182)
entry_aadhar = Entry(billing, textvariable=aadhar,font =('Arial Bond',13,'bold'), width= 18, bg='sky blue', fg ='darkorange3', relief=GROOVE, bd=5).place(x=430,y=182)

room_number = StringVar()
label_room = Label(billing, text ='Room Number :', font =('Arial Bond',13,'bold'), bg ='sky blue', fg ='red', relief=GROOVE, bd =5).place(x=620,y=182)
entry_room = ttk.Combobox(billing,textvariable=room_number, width =15, height =3)
entry_room['values'] = ('1A-01','1A-02','1A-03','1A-04','1A-05','2A-01','2A-02','2A-03','2A-04','2A-05','3A-01','3A-02','3A-03','3A-04','3A-05')
entry_room.place(x=765,y=185)

current_date = StringVar()
today = date.today()
d1 = today.strftime('%d-%m-%Y')
label_date = Label(billing, text =' Date : ', font =('Arial Bond',13,'bold'), bg ='sky blue', fg ='red', relief=GROOVE, bd =5).place(x=900,y=182)
entry_date = Entry(billing, textvariable= current_date, font =('Arial Bond',13,'bold'), bg ='sky blue', fg ='darkorange3', relief=GROOVE, bd =5).place(x=975,y=182)
current_date.set(d1)

#Enter Button near to the boards details

enter_button = Button(billing, text ='ENTER',command=enter, font =('Arial Bond',14,'bold'), bg ='steel blue', fg= 'gold', relief=GROOVE, bd=5).place(x=1175,y=172)

#Buttons in the bottom frame

clearall_button = Button(billing, text ='Clear All', font =('times new roman',15,'bold'), relief=GROOVE, bg= 'seagreen', fg ='gold', bd =5)
clearall_button.place(x=100,y=600)

clear_previous = Button(billing, text ='Clear Previous',command=delete_previous, font =('times new roman',15,'bold'), relief=GROOVE, bg ='seagreen', fg ='gold', bd=5)
clear_previous.place(x=280,y=600)

update_button = Button(billing, text ='Update Records', font =('times new roman',15,'bold'), bg ='seagreen', fg ='gold',relief=GROOVE,bd =5)
update_button.place(x=510,y=600)

bill_button = Button(billing, text ='Bill',command=bill, font=('times new roman',15,'bold'), bg ='seagreen', fg ='gold', relief=GROOVE, bd =5, padx =30, pady=4)
bill_button.place(x=780,y=595)

close_button = Button(billing, text ='Close', command=billing.destroy,font =('times new roman',15,'bold'), bg ='seagreen', fg ='gold', relief=GROOVE, bd =5, padx=30, pady=4)
close_button.place(x=1050,y=595)

#Product details table

scrollx = ttk.Scrollbar(billing,orient=HORIZONTAL)
scrolly = ttk.Scrollbar(billing,orient=VERTICAL)
supermarket_billing =ttk.Treeview(billing,columns=('Pro Code','prod','Price'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)

scrollx = ttk.Scrollbar(command=supermarket_billing.xview)
scrolly = ttk.Scrollbar(command=supermarket_billing.yview)

supermarket_billing.heading('Pro Code',text='Product_code')
supermarket_billing.heading('prod',text='Product_Name')
supermarket_billing.heading('Price',text='Price(Rs)')
supermarket_billing['show'] = 'headings'
supermarket_billing.pack(fill=BOTH,expand=1)

billing.mainloop()
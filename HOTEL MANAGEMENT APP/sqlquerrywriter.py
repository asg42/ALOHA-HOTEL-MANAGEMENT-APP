import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='system123')
mycursor = mydb.cursor(buffered=True)
try:
    mycursor.execute('drop database hotelmanagement;')
except:
    pass
mycursor.execute('create database hotelmanagement;')
mycursor.execute('use hotelmanagement;')
mycursor.execute('create table login(Id varchar(50),Pwd varchar(3));')
mycursor.execute('desc login;')
for everything in mycursor:
    print(everything)
    print()
mycursor.execute("insert into login(Id,Pwd) values('Joydeep Sir','1');")
mycursor.execute("insert into login(Id,Pwd) values('akashdeep','4');")
mycursor.execute("insert into login(Id,Pwd) values('arpita','7');")
mycursor.execute("insert into login(Id,Pwd) values('samrajnee','23');")
mycursor.execute("insert into login(Id,Pwd) values('shounak','24');")
mycursor.execute("insert into login(Id,Pwd) values('suhina','31');")
mycursor.execute("insert into login(Id,Pwd) values('swastika','32');")
mycursor.execute('select * from login;')
for everything in mycursor:
    print(everything)
    print()
mycursor.execute('create table customer(Customer_Name varchar(50),Cust_Id varchar(30) primary key,Phone_No varchar(20),No_Of_Days_To_Stay integer,Type_of_Room_Required varchar(30),Personal_Id varchar(30),start_date varchar(10),end_date varchar(10),address varchar(100),bill_total_amt integer,room_no integer);')
mycursor.execute('desc customer;')
for everything in mycursor:
    print(everything)

mycursor.execute("insert into customer(Customer_Name,Cust_Id,Phone_No ,No_Of_Days_To_Stay ,Type_of_Room_Required ,Personal_Id,start_date ,end_date ,address ,bill_total_amt ,room_no ) values('Satyajit Roy', '1', '9876543210', 10, 'Executive Suite with Lounge', '98760', '12/1/22', '12/11/22', 'Sweden', 5890, 101);")
mycursor.execute("insert into customer(Customer_Name,Cust_Id ,Phone_No ,No_Of_Days_To_Stay ,Type_of_Room_Required ,Personal_Id ,start_date ,end_date ,address ,bill_total_amt ,room_no) values('Lata Mangeshkar','2','9239827463',18,'Deluxe Twin Bed',5504,'11/25/22','12/13/22','California',6690,102);")
mycursor.execute('select * from customer;')
print()
mydb.commit()
mydb.close()

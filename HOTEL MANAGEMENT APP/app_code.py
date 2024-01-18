#  Let's do it IN-SHORT!!

# Importing required modules
from tkinter import *
from tkinter import messagebox
from time import strftime
from datetime import datetime
from tkcalendar import Calendar
import mysql.connector as connectsql
from PIL import ImageTk

mycon = connectsql.connect(host='localhost', user='root', passwd='system123', database='hotelmanagement')
mycon2 = connectsql.connect(host='localhost', user='root', passwd='system123', database='hotelmanagement')
main_width = 650
main_height = 650
main_home = Tk()

# Main window framework starts
# Dimension of main window
main_home.title('ALOHA RESORT ADMIN APP')
screen_width = main_home.winfo_screenwidth()
screen_height = main_home.winfo_screenheight()
main_home.geometry(f'{main_width}x{main_height}+{(int((screen_width - main_width) / 2))}+'
                   f'{(int((screen_height - main_height) // 2) - 40)}')
main_home.maxsize(main_width, main_height)
main_home.minsize(main_width, main_height)

# Dimension of the background canvas
bg_canvas = Canvas(main_home, bg='DarkGoldenRod1', bd=0, highlightthickness=0)
bg_canvas.pack(side=RIGHT, anchor=CENTER, fill=BOTH, expand=TRUE)

# app background
image_bg = ImageTk.PhotoImage(file="app_bg.jpg")
canvas_bg = bg_canvas.create_image(0, 0, image=image_bg, anchor=NW, tags='bg_canvas')

data_bg, heading_bg = '', ''
show_value, login_data, entry_id, entry_pwd, b_text_1, font = 0, {}, Entry(), Entry(), 0, 0
warning_id, warning_pwd, user_id, mycon = 0, 0, 0, ''
home_menu, change_menu, display_menu, search_menu, \
state_menu = Menu(), Menu(), Menu(), Menu(), Menu(),
time_label = Label()
info, customers, custid, roomno = {}, [], 0, 0
Name, ph, Ad, Persnl_ID, chkin_date, chkout_date, \
room_choice = '', '', '', '', '', '', ''
heading = 0


def login():
    global show_value, login_data, entry_id, entry_pwd
    hotel_name = bg_canvas.create_text(325, 180, text='ALOHA RESORT ADMIN APP', justify='center',
                                       font=('Franklin Gothic Demi', 28), fill='white', anchor='n')
    hotel_name_bg = bg_canvas.create_rectangle(70, 150, 580, 250, fill='gray20', outline='gray20')
    bg_canvas.tag_lower(hotel_name_bg, hotel_name)

    bg_canvas.create_text(240, 340, text='Enter your login ID:', font=('Georgia', 16),
                          fill='black', anchor=E)
    bg_canvas.create_text(240, 420, text='Enter the Password:', font=('Georgia', 16),
                          fill='black', anchor=E)
    # Text box for entering login id
    entry_id = Entry(bg_canvas, width=30, fg='black', bg='olivedrab2', font=('Microsoft Uighur', 20, 'bold'),
                     bd=4, relief='groove')
    bg_canvas.create_window(245, 340, window=entry_id, anchor=W)
    show_value = '*'
    # Text box for entering pwd
    entry_pwd = Entry(bg_canvas, width=30, fg='black', font=('Microsoft Uighur', 20, 'bold'),
                      show=show_value, bd=4, bg='olivedrab2', relief='groove')
    bg_canvas.create_window(246, 420, window=entry_pwd, anchor=W)
    b_text_1 = 'SHOW'
    login_data = {"Joydeep Sir": 1, "akashdeep": 4, "arpita": 7, "samrajnee": 23, "shounak": 24,
                  "suhina": 31, "swastika": 32}  # USER ID PASSWORD for each member including Joydeep sir's

    #  Show or hide the password framework
    def see():
        global show_value, b_text_1, font
        if show_value == '*':
            show_value = ''
            font = ('Microsoft Uighur', 20, 'bold')
            entry_pwd.configure(width=30, show=show_value, font=font)
            b_text_1 = 'HIDE'
            show.configure(text=b_text_1)
        elif show_value == '':
            show_value = '*'  # Used for hiding the password
            font = ('Microsoft Uighur', 20, 'bold')
            entry_pwd.configure(width=30, show=show_value, font=font)
            b_text_1 = 'SHOW'
            show.configure(text=b_text_1)

    show = Button(bg_canvas, text=b_text_1, bg='sandybrown', bd=0, width=11, height=2, highlightthickness=0,
                  command=see)
    bg_canvas.create_window(640, 400, window=show, anchor=E)

    # Checking ID and PASSWORD validity process
    # GUI Design for the validity checking

    def check_(Id, pwd):
        global warning_id, warning_pwd, login_data, user_id, mycon
        warning_id = bg_canvas.create_text(205, 380, text='', font='Helvetica', fill='red', anchor=W, tags='warning')
        warning_pwd = bg_canvas.create_text(205, 440, text='', font='Helvetica', fill='red', anchor=W, tags='warning')
        mycon = connectsql.connect(host='localhost', user='root', passwd='system123', database='hotelmanagement')
        if not mycon.is_connected():
            print("Connection could not be established.")
        else:
            mycur = mycon.cursor()
            mycur.execute("select * from login")
            data = mycur.fetchall()
            print(data)
            for row in data:
                if Id == row[0]:
                    bg_canvas.delete('warning')
                    if Id == row[0] and pwd == row[1]:
                        bg_canvas.delete('warning')
                        warning_id = bg_canvas.create_text(205, 375, text='Correct ID', font='Helvetica', fill='green',
                                                           anchor=W, tags='warning')
                        warning_pwd = bg_canvas.create_text(205, 465, text='Correct Pwd', font='Helvetica',
                                                            fill='green',
                                                            anchor=W, tags='warning')
                        user_id = Id

                        home()
                        break
                    else:
                        print("Invalid input")
                        bg_canvas.delete('warning')
                        warning_pwd = bg_canvas.create_text(205, 465, text='**Invalid PASSWORD for entered ID',
                                                            font='Helvetica', fill='red', anchor=W, tags='warning')
                else:
                    bg_canvas.delete('warning')
                    warning_id = bg_canvas.create_text(205, 375, text='**Invalid ID', font='Helvetica', fill='red',
                                                       anchor=W, tags='warning')

        if pwd != '':
            pwd = int(pwd)
        else:
            pwd = 0

    logged_in_b = Button(bg_canvas, text='Enter>>', font=('Arial', 15, 'bold'), bd=0, bg='#1B2650',
                         fg='white', width=12, height=1, pady=2,
                         command=lambda: check_(entry_id.get(), entry_pwd.get()))
    bg_canvas.create_window(462, 586, window=logged_in_b, anchor='nw')

    # Member button to show of members of the group

    def members(Id):
        global entry_id, entry_pwd, login_data
        entry_id.delete(0, END)
        entry_id.insert(0, Id)
        entry_pwd.delete(0, END)
        entry_pwd.insert(0, str(login_data[Id]))
        check_(entry_id.get(), entry_pwd.get())

    my_menu = Menubutton(bg_canvas, width=12, height=1, bd=0, highlightthickness=0, bg='#1B2650', fg='#fff5fa',
                         text='Members', font=('Arial', 15, 'bold'), activebackground='#3d1c39',
                         activeforeground='#e8dfe3', direction='above', pady=8)
    bg_canvas.create_window(30, 586, window=my_menu, anchor='nw')
    members_m = Menu(my_menu, title='Click to use info', tearoff=0, font=('Franklin Gothic Book', 15, 'bold'),
                     activebackground='#ff9c2b', activeforeground='black', fg='#2e2b28')

    # Name of the members including Joydeep Sir's name will be displayed when the menu button os clicked

    my_menu.configure(menu=members_m)
    members_m.add_command(label='Joydeep Sir', command=lambda: members("Joydeep Sir"))
    members_m.add_command(label='Akashdeep', command=lambda: members("akashdeep"))
    members_m.add_command(label='Arpita', command=lambda: members("arpita"))
    members_m.add_command(label='Samrajnee', command=lambda: members("samrajnee"))
    members_m.add_command(label='Shounak', command=lambda: members("shounak"))
    members_m.add_command(label='Suhina', command=lambda: members("suhina"))
    members_m.add_command(label='Swastika', command=lambda: members("swastika"))


def home():
    global main_home, bg_canvas, heading_bg, data_bg, image_bg, home_menu, change_menu, display_menu, search_menu, state_menu, \
        heading, info, customers, custid, roomno, mycon, mydb
    print('home')
    bg_canvas.destroy()

    # Dimension of the background canvas
    bg_canvas = Canvas(main_home, bg='DarkGoldenRod1', bd=0, highlightthickness=0)
    bg_canvas.pack(side=RIGHT, anchor=CENTER, fill=BOTH, expand=TRUE)

    # app background
    canvas_bg = bg_canvas.create_image(0, 0, image=image_bg, anchor=NW, tags='bg_canvas')
    data_bg = bg_canvas.create_rectangle(20, 140, 630, 640, fill='gray97', outline='gray97', tags='bg_canvas')

    # App Heading, time-display
    heading_bg = bg_canvas.create_rectangle(100, 10, 550, 70, fill='gray30', outline='gray30', tags='bgcanvas')
    heading = bg_canvas.create_text(325, 20, text='ALOHA RESORT ADMIN APP', justify='center',
                                    font=('Franklin Gothic Demi', 24), fill='white', anchor='n')

    def time():
        global time_label
        lbl_time = Label(bg_canvas, font=('Calibri', 12, 'bold'), background='#702666', foreground='#fff5fa')
        time_label = bg_canvas.create_window(606, 120, window=lbl_time)
        string = strftime('%H:%M:%S Hrs')
        lbl_time.config(text=string)
        lbl_time.after(1000, time)

    time()

    def clear():
        # CLEARING THE WIDGETS ON SCREEN
        global bg_canvas, time_label, heading, canvas_bg, data_bg, heading_bg, mycon
        widgets = bg_canvas.find_all()
        keep = [time_label, heading, tab_book, tab_search, tab_bill, heading, canvas_bg, data_bg, heading_bg]
        for i in widgets:
            if i not in keep:
                bg_canvas.delete(i)

    cursor = mycon2.cursor()
    db = cursor.execute("select * from customer")

    # Customers database
    for customer in cursor:
        info = {'name': customer[0], 'address': customer[8], 'phno': customer[2], 'persnlid': customer[5],
                'checkin': customer[6], 'checkout': customer[7], 'room': customer[4],
                'custid': customer[1], 'roomno': customer[10],
                'bill': customer[9]}
        customers.append(info)

    info = {'name': '', 'address': '', 'phno': 0, 'persnlid': 0, 'checkin': '',
            'checkout': '', 'room': '', 'beds': 0, 'custid': 0, 'roomno': 0, 'bill': 0}
    rooms = {'Deluxe King Bed': 3500, 'Deluxe Twin Bed': 4000,
             'Deluxe Suite with Lounge': 4500, 'Executive Suite with Lounge': 5000}
    custid = 1
    roomno = 101

    def book_tab():
        print('book')
        clear()

        # Customer Details
        bg_canvas.create_text(325, 145, text='Enter Customer Details',
                              font=('Microsoft New Tai Lue', 16, 'bold'),
                              fill='black', anchor='n')
        bg_canvas.create_text(50, 180, text='Name: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')
        name_booking = Entry(bg_canvas, font=12, width=30, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(150, 179, window=name_booking, anchor='nw')

        bg_canvas.create_text(50, 210, text='Phone: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')

        phn_booking = Entry(bg_canvas, font=12, width=10, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(150, 209, window=phn_booking, anchor='nw')

        bg_canvas.create_text(50, 240, text='Address: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')

        address_booking = Entry(bg_canvas, font=12, width=30, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(150, 239, window=address_booking, anchor='nw')

        bg_canvas.create_text(50, 270, text='Personal ID: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')

        P_Id_booking = Entry(bg_canvas, font=12, width=30, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(150, 269, window=P_Id_booking, anchor='nw')

        bg_canvas.create_text(50, 300, text='Enter following dates: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')
        bg_canvas.create_text(50, 320, text='Check-in: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')
        book_cal_in = Calendar(bg_canvas, font=('Roboto Condensed', 7, 'bold'), selectmode='day', year=2022,
                               month=11,
                               day=1)
        bg_canvas.create_window(50, 340, window=book_cal_in, anchor='nw')

        bg_canvas.create_text(350, 320, text='Check-out: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')
        book_cal_out = Calendar(bg_canvas, font=('Roboto Condensed', 7, 'bold'), selectmode='day', year=2022,
                                month=11,
                                day=1)
        bg_canvas.create_window(350, 340, window=book_cal_out, anchor='nw')

        # Rooms
        def select_room(choice):
            global room_choice
            room_choice = choice

        DelxKngBed_book = Checkbutton(bg_canvas, text='Deluxe King Bed',
                                      relief='flat', anchor='w', fg='gray10',
                                      justify='left', bg='gray85', bd=0,
                                      font=('Franklin Gothic Book', 12),
                                      command=lambda: select_room('Deluxe King Bed'),
                                      width=24, padx=8)
        DelxTwnBed_book = Checkbutton(bg_canvas, text='Deluxe Twin Bed',
                                      relief='flat', anchor='w', fg='gray10',
                                      justify='left', bg='gray85', bd=0,
                                      font=('Franklin Gothic Book', 12),
                                      command=lambda: select_room('Deluxe Twin Bed'),
                                      width=24, padx=8)
        DelxSuiteLounge_book = Checkbutton(bg_canvas, text='Deluxe Suite with Lounge',
                                           relief='flat', fg='gray10',
                                           anchor='w', justify='left', bg='gray85',
                                           bd=0, font=('Franklin Gothic Book', 12),
                                           command=lambda: select_room('Deluxe Suite with Lounge'),
                                           width=24, padx=8)
        ExecSuiteLounge_book = Checkbutton(bg_canvas, text='Executive Suite with Lounge',
                                           relief='flat', fg='gray10',
                                           anchor='w', justify='left', bg='gray85',
                                           bd=0, font=('Franklin Gothic Book', 12),
                                           command=lambda: select_room('Executive Suite with Lounge'),
                                           width=24, padx=8)
        bg_canvas.create_text(50, 502, text='Select Room(s): ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')
        bg_canvas.create_window(50, 525, window=DelxKngBed_book, anchor='nw')
        bg_canvas.create_window(350, 525, window=DelxTwnBed_book, anchor='nw')
        bg_canvas.create_window(50, 560, window=DelxSuiteLounge_book, anchor='nw')
        bg_canvas.create_window(350, 560, window=ExecSuiteLounge_book, anchor='nw')

        def add_booking_entry(a):
            global custid, roomno, customers, info, Name, ph, Ad, \
                Persnl_ID, chkin_date, chkout_date, room_choice
            if a == 1:
                Name = str(name_booking.get())
                ph = str(phn_booking.get())
                Ad = str(address_booking.get())
                Persnl_ID = str(P_Id_booking.get())
                chkin_date = str(book_cal_in.get_date())
                chkout_date = str(book_cal_out.get_date())
                add_booking_entry(2)
            elif a == 2:
                data_list = [Name, ph, Ad, Persnl_ID, chkin_date,
                             chkout_date, room_choice]
                coords = [(450, 180), (350, 210), (450, 240), (450, 270),
                          (100, 300), (340, 330), (100, 360)]
                check = 'empty'
                for data in data_list:
                    if data == '' and check != 'not-empty':
                        j = data_list.index(data)
                        for k in range(j):
                            if data_list[k] != '':
                                bg_canvas.delete('warning_fill')
                        bg_canvas.create_text(coords[j], text='** Please enter this info',
                                              anchor='nw', tags='warning_fill')
                        break
                else:
                    check = 'not-empty'
                    bg_canvas.delete('warning_fill')
                    if not (ph.isnumeric()) or not (len(ph)) == 10:
                        bg_canvas.create_text(coords[1], text='** Invalid Info',
                                              anchor='nw', tags='warning_type_phn')
                        check = 'invalid'
                    if not (Persnl_ID.isnumeric()):
                        bg_canvas.create_text(coords[3], text='** Invalid Info',
                                              anchor='nw', tags='warning_type_PId')
                        check = 'invalid'
                    if ph.isnumeric() and len(ph) == 10:
                        bg_canvas.delete('warning_type_phn')
                        ph = str(ph)
                    if Persnl_ID.isnumeric():
                        bg_canvas.delete('warning_type_PId')
                        Persnl_ID = str(Persnl_ID)
                    if ph.isnumeric() and len(ph) == 10 and Persnl_ID.isnumeric():
                        check = 'all good'

                if check == 'all good':
                    for customer in customers:
                        custid = int(customer['custid'])
                        roomno = int(customer['roomno'])
                    custid += 1
                    roomno += 1

                    info['name'] = Name
                    info['address'] = Ad
                    info['phno'] = ph
                    info['persnlid'] = Persnl_ID
                    info['custid'] = str(custid)
                    info['checkin'] = chkin_date
                    info['checkout'] = chkout_date
                    info['room'] = room_choice
                    info['roomno'] = roomno
                    customers.append(info.copy())

                    def total(cust_detail):
                        indate = datetime.strptime(cust_detail['checkin'], '%M/%d/%y')
                        outdate = datetime.strptime(cust_detail['checkout'], '%M/%d/%y')
                        delta = outdate - indate
                        delta = int(delta.days)
                        costing = rooms[cust_detail['room']] * delta
                        return delta, costing

                    cust_no_of_days, cust_bill = total(info)

                    mycon2 = connectsql.connect(host="localhost", user="root",  passwd="system123",
                                                     database=" hotelmanagement")
                    cursor = mycon2.cursor()
                    sql = "insert into customer (customer_name,cust_id, phone_no, no_of_days_to_stay, type_of_room_required, personal_id,"\
                           " start_date, end_date, address, bill_total_amt, room_no) VALUES(" + "'"+Name + "'" + "," +"'"+ str(custid) +"'"+ "," +"'"+ ph +"'"+ ","\
                           + str(cust_no_of_days) + "," +"'"+ str(room_choice) + "'"+"," +"'"+ str(Persnl_ID) +"'"+ "," + "'"+str(chkin_date)+"'" +\
                           "," +"'"+ str(chkout_date) +"'"+ "," +"'"+ str(Ad)+"'" + "," + str(cust_bill) + "," + str(roomno)+")"
                    print(sql)
                    db = cursor.execute(sql)
                    mycon2.commit()
                    cursor.close()
                    mycon2.close()
                print(customers)
                messagebox.showinfo("Confirmation Box", "Your hotel booking has been confirmed. Have a pleasant stay!")

        enter_booking = Button(bg_canvas, text='Enter Booking', font=('arial', 12, 'bold'), bd=0,
                               bg='green2', fg='gray10', activebackground='green4', width=18, height=1,
                               command=lambda: add_booking_entry(1))
        bg_canvas.create_window(500, 610, window=enter_booking)

    booking = Button(bg_canvas, text='Bookings', bd=0, highlightthickness=0, bg='green', fg='white',
                     font=('Microsoft New Tai Lue', 13, 'bold'), height=0, width=10, command=book_tab)
    tab_book = bg_canvas.create_window(10, 120, window=booking, anchor=W)

    def search():
        print('search')
        clear()

        # search page
        bg_canvas.create_text(325, 145, text='Search by Customer: (any detail)',
                              font=('Microsoft New Tai Lue', 16, 'bold'),
                              fill='black', anchor='n')
        bg_canvas.create_text(30, 180, text='Customer ID: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')
        custid_search = Entry(bg_canvas, font=12, width=8, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(130, 179, window=custid_search, anchor='nw')

        bg_canvas.create_text(235, 180, text='Name: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')

        name_search = Entry(bg_canvas, font=12, width=25, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(335, 179, window=name_search, anchor='nw')

        bg_canvas.create_text(30, 210, text='Phone No.: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')

        phone_search = Entry(bg_canvas, font=12, width=8, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(130, 209, window=phone_search, anchor='nw')

        bg_canvas.create_text(235, 210, text='Personal ID: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')

        P_Id_search = Entry(bg_canvas, font=12, width=25, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(335, 209, window=P_Id_search, anchor='nw')

        text_frame = Frame(bg_canvas)
        text_scrollbar = Scrollbar(text_frame, orient=VERTICAL)
        text_scrollbar.pack(side=RIGHT, fill=Y)
        search_results = Text(text_frame, width=52, height=13, wrap=WORD, font='BodoniMT 15', bd=0, bg='olivedrab1',
                              relief='groove', selectbackground='#BD89B6', spacing1=3, state=DISABLED,
                              yscrollcommand=text_scrollbar.set)
        search_results.pack()
        text_scrollbar.configure(command=search_results.yview)
        bg_canvas.create_window(30, 280, window=text_frame, anchor=NW, tags='text_frame')

        def get_total(cust_detail):
            indate = datetime.strptime(cust_detail['checkin'], '%M/%d/%y')
            outdate = datetime.strptime(cust_detail['checkout'], '%M/%d/%y')
            delta = outdate - indate
            delta = int(delta.days)
            costing = rooms[cust_detail['room']] * delta
            return delta, costing

        def run_search(a):
            global custid, roomno, customers, info, Name, ph, Ad, \
                Persnl_ID, chkin_date, chkout_date, room_choice

            search_results.configure(state=NORMAL)
            search_results.delete('1.0', END)
            search_results.configure(state=DISABLED)

            if a == 1:
                custid = str(custid_search.get())
                Name = str(name_search.get())
                ph = str(phone_search.get())
                Persnl_ID = str(P_Id_search.get())
                run_search(2)
            elif a == 2:
                check = 'not_int'
                if custid == '' and Name == '' and ph == '' and Persnl_ID == '':
                    bg_canvas.delete('warning_fill')
                    bg_canvas.create_text(225, 235, font=8, text='** Please enter some info!',
                                          anchor='nw', tags='warning_fill')
                else:
                    bg_canvas.delete('warning_fill')
                    if custid == '' and ph == '' and Persnl_ID == '':
                        bg_canvas.delete('warning_fill')
                        check = 'all good'
                    elif not (custid.isnumeric() or (ph.isnumeric() or len(ph) == 10) or Persnl_ID.isnumeric()):
                        if not (custid.isnumeric()):
                            check = 'invalid'
                        if not (ph.isnumeric() or len(ph) == 10):
                            check = 'invalid'
                        if not (Persnl_ID.isnumeric()):
                            print(check)
                    else:
                        bg_canvas.delete('warning_fill')
                        check = 'all good'
                    if check == 'invalid':
                        bg_canvas.create_text(225, 235, font=8, text='** Invalid info!',
                                              anchor='nw', tags='warning_fill')
                    elif check == 'all good':
                        bg_canvas.delete('warning_fill')
                        empty = True
                        if custid != '':
                            print(customers)
                        for customer_ in customers:
                            result = 'search'
                            if custid == customer_['custid'] and custid != '':
                                result = 'found'
                            if Name.lower() in customer_['name'].lower() and Name != '':
                                result = 'found'
                            if ph in customer_['phno'] and ph != '':
                                result = 'found'
                            if Persnl_ID == customer_['persnlid'] and Persnl_ID != '':
                                result = 'found'
                            if result == 'found':
                                print(result)
                                no_of_days, costing = get_total(customer_)
                                for record in customers:
                                    if record['custid'] == customer_['custid']:
                                        index = customers.index(record)
                                        customers[index]['bill'] = costing
                                result = 'Name: ' + str(customer_['name']) + '\ncustomer_ Id: ' + \
                                         str(customer_['custid']) + '\nAddress: ' + str(customer_['address']) + \
                                         '\nPhone no: ' + str(customer_['phno']) + '\nPersonal Id: ' + \
                                         str(customer_['persnlid']) + '\nCheck in: ' + str(customer_['checkin']) + \
                                         '\nCheck out: ' + str(customer_['checkout']) + '\nRoom: ' + \
                                         str(customer_['room']) + '\nRoom no: ' + str(customer_['roomno']) + \
                                         '\nCurrent total bill: ' + str(customer_['bill']) + '\n' + ('-' * 81)
                                search_results.configure(state=NORMAL)
                                search_results.insert(END, str(result) + '\n')
                                search_results.configure(state=DISABLED)
                                empty = False
                        else:
                            if empty:
                                search_results.configure(state=NORMAL)
                                search_results.delete('1.0', END)
                                search_results.insert('1.0', 'No matches found for search!')
                                search_results.configure(state=DISABLED)

        run_search_btn = Button(bg_canvas, text='Search', bd=0, highlightthickness=0, bg='black', fg='white',
                                font=('Microsoft New Tai Lue', 11, 'bold'), height=0, width=8,
                                command=lambda: run_search(1))
        bg_canvas.create_window(550, 240, window=run_search_btn, anchor='nw')

    search_cust = Button(bg_canvas, text='Search Customer', bd=0, highlightthickness=0, bg='black', fg='white',
                         font=('Microsoft New Tai Lue', 13, 'bold'), height=0, width=16, command=search)
    tab_search = bg_canvas.create_window(114, 120, window=search_cust, anchor=W)

    def billing():
        print('bill')
        clear()

        # billing page
        bg_canvas.create_text(325, 145, text='Type Customer Details: (any detail)',
                              font=('Microsoft New Tai Lue', 16, 'bold'),
                              fill='black', anchor='n')
        bg_canvas.create_text(30, 180, text='Customer ID: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')
        custid_bill = Entry(bg_canvas, font=12, width=8, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(130, 179, window=custid_bill, anchor='nw')

        bg_canvas.create_text(235, 180, text='Name: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')

        name_bill = Entry(bg_canvas, font=12, width=25, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(335, 179, window=name_bill, anchor='nw')

        bg_canvas.create_text(30, 210, text='Phone No.: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')

        phone_bill = Entry(bg_canvas, font=12, width=8, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(130, 209, window=phone_bill, anchor='nw')

        bg_canvas.create_text(235, 210, text='Personal ID: ',
                              font=('Microsoft New Tai Lue', 12),
                              fill='black', anchor='nw')

        P_Id_bill = Entry(bg_canvas, font=12, width=25, bg='olivedrab1', relief='groove')
        bg_canvas.create_window(335, 209, window=P_Id_bill, anchor='nw')

        text_frame = Frame(bg_canvas)
        text_scrollbar = Scrollbar(text_frame, orient=VERTICAL)
        text_scrollbar.pack(side=RIGHT, fill=Y)
        bill_total = Text(text_frame, width=52, height=13, wrap=WORD, font='BodoniMT 15', bd=0, bg='olivedrab1',
                          relief='groove',
                          selectbackground='#BD89B6', spacing1=3, state=DISABLED,
                          yscrollcommand=text_scrollbar.set)
        bill_total.pack()
        text_scrollbar.configure(command=bill_total.yview)
        bg_canvas.create_window(30, 280, window=text_frame, anchor=NW, tags='text_frame')

        def total(cust_detail):
            indate = datetime.strptime(cust_detail['checkin'], '%M/%d/%y')
            outdate = datetime.strptime(cust_detail['checkout'], '%M/%d/%y')
            delta = outdate - indate
            delta = int(delta.days)
            costing = rooms[cust_detail['room']] * delta
            return delta, costing

        def search_bill(a):
            print('searching...')
            global custid, roomno, customers, info, Name, ph, Ad, \
                Persnl_ID, chkin_date, chkout_date, room_choice

            bill_total.configure(state=NORMAL)
            bill_total.delete('1.0', END)
            bill_total.configure(state=DISABLED)

            if a == 1:
                custid = str(custid_bill.get())
                Name = str(name_bill.get())
                ph = str(phone_bill.get())
                Persnl_ID = str(P_Id_bill.get())
                search_bill(2)
            elif a == 2:
                check = 'not_int'
                if custid == '' and Name == '' and ph == '' and Persnl_ID == '':
                    bg_canvas.delete('warning_fill')
                    bg_canvas.create_text(225, 235, font=8, text='** Please enter some info!',
                                          anchor='nw', tags='warning_fill')
                else:
                    bg_canvas.delete('warning_fill')
                    if custid == '' and ph == '' and Persnl_ID == '':
                        bg_canvas.delete('warning_fill')
                        check = 'all good'
                    elif not (custid.isnumeric() or (ph.isnumeric() or len(ph) == 10) or Persnl_ID.isnumeric()):
                        if not (custid.isnumeric()):
                            check = 'invalid'
                        if not (ph.isnumeric() or len(ph) == 10):
                            check = 'invalid'
                        if not (Persnl_ID.isnumeric()):
                            print(check)
                    else:
                        bg_canvas.delete('warning_fill')
                        check = 'all good'
                    if check == 'invalid':
                        bg_canvas.create_text(225, 235, font=8, text='** Invalid info!',
                                              anchor='nw', tags='warning_fill')
                    elif check == 'all good':
                        bg_canvas.delete('warning_fill')
                        empty = True
                        if custid != '':
                            custid = int(custid)
                        for customer_ in customers:
                            result = 'search'
                            if str(custid) == str(customer_['custid']) and custid != '':
                                result = 'found'
                            if Name.lower() in customer_['name'].lower() and Name != '':
                                result = 'found'
                            if ph in customer_['phno'] and ph != '':
                                result = 'found'
                            if Persnl_ID == customer_['persnlid'] and Persnl_ID != '':
                                result = 'found'
                            if result == 'found':
                                no_of_days, costing = total(customer_)
                                for record in customers:
                                    if record['custid'] == customer_['custid']:
                                        index = customers.index(record)
                                        customers[index]['bill'] = costing
                                print(result)
                                result = (' ' * 35) + 'ALOHA RESORT' + '\nDate of Invoice: ' + str('2022/11/11') + \
                                         '\nCustomer_ Id: ' + str(customer_['custid']) + '\nName: ' + \
                                         str(customer_['name']) + '\nPhone no: ' + str(customer_['phno']) + \
                                         '\nPersonal Id: ' + str(customer_['persnlid']) + '\nRoom: ' + \
                                         str(customer_['room']) + '\nCharges per day: ' + str(rooms[customer_['room']]) \
                                         + '\nCheck in: ' + str(customer_['checkin']) + '\nCheck out: ' + \
                                         str(customer_['checkout']) + '\nStay duration in days: ' + str(no_of_days) + \
                                         '\nCurrent total bill: ' + str(customer_['bill']) + \
                                         '\n' + (' ' * 30) + 'Thank you and visit again!' + '\n' + ('-' * 81)
                                bill_total.configure(state=NORMAL)
                                bill_total.insert(END, str(result) + '\n')
                                bill_total.configure(state=DISABLED)
                                empty = False
                        else:
                            if empty:
                                bill_total.configure(state=NORMAL)
                                bill_total.delete('1.0', END)
                                bill_total.insert('1.0', 'No matches found for search!')
                                bill_total.configure(state=DISABLED)

        search_bill_btn = Button(bg_canvas, text='Search', bd=0, highlightthickness=0, bg='black', fg='white',
                                 font=('Microsoft New Tai Lue', 11, 'bold'), height=0, width=8,
                                 command=lambda: search_bill(1))
        bg_canvas.create_window(550, 240, window=search_bill_btn, anchor='nw')

    billing = Button(bg_canvas, text='Billing', bd=0, highlightthickness=0, bg='deep sky blue', fg='white',
                     font=('Microsoft New Tai Lue', 13, 'bold'), height=0, width=9, command=billing)
    tab_bill = bg_canvas.create_window(278, 120, window=billing, anchor=W)


login()

main_home.mainloop()

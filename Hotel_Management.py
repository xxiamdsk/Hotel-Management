#                                                              ☻☻☻☻☻☻╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦☻☻☻☻☻☻
# ﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿   MADE BY DEEPAK SINGH KUSHWAHA   ﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿﴾﴿
#                                                              ☻☻☻☻☻☻╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩☻☻☻☻☻☻


#                                                                    *******************************
#                                                               ****** Creating Database and Table ******
#                                                                    *******************************

import random
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='')
mycursor = db.cursor()
mycursor.execute('create database if not exists HOTEL_MANAGEMENT')

db = mysql.connector.connect(
    host='localhost', user='root', password='', database='HOTEL_MANAGEMENT')
mycursor = db.cursor()

mycursor.execute("create table if not exists hoteldata(Ccode int(5) primary key,Cname varchar(20),Cadd varchar(20),Cindate varchar(5),Coutdate varchar(5),Room_no varchar(5),Room_rent varchar(10),Food_bill varchar(10) default '00',Laudry_bill varchar(10) default '00' ,Game_bill varchar(10) default '00',SubTotal_bill varchar(10),Add_charges varchar(10) default '1800',GrandTotal_bill varchar(10))")
mycursor.execute("create table if not exists Room(Rooms varchar(10),Type varchar(45),Charges int(7),Features varchar(90),Occupancy int(45))")
mycursor.execute("create table if not exists Customer(Ccode int(5),Cid_type varchar(20), Cid_no varchar(15) primary key , Cname varchar(15), Ccontact_no varchar(15),Cadd varchar(20),Cindate varchar(5), Coutdate varchar(5), CNationality varchar(10))")

# data already in tables
# mycursor.execute("insert into hoteldata values(25,'Deepak','Morar,Gwalior',25,26,1000,6000,150,10,180,6340,1800,8140)")
# mycursor.execute("insert into hoteldata values(26,'Amit','Morar,Gwalior',5,8,1017,10000,5,0,50,10155,1800,11955)")
# mycursor.execute("insert into hoteldata values(27,'Anuj','New Delhi',12,20,1407,4000,130,7,80,4217,1800,6017)")
# mycursor.execute("insert into hoteldata values(28,'Kunal','Morar,Gwalior',5,8,1405,9000,20,0,90,9110,1800,10910)")
# mycursor.execute("insert into hoteldata values(29,'Smith','Canada',23,30,1008,3000,20,5,50,30075,1800,31875)")
# mycursor.execute("insert into hoteldata values(30,'Alex','America',25,30,1012,3000,30,6,0,30036,1800,31836)")

# mycursor.execute("insert into Room values('1-500','Duplex',6000,'Two rooms on same floor connected by common stairs',5)")
# mycursor.execute("insert into Room values('501-1000','Cabana',5000,'Faces water body,beach or a swimming pool',3)")
# mycursor.execute("insert into Room values('1001-1500','Lanai',4000,'This room faces a landscape, a waterfall, or a garden',4)")
# mycursor.execute("insert into Room values('1501-2000','Suit',3000, 'It is composed of one or more bedrooms, a living room, and a dining area',12)")

# mycursor.execute("insert into Customer values(25,'Aadhaar card',412563578952,'Deepak',8269513294,'Morar,Gwalior',25,26,'Indian' )")
# mycursor.execute("insert into Customer values(26,'Pan card', 5874695325,'Amit', 9063560847,'Morar,Gwalior',5,8,'Indian')")
# mycursor.execute("insert into Customer values(27,'Pan card', 8456958236, 'Anuj', 9770563593,'New Delhi',12,20,'Indian')")
# mycursor.execute("insert into Customer values(28,'Service Id',8546952156,'Kunal',4856985123,'Morar,Gwalior',5,8,'Indian')")
# mycursor.execute("insert into Customer values(29,'Voter Id Card',45896244,'Smith',6598541256,'Canada',23,30,'Canadian')")
# mycursor.execute("insert into Customer values(30,'Aadhaar card',485962578545,'Alex',6325489652,'America',25,30,'American')")
db.commit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------


def speciality():
    db = mysql.connector.connect(
        host='localhost', user='root', password='123456', database='HOTEL_MANAGEMENT')
    mycursor = db.cursor()
    qry = ("select * from room")
    mycursor.execute(qry)
    print("\nDESCRIPTION:")
    print("Located on the hills of Nice, a short distance from the famous Promenade des Anglais, Hotel Anis is one of the hotels in the Costa Azzurra(or Blue Coast) able to satisfy the different needs of its guests with comfort and first rate services. It is only 2 km from the airport and from highway exits. The hotel has a large parking area , a real luxury in a city like Nice.At Hotel Anis you will be welcomed amongst olive trees, citron trees and magnolias,in gardens that hide exotic plants and in a wonderful outdoor pool with deck chairs; protected against the sun’s rays by big umbrellas you can enjoy a drink amongst the wisteria bushes.The spacious rooms of this beautiful Mediterranean residence offer thepossibility of enjoying a rich breakfast buffet on the splendid outdoor terrace where guests may continue to enjoy frequent sunny days and mild temperature, even during the winter months.The hotel’s reception is open 24 hours a day and offers booking services for guided tours to Monte Carlo.\n")
    for (Rooms, Type, Charges, Features, Occupancy) in mycursor:
        print("We have Rooms", Rooms, "of type", Type, ",it has",
              Features, "and occupancy of", Occupancy, "persons.")
    db.commit()
    print("SERVICES:")
    print("For the disabled, Breakfast, Restaurant, Adsl wi-fi internet, Fax, Newspapers, Transfer, Tourist information, Small animals welcome, Private parking,Guarded garage, 24h reception, 24h bar, Beaches at 500 m, Shuttle bus stop for the airport only 10 minutes away.\n")
    print("FACILITIES:")
    print("ReceptionHall, Bar, Pool 10.00 a.m. – 6.00 p.m.\n")
    print("BOOKING:")
    print("Excursions, Guided tours, Private parties")
    mycursor.close()
    db.close()


#                                                                   **********************************
#                                                              ****** Function,hotel fare calculator *******
#                                                                   **********************************

def hotelfarecal():
    while True:
        print("\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1.Booking for Room")
        print("2.Show Customer Record")
        print("3.Search Customer Record")
        print("4.Delete Customer Record")
        print("5.Update Customer Record")
        print("6.Return to Main Menu")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        b = (input("\nEnter your choice:"))

        if (b == '1'):
            z = 'y'
            while (z == 'y'):
                inputdata()
                z = input("\nDo you want to continue..(y/n):")
            if (z == 'n'):
                return hotelfarecal()
            else:
                print("Invalid Input!!")
                z = input("\nDo you want to continue..(y/n):")
        elif (b == '2'):
            z = 'y'
            while z == 'y':
                display()
                z = input("\nDo you want to continue..(y/n):")
            if (z == 'n'):
                return hotelfarecal()
            else:
                print("Invalid Input!!")
                z = input("\nDo you want to continue..(y/n):")
        elif (b == '3'):
            z = 'y'
            while (z == 'y'):
                search()
                z = input("\nDo you want to continue..(y/n):")
            if (z == 'n'):
                return hotelfarecal()
            else:
                print("Invalid Input!!")
                z = input("\nDo you want to continue..(y/n):")
        elif (b == '4'):
            z = 'y'
            while (z == 'y'):
                delete()
                z = input("\nDo you want to continue..(y/n):")
            if (z == 'n'):
                return hotelfarecal()
            else:
                print("Invalid Input!!")
                z = input("\nDo you want to continue..(y/n):")
        elif (b == '5'):
            z = 'y'
            while (z == 'y'):
                update()
                z = input("\nDo you want to continue..(y/n):")
            if (z == 'n'):
                return hotelfarecal()
            else:
                print("Invalid Input!!")
                z = input("\nDo you want to continue..(y/n):")
        elif (b == '6'):
            break
        else:
            print("Invalid Input......")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------


#                                                                            ******************
#                                                                       ****** Inserting data ******
#                                                                            ******************


def inputdata():
    r = 0
    l = 0
    p = 0
    s = 0
    rm = 0
    db = mysql.connector.connect(
        host='localhost', user='root', password='123456', database='HOTEL_MANAGEMENT')
    mycursor = db.cursor()
    Ccode = input("\nEnter Customer Code:")
    Cname = input("Enter Customer Name:")
    Cadd = input("Enter Customer Address:")
    Cindate = input("Enter Customer Check in Date:")
    Coutdate = input("Enter Customer Check out Date:")
    Cid_type = input("Enter your Identity card name:")
    Cid_no = input("Enter your Identity number:")
    Ccontact_no = input("Enter you Contact number:")
    CNationality = input("Enter your nationality:")
    print("\n")

#                                                                       ***********************
#                                                                  ****** Choose Room for rent******
#                                                                       ***********************

    print("We have the following rooms for you:-")
    print("1.  Duplex---->Rs 6000 PN\-")
    print("2.  Cabana---->Rs 5000 PN\-")
    print("3.  Lanai---->Rs 4000 PN\-")
    print("4.  Suit---->Rs 3000 PN\-")
    print("5.  Next")
    while True:
        x = int(input("\nEnter you choice:"))
        if (x == 1):
            n = int(input("For How Many Nights Did You Stay:"))
            print("You have opted room Duplex")
            s = s+6000*n
            Room_no = random.randint(1, 501)
            break
            print("Your Room Number is:", Room_no)
        elif (x == 2):
            n = int(input("For How Many Nights Did You Stay:"))
            print("You have opted room Cabana")
            s = s+5000*n
            Room_no = random.randint(501, 1001)
            print("Your Room Number is:", Room_no)
            break
        elif (x == 3):
            n = int(input("For How Many Nights Did You Stay:"))
            print("You have opted room Lanai")
            s = s+4000*n
            Room_no = random.randint(1001, 1501)
            print("Your Room Number is:", Room_no)
            break
        elif (x == 4):
            n = int(input("For How Many Nights Did You Stay:"))
            print("You have opted room Suit")
            s = s+3000*n
            Room_no = random.randint(1501, 2001)
            print("Your Room Number is:", Room_no)
            break
        elif (x == 4):
            n = int(input("For How Many Nights Did You Stay:"))
            print("You have opted room Suit")
            s = s+3000*n
            Room_no = random.randint(2001, 2501)
            print("Your Room Number is:", Room_no)
            break
        elif (x == 5):
            Room_no = random.randint(2001, 2501)
            break
        else:
            print("Please choose a room")
    print("\nYour room rent is", s, 'RS')

#                                                                         **************************
#                                                                    ****** Choose Restaurant Menu ******
#                                                                         **************************

    print("\n")
    print("*****RESTAURANT MENU*****")
    print("1.water----->Rs 20", "\n2.tea----->Rs 10", "\n3.breakfast combo--->Rs 90",
          "\n4.lunch---->Rs 110", "\n5.dinner--->Rs 150", "\n6.Next")
    while True:
        c = int(input("\nEnter your choice:")) 
        if (c == 1):
            d = int(input("Enter the quantity:"))
            r = r+20*d
        elif (c == 2):
            d = int(input("Enter the quantity:"))
            r = r+10*d
        elif (c == 3):
            d = int(input("Enter the quantity:"))
            r = r+90*d
        elif (c == 4):
            d = int(input("Enter the quantity:"))
            r = r+110*d
        elif (c == 5):
            d = int(input("Enter the quantity:"))
            r = r+150*d
        elif (c == 6):
            break
        else:
            print("Invalid option")
        
    print("\nTotal food Cost=Rs ", r)

#                                                                             ***********************
#                                                                        ****** Choose Laundry Menu ******
#                                                                             ***********************

    print("\n")
    print("******LAUNDRY MENU*******")
    print("1.Shorts----->Rs 3", "\n2.Trousers----->Rs 4", "\n3.Shirt--->Rs 5",
         "4.Jeans---->Rs 6", "\n5.Girlsuit--->Rs 8", "\n6.Next")
    while True:
        e = int(input("\nEnter your choice:"))
        if (e == 1):
            f = int(input("Enter the quantity:"))
            l = l+3*f
        elif (e == 2):
            f = int(input("Enter the quantity:"))
            l = l+4*f
        elif (e == 3):
            f = int(input("Enter the quantity:"))
            l = l+5*f
        elif (e == 4):
            f = int(input("Enter the quantity:"))
            l = l+5*f
        elif (e == 5):
            f = int(input("Enter the quantity:"))
            l = l+6*f
        elif (e == 6):
            break
        else:
            print("Invalid option")
    print("\nTotal Laundary Cost=Rs", l)

#                                                                           ********************
#                                                                      ****** Choose Game Menu ******
#                                                                           ********************

    print("\n")
    print("******GAME MENU*******")
    print("1.Table tennis----->Rs 60", "\n2.Bowling----->Rs 80", "\n3.Snooker--->Rs 70",
         "4.Video games---->Rs 90", "\n5.Pool--->Rs 50==6", "\n6.Next")
    while True:
        g = int(input("\nEnter your choice:"))
        if (g == 1):
            h = int(input("No. of hours:"))
            p = p+60*h
        elif (g == 2):
            h = int(input("No. of hours:"))
            p = p+80*h
        elif (g == 3):
            h = int(input("No. of hours:"))
            p = p+70*h
        elif (g == 4):
            h = int(input("No. of hours:"))
            p = p+90*h
        elif (g == 5):
            h = int(input("No. of hours:"))
            p = p+50*h
        elif (g == 6):
            break
        else:
            print("Invalid option")
    print("\nTotal Game Bill=Rs", p)

#                                                   *********************************************************************
#                                              ****** Calulating Sub Total Bill,Additional Charges and Grand Total Bill ******
#                                                   *********************************************************************

    SubTotal_bill = s+r+l+p
    Add_charges = 1800
    Room_rent = s
    Game_bill = p
    Food_bill = r
    Laudry_bill = l
    GrandTotal_bill = SubTotal_bill+Add_charges
    print("\nYou have to pay Rs", GrandTotal_bill)

    rec = ("insert into hoteldata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    cotm = ("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data1 = (Ccode, Cid_type, Cid_no, Cname, Ccontact_no,
             Cadd, Cindate, Coutdate, CNationality)
    data2 = (Ccode, Cname, Cadd, Cindate, Coutdate, Room_no, Room_rent, Food_bill,
             Laudry_bill, Game_bill, SubTotal_bill, Add_charges, GrandTotal_bill)
    mycursor.execute(cotm, data1)
    mycursor.execute(rec, data2)
    db.commit()
    mycursor.close()
    print("\nRecord Inserted.......")
    db.close()

#                                                                       ****************************
#                                                                  ****** Show Details of Customer ******
#                                                                       ****************************


def display():
    print("\n")
    print("1.Display all records")
    print("2.Display through code number")
    d = input("\nEnter your choice:")
    if (d == '1'):
        db = mysql.connector.connect(
            host='localhost', user='root', password='123456', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        qry = ("select h.Ccode,h.Cname,h.Cadd,h.Cindate,h.Coutdate,h.Room_no,c.CNationality,c.Ccontact_no,c.Cid_type,c.Cid_no from hoteldata h,\
customer c where h.Ccode=c.Ccode")
        mycursor.execute(qry)
        for (Ccode, Cname, Cadd, Cindate, Coutdate, Room_no, CNationality, Ccontact_no, Cid_type, Cid_no) in mycursor:
            print("\n")
            print("Customer details.......")
            print("Customer code:", Ccode)
            print("Customer name:", Cname)
            print("Customer Id type:", Cid_type)
            print("Customer Id Number:", Cid_no)
            print("Customer address:", Cadd)
            print("customer Nationality:", CNationality)
            print("Check in date:", Cindate)
            print("Check out date", Coutdate)
            print("Room number:", Room_no)
            print("Customer Contact number:", Ccontact_no)
            print("___________________________________")
        mycursor.close()
        print("\nIt's All record")
        db.close()

    elif (d == '2'):
        db = mysql.connector.connect(
            host='localhost', user='root', password='123456', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = input("\nEnter code of customer:")
        qry = ("select h.Ccode,h.Cname,h.Cadd,h.Cindate,h.Coutdate,h.Room_no,c.CNationality,c.Ccontact_no,c.Cid_type,c.Cid_no from hoteldata h, customer c where h.Ccode=c.Ccode and h.Ccode=%s")
        rec_code = (Ccode,)
        mycursor.execute(qry, rec_code)
        rec_count = 0
        for (Ccode, Cname, Cadd, Cindate, Coutdate, Room_no, CNationality, Ccontact_no, Cid_type, Cid_no) in mycursor:
            rec_count += 1
            print('\nRecord Found......')
            print("Customer details.......")
            print("Customer code:", Ccode)
            print("Customer name:", Cname)
            print("Customer Id type:", Cid_type)
            print("Customer Id Number:", Cid_no)
            print("Customer address:", Cadd)
            print("customer Nationality:", CNationality)
            print("Check in date:", Cindate)
            print("Check out date", Coutdate)
            print("Room number:", Room_no)
            print("Customer Contact numbber:", Ccontact_no)
        if (rec_count == 0):
            print("\nRecord not found!!")
            db.commit()
            mycursor.close()
            db.close()

    else:
        print("Invalid Input!!")


#                                                                          *******************
#                                                                     ****** Search Customer ******
#                                                                          *******************

def search():
    db = mysql.connector.connect(
        host='localhost', user='root', password='123456', database='HOTEL_MANAGEMENT')
    mycursor = db.cursor()
    Ccode = input("\nEnter Customer Code to be Searched in Hotel:")
    qry = ("select * from hoteldata where Ccode=%s")
    rec_srch = (Ccode,)
    mycursor.execute(qry, rec_srch)
    rec_count = 0
    for (Ccode, Cname, Cadd, Cindate, Coutdate, Room_no, Room_rent, Food_bill, Laudry_bill, Game_bill, SubTotal_bill, Add_charges, GrandTotal_bill) in mycursor:
        rec_count += 1
        print('\nRecord Found')
        print("Customer details......")
        print("Customer code:", Ccode)
        print("Customer name:", Cname)
        print("Customer address:", Cadd)
        print("Check in date:", Cindate)
        print("Check out date", Coutdate)
        print("Room number:", Room_no)
        print("Room rent is:", Room_rent)
        print("Food bill is:", Food_bill)
        print("Laundary bill is:", Laudry_bill)
        print("Game bill is:", Game_bill)
        print("Sub total bill is:", SubTotal_bill)
        print("Additional Service Charges is:", Add_charges)
        print("Grand Total bill is:", GrandTotal_bill)
    if (rec_count == 0):
        print("\nRecord not found!!")
        db.commit()
        mycursor.close()
        db.close()

#                                                                           *******************
#                                                                      ****** Delete Customer ******
#                                                                           *******************


def delete():
    db = mysql.connector.connect(
        host='localhost', user='root', password='123456', database='HOTEL_MANAGEMENT')
    mycursor = db.cursor()
    Ccode = input("\nEnter Customer Code to be delete from Hotel:")
    qry = ("delete from hoteldata where Ccode=%s")
    qry1 = ("delete from customer where Ccode=%s")
    del_rec = (Ccode,)
    mycursor.execute(qry, del_rec)
    mycursor.execute(qry1, del_rec)
    print("\nRecord Deleted......")
    db.commit()
    mycursor.close()
    db.close()

#                                                                           *******************
#                                                                      ****** Update Customer ******
#                                                                           *******************


def update():
    print("\nWhich Data Should be Updated......")
    print("1.Customer Name:")
    print("2.Customer Address")
    print("3.Customer in Date")
    print("4.Customer out Date")
    print("5.Customer Room Number")
    print("6.Customer Room Rent")
    print("7.Customer Food bill")
    print("8.Customer Laundary bill")
    print("9.Custmer Game bill")

    c = int(input("\nSelect your Choice:"))
    if (c == 1):
        db = mysql.connector.connect(
            host='localhost', user='root', password='123456', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = input('\nEnter Code of Customer to be Updated:')
        qry = ('select * from hoteldata where Ccode=%s')
        Cname = input("Enter Customer Name:")
        q = ('update hoteldata set Cname=%s where Ccode=%s')
        data = (Cname, Ccode)
        mycursor.execute(q, data)
        print('\nRecord Updated.....')
        db.commit()
        mycursor.close()
        db.close()


    elif (c == 2):
        db = mysql.connector.connect(
            host='localhost', user='root', password='123456', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = int(input('\nEnter Code of Customer to be Updated:'))
        qry = ('select * from hoteldata where Ccode=%s')
        Cadd = input("Enter Customer Adrress:")
        q = ('update hoteldata set Cadd=%s where Ccode=%s')
        data = (Cadd, Ccode)
        mycursor.execute(q, data)
        print('\nRecord Updated......')
        db.commit()
        mycursor.close()
        db.close()

    elif (c == 3):
        db = mysql.connector.connect(
            host='localhost', user='root', password='123456', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = int(input('\nEnter Code of Customer to be Updated:'))
        qry = ('select * from hoteldata where Ccode=%s')
        Cindate = input("Enter Customer in Date:")
        q = ('update hoteldata set Cindate=%s where Ccode=%s')
        data = (Cindate, Ccode)
        mycursor.execute(q, data)
        print('\nRecord Updated......')
        db.commit()
        mycursor.close()
        db.close()

    elif (c == 4):
        db = mysql.connector.connect(
            host='localhost', user='root', password='123456', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = int(input('\nEnter Code of Customer to be Updated:'))
        qry = ('select * from hoteldata where Ccode=%s')
        Coutdate = input("Enter Customer out Date:")
        q = ('update hoteldata set Coutdate=%s where Ccode=%s')
        data = (Coutdate, Ccode)
        mycursor.execute(q, data)
        print('\nRecord Updated......')
        db.commit()
        mycursor.close()
        db.close()

    elif (c == 5):
        db = mysql.connector.connect(
            host='localhost', user='root', password='123456', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = int(input('\nEnter Code of Customer to be Updated:'))
        qry = ('select * from hoteldata where Ccode=%s')
        Room_no = input("Enter Customer Room number:")
        q = ('update hoteldata set Room_no=%s where Ccode=%s')
        data = (Room_no, Ccode)
        mycursor.execute(q, data)
        print('\nRecord Updated......')
        db.commit()
        mycursor.close()
        db.close()

    else:
        print("Invalid Input!!")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------


print("\n\t\t\t\t\t\t\t\t      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎░░ WELCOME TO EMIRATES PALACE ░░֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎")
print("\t\t\t\t\t\t\t\t      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")

while True:
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1.Speciality of your Hotel")
    print("2.Customer Management")
    print("3.Booking for Private Party")
    print("4.EXIT")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    b = input("\nEnter your choice:")
    if (b == '1'):
        speciality()
    elif (b == '2'):
        hotelfarecal()
    # elif (b=='3'):
    #     party()
    elif (b == '4'):
        quit()
    else:
        print("Wrong Choice")

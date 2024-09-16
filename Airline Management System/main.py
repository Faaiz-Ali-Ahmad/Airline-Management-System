# **************** Project on Airlines  Booking  System *************************
import datetime as dt
import mysql.connector as ms
import os

def welcome():
    print("---------------------------------------------------------------------------------------")
    print("\n\n****************** W E L C O M E **************************\n\n ")
    print(" AIRLINES   BOOKING   SYSTEM")
    print(" \n D E V E L O P E D  B Y :\n")
    print(" \n Faaiz Ali Ahmad \n")
    
def INTRO():
    
    intro = '''
    ---------------------------------------------------------------------------
              W E L C O M E    T O      I N D I A N     A I R L I N E S
          ________________________________________________________________
                
    WELCOME TO THE INDIAN AIRLINES. WE PROVICE YOU FACILITY TO BOOK YOUR SEETS
    IN FOLLOWING CATEGORIES: 
        CLASSES                
    ****************           
         EXECUTIVE
         BUSINESS
         ECONOMY
         
   # THE GST IS APPLICABLE ON THE BOOKING AMOUTNT AS PER GOVERNMENT GUIDLINES. 
   # IN CASE OF CANCELLATION OF TICKETS THE CANCELLATION CHARGES ARE APPLICABLE
     AS PER THE GOVERNMENT GUIDLINES.
  '''
    print(intro)

def ADDDATA():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="airlines")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        i   = input("Enter Passenger ID  : ")
        nm  = input("Enter Name          : ")
        ag  = input("Enter Age           : ")
        add = input("Enter Address       : ")
        mob = input("Enter Mobile No.    : ")
        try:
            st = "insert into passenger values( {}, '{}', '{}', '{}', '{}', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)".format(i, nm, ag, add, mob)
            cursor.execute(st)
            conobj.commit()
            print("\n\nData added successfully\n")
        except ms.ProgrammingError:
            print('[ NO TABLE EXIST ]')
            return
        ch = input("Press y to add more records : ")
    conobj.close()
    

def DISPLAYDATA():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="airlines")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        st = "select * from passenger order by id"
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    f = 0
    print("\n\t\t\t\tLIST  OF  PASSENGERS \n")
    while d is not None:
        f = 1
        print("---------------------------------------------------------------------------------------")
        print(" PASSENGER ID : ", d[0], end = ' ')
        print(" Name : ", d[1])
        print(" Age : ", d[2], end = ' ')
        print(" Address : ", d[3], end = ' ')
        print(" Mobile No. : ", d[4])
        print(" Flight No. : ", d[5], end = ' ')
        print(" Flight Name : ", d[6], end = ' ')
        print(" Class : ", d[7], end = ' ')
        print(" Seat No. : ", d[8])            
        print(" Source : ", d[9], end = ' ')
        print(" Destination : ", d[10])  
        print(" Fare : ", d[11], end = ' ')
        print(" Date of Journey : ", d[12])
        print("---------------------------------------------------------------------------------------")
        d = cursor.fetchone()
    conobj.close()
    if f == 0:
        print("\n\nNo Record Exist\n")

def SEARCHDATA():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="airlines")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = input("Enter Passenger ID : ")
        st = "select * from passenger where id = '{}'".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        print("\n\t\t\t\t[ SEARCH  RESULT ... ]\n")
        print("---------------------------------------------------------------------------------------")
        print(" PASSENGER ID    : ", d[0])
        print(" Name            : ", d[1])
        print(" Age             : ", d[2])
        print(" Address         : ", d[3])
        print(" Mobile No.      : ", d[4])
        print(" Flight No.      : ", d[5])
        print(" Flight Name     : ", d[6])
        print(" Class           : ", d[7])
        print(" Seat No.        : ", d[8])            
        print(" Source          : ", d[9])
        print(" Destination     : ", d[10])  
        print(" Fare            : ", d[11])
        print(" Date of Journey : ", d[12])
        print("---------------------------------------------------------------------------------------")
    else:
        print("\n\nRecord Not Found For This ID\n")
    conobj.close()
    
    
def EDITDATA():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="airlines")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = input("Enter Passenger ID : ")
        st = "select * from passenger where id = '{}'".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        print("\n\t\t\t\t[ MODIFYING  RECORDS ]\n")
        n = input("Enter new Name or press 0 to unchange : ")
        if n !='0':
            st = "update passenger set name = '{}' where id = '{}'".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = int(input("Enter new Age or press 0 to unchange : "))
        if n !='0':
            st = "update passenger set age = {} where id = '{}'".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = input("Enter new Address or press 0 to unchange : ")
        if n !='0':
            st = "update passenger set address = '{}' where id = '{}'".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = input("Enter new Mobile No. or press 0 to unchange : ")
        if n !='0':
            st = "update passenger set mobile = '{}' where id = '{}'".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = input("Enter new Flight No. press 0 to unchange : ")
        if n !='0':
            st = "update passenger set flightno = '{}' where id = '{}'".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = input("Enter new Flight Name or press 0 to unchange : ")
        if n !='0':
            st = "update passenger set flightname = '{}' where id = '{}'".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = input("Enter new Source Point or press 0 to unchange : ")
        if n !='0':
            st = "update passenger set source = '{}' where id = '{}'".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = input("Enter new Destination Point or press 0 to unchange : ")
        if n !='0':
            st = "update passenger set destination = '{}' where id = '{}'".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = input("Enter new Class Type or press 0 to unchange : ")
        if n !='0':
            st = "update passenger set class = '{}' where id = '{}'".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = input("Enter new Seat No. or press 0 to unchange : ")
        if n !='0':
            st = "update passenger set seatno = '{}' where id = '{}'".format(n, i)
            cursor.execute(st)
            conobj.commit()
        n = int(input("Enter new Fare or press 0 to unchange : "))
        if n != 0:
            st = "update passenger set fare = {} where id = '{}'".format(n, i)
            cursor.execute(st)
            conobj.commit()
        conobj.close()
        print("\n\nRecord Modified Successfully\n")
    else:
        print("\n\nRecord Not Found For This ID\n")
    conobj.close()
    
def REMOVEDATA():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="airlines")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = input("Enter Passenger ID : ")
        st = "select * from passenger where id = '{}'".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        st = "delete from passenger where id = '{}'".format(i)
        cursor.execute(st)
        conobj.commit()
        conobj.close()
        print("\n\nRecord Deleted Successfully\n")
    else:
        print("\n\nRecord Not Found For This ID\n")
    conobj.close()    

    
def BOOKING():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="airlines")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = input("Enter Passenger ID : ")
        st = "select * from passenger where id = '{}'".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        print("\n\t\t\t\t[ TICKET  BOOKING . . . ]\n")
        print("______________________")
        print("SELECT A CLASS")
        print("Press 1 FOR EXECUTIVE")
        print("Press 2 FOR BUSINESS ")
        print("Press 3 FOR ECONOMY")
        print("Press 0 FOR EXIT BOOKING")
        ch = int(input("Enter your choice : "))
        if ch != 0:
            fno = input("Enter Flight Number : ")
            fnm = input("Enter Flight Name : ")
            sno = input("Enter Seat Number : ")
            src = input("Enter Source Point : ")
            dst = input("Enter Destination Point : ")
            far = input("Enter Fare : ")
            dat = dt.date.today()
            st = "update passenger set class = '{}', flightno = '{}', flightname = '{}', seatno = '{}', source = '{}', destination = '{}', fare = '{}', doj = '{}' where id = '{}'".format(ch, fno, fnm, sno, src, dst, far, dat, i)
            cursor.execute(st)
            conobj.commit()
            print("\n\nBOOKING DONE SUCCESSFULLY\n")
        else:
            print("Booking Exit")
            return
        st = "select * from passenger where id = '{}'".format(i)
        cursor.execute(st)
        d = cursor.fetchone()
        print("\n\nBooking Confirmed")
        print("---------------------------------------------------------------------------------------")
        print("\t\tINDIAN  AIRLINES\n")
        print(" PASSENGER ID    : ", d[0], end = ' ')
        print(" Name            : ", d[1])
        print(" Age             : ", d[2], end = ' ')
        print(" Address         : ", d[3], end = ' ')
        print(" Mobile No.      : ", d[4])
        print(" Flight No.      : ", d[5], end = ' ')
        print(" Flight Name     : ", d[6])
        print(" Class           : ", d[7], end = ' ')
        print(" Seat No.        : ", d[8])            
        print(" Source          : ", d[9], end = ' ')
        print(" Destination     : ", d[10])  
        print(" Fare            : ", d[11], end = ' ')
        print(" Date of Journey : ", d[12])
        print("---------------------------------------------------------------------------------------")
    else:
        print("\n\nRecord Not Found For This ID\n")
    conobj.close()
    
                    
def CANCELLATION():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="airlines")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = input("Enter Passenger ID : ")
        st = "select * from passenger where id = '{}'".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        print("\n\t\t\t\t[ TICKET  CANCELLATION . . . ]\n")
        print("---------------------------------------------------------------------------------------")
        print("\t\tINDIAN  AIRLINES\n")
        print(" PASSENGER ID    : ", d[0], end = ' ')
        print(" Name            : ", d[1])
        print(" Age             : ", d[2], end = ' ')
        print(" Address         : ", d[3], end = ' ')
        print(" Mobile No.      : ", d[4])
        print(" Flight No.      : ", d[5], end = ' ')
        print(" Flight Name     : ", d[6])
        print(" Class           : ", d[7], end = ' ')
        print(" Seat No.        : ", d[8])            
        print(" Source          : ", d[9], end = ' ')
        print(" Destination     : ", d[10])  
        print(" Fare            : ", d[11], end = ' ')
        print(" Date of Journey : ", d[12])
        print("---------------------------------------------------------------------------------------")
        ch = input("ARE YOU SURE TO CANCEL THE TICKET BOOKED (Y / N) : ")
        if ch == 'Y' or ch == 'y':
            print("\n\nBooking Cancelled\n")
            print("Amount ", d[11], " will be Credit in your account within 24 hours.")
            st = "update passenger set class = NULL, flightno = NULL, flightname = NULL, seatno = NULL, source = NULL, destination = NULL, fare = NULL, doj = NULL where id = '{}'".format(i)
            cursor.execute(st)
            conobj.commit()
            print("\n\nBOOKING CANCELLEDE SUCCESSFULLY\n")
        else:
            print("Cencellation Abott... ")
            return
    else:
        print("\n\nRecord Not Found For This ID\n")
    conobj.close()
        
def PRINTTICKET():
    try:
        conobj = ms.connect(host="localhost", user="root", passwd="pass", database="airlines")
    except ms.ProgrammingError:
        print('[ NO DATABASE FOUND ]')
        return
    cursor = conobj.cursor()
    try:
        i = input("Enter Passenger ID : ")
        st = "select * from passenger where id = '{}'".format(i)
        cursor.execute(st)
    except ms.ProgrammingError:
        print('[ NO TABLE EXIST ]')
        return
    d = cursor.fetchone()
    if d is not None:
        print("     INDIAN  AIRLINES \n")
        print("      ( E-TICKET ) \n")
        print("---------------------------------------------------------------------------------------")
        print("\t\tINDIAN  AIRLINES\n")
        print(" PASSENGER ID    : ", d[0], end = ' ')
        print(" Name            : ", d[1])
        print(" Age             : ", d[2], end = ' ')
        print(" Address         : ", d[3], end = ' ')
        print(" Mobile No.      : ", d[4])
        print(" Flight No.      : ", d[5], end = ' ')
        print(" Flight Name     : ", d[6])
        print(" Class           : ", d[7], end = ' ')
        print(" Seat No.        : ", d[8])            
        print(" Source          : ", d[9], end = ' ')
        print(" Destination     : ", d[10])  
        print(" Fare            : ", d[11], end = ' ')
        print(" Date of Journey : ", d[12])
        print("---------------------------------------------------------------------------------------")
    else:
        print("\n\nRecord Not Found For This ID\n")
    conobj.close()
   
def CHANGEPASSWORD():
    try:
        file = open('pass.txt', 'r')
    except FileNotFoundError:
        print("Your OTP is   123")
        n = input("Enter OTP : ")
        if n == '123':
            a = input("Enter New Password : ")
            b = input("Re-Enter New Password : ")
            if a == b:
                with open('pass.txt', 'w') as file2:
                    file2.write(a)
                    print("\n[ PASSWORD  RESET  SUCCESSFULLY ]")
        return
    try:
        n = input("Enter Old Password : ")
        data = file.read()
        if n == data:
            a = input("Enter New Password : ")
            b = input("Re-Enter New Password : ")
            if a == b:
                with open('temp.txt', 'w') as file2:
                    file2.write(a)
                    print("\n[ PASSWORD  RESET  SUCCESSFULLY ]")
                file.close()
                os.remove('pass.txt')
                os.rename('temp.txt','pass.txt')
    except EOFError :
        file.close()
        
def ADMIN():
    try:
        file = open('pass.txt', 'r')
    except FileNotFoundError:
        CHANGEPASSWORD()
    try:
        file = open('pass.txt', 'r')
        d = file.read()
        file.close()
        n = input("Enter Password : ")
        if n == d:
            ch = '1'
            while ch != '0':
                print("---------------------------------------------------------------------------------------")
                print("1.  FOR  INSTRUCTIONS")
                print("2.  ADD PASSENGER")
                print("3.  DISPLAY PASSENGERS")
                print("4.  SEARCH  PASSENGERS")
                print("5.  EDIT  PASSENGER")
                print("6.  REMOVE A PASSENGER")
                print("7.  BOOKING")
                print("8.  CANCELLATION")
                print("9.  PRINT  TICKET")
                print("10. CHANGE PASSWORD")
                print("0.  EXIT")
                ch = input("Enter your choice : ")
                print("---------------------------------------------------------------------------------------")
                if ch == '1' :
                    INTRO()
                elif ch == '2':
                    ADDDATA()
                elif ch == '3':
                    DISPLAYDATA()
                elif ch == '4':
                    SEARCHDATA()
                elif ch == '5':
                    EDITDATA()
                elif ch == '6':
                    REMOVEDATA()
                elif ch == '7':
                    BOOKING()
                elif ch == '8':
                    CANCELLATION()
                elif ch == '9':
                    PRINTTICKET()
                elif ch == '10':
                    CHANGEPASSWORD()
                elif ch == '0':
                    break
                else:
                    print("Invalid Choice")
        else:
            print("[ ACCESS  DENIED ]")
    except EOFError :
        file.close()
    
#-------------------MAIN----------------------------------------
conobj = ms.connect(host="localhost", user="root", passwd="pass")
cursor = conobj.cursor()
try:
    st = "create database airlines"
    cursor.execute(st)
    conobj.commit()
except ms.DatabaseError:
    conobj.close()
try:
    conobj = ms.connect(host="localhost", user="root", passwd="pass", database="airlines")
    cursor = conobj.cursor()
    st = "create table passenger( id integer primary key, name varchar(100) not null, age integer, address varchar(200), mobile varchar(20), flightno varchar(20), flightname varchar(20), class varchar(20), seatno varchar(20), source varchar(20), destination varchar(20), fare integer , doj date)"
    cursor.execute(st)
    conobj.commit()
    conobj.close()
except ms.ProgrammingError:
    conobj.close()
welcome()
ADMIN()
print("Thank You")

import mysql.connector as sql
import mysql

    #### Defining Account_Open Functions ####

def open():
    try:
        
        nm = input("\tPlease Enter Cust Name      : ")
        bl = int(input("\tPlease Enter Initial Amount : "))
        g = input("\tCustomer Gender             : ")

        if bl<=500:
            while True:
                 print("\n\t\tMin Balance require Rs.500")
                 bl = int(input("\tAgain Enter Initial Amount  : "))
                 if bl>=500:
                     break
                   
        msql = "insert into bank_acc (name,bal,gender) values (%s,%s,%s)"
        l = [nm,bl,g]
        cur = mydb.cursor()
        cur.execute(msql,l)

        s = "select accno from bank_acc where name=%s"
        l1 = [nm]
        c = mydb.cursor()
        c.execute(s,l1)
        row = c.fetchone()
        if cur.rowcount == 1:
            print("\n\t======================================")
            print("\n\t\tAccount Opened Successfully..")
            print("\t\tAccount No is   : ",row[0])

        s1 = "insert into transaction (accno,txn, amt, avail_bal) values (%s,%s,%s,%s)"
        l2 = [row[0], 'D', bl, bl]
        c2 = mydb.cursor()
        c2.execute(s1,l2)
        
        mydb.commit()
        mydb.close()

    except Exception as e:
        print("\n\n\t\tFailed  to connect..",e)

    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        
    #### Defining Deposit_operation function ####

def deposit():
    try:
        an = int(input("\n\tPlease Enter A/c No to deposit  : "))
        amt = int(input("\tPlease Enter Amount             : "))

        msql = "update bank_acc set bal=bal+%s where accno=%s"
        l = [amt,an]
        cur = mydb.cursor()
        cur.execute(msql,l)

        m_row = "select bal from bank_acc where accno=%s"
        l2 = [an]
        c = mydb.cursor()
        c.execute(m_row,l2)
        row = c.fetchone()
        
        if cur.rowcount == 1:
            print("\n\t======================================")
            print("\n\t\tAmount deposited Successfully.")
            print("\tAvailable Balance is      : ","Rs.",row[0])
        else:
            print("\n\t\tAccount No not found..")

        s1 = "insert into transaction (accno, txn, amt,avail_bal ) values (%s,%s,%s,%s)"
        l2 = [an, 'D', amt, row[0]]
        c2 = mydb.cursor()
        c2.execute(s1,l2)

        mydb.commit()
        mydb.close()

    except Exception as e:
        print("\n\n\t\tFailed to connect..",e)

    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        
    ####  Defining Withdraw_operation function ####
            
def withdraw():
    try:
        an = int(input("\n\tPlease Enter A/c No to withdraw  : "))
        amt = int(input("\tPlease Enter Amount              : "))

        sql = "select bal from bank_acc where accno=%s"
        l=[an]
        c = mydb.cursor()
        c.execute(sql,l)
        row = c.fetchone()

        if row[0]-amt<500:
            print("\n\t-----------------------------------------")
            print("\n\t\tInsufficient Balance to withdraw..")

        else:
            msql = "update bank_acc set bal=bal-%s where accno=%s"
            l1 = [amt,an]
            cur = mydb.cursor()
            cur.execute(msql,l1)
            print("\n\t======================================")
            print("\n\t\tAmount Withdrawn Successfully.")
            print("\tAvailable Balance is      : ","Rs.",row[0]-amt)

        s1 = "insert into transaction (accno,txn, amt, avail_bal) values (%s,%s,%s,%s)"
        l2 = [an, 'W', amt, row[0]-amt]
        c2 = mydb.cursor()
        c2.execute(s1,l2)


        mydb.commit()
        mydb.close()

    except Exception as e:
        print("\n\n\t\tFailed to connect..",e)

    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        
    ####  Defining Balance_Enquiry function  ####

def enquiry():
    try:
        an = int(input("\n\tPlease Enter A/c No.        : "))

        sql = "select * from bank_acc where accno=%s"
        l = [an]

        cur = mydb.cursor()
        cur.execute(sql,l)
        rows = cur.fetchall()
        found=False
        for row in rows:
            print("\n\t---------------------------------------")
            print("\n\t\tAccount No.         : ",row[0])
            print("\t\tCustomer Name       : ",row[1])
            print("\t\tAvailable Balance   : ",row[2])
            print("\n\t---------------------------------------")
            found=True

        if found==False:
            print("\n\t\tAccount No",an,"does not exist..")

        mydb.close()

    except Exception as e:
        print("\n\n\t\tFailed to connect..",e)
        
    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#

        ##### Defining transaction function #####

def transaction():
    try:
        an = int(input("\n\tPlease Enter A/C No.       : "))
        sql = "select * from transaction where accno=%s order by dt"
        l1 = [an]
        c1 = mydb.cursor()
        c1.execute(sql,l1)
        rows = c1.fetchall()
        found=False
        print("\n\t----------------------------------------------")
        print("\n\t| AccNo |","Date ".ljust(18),"|"," TXN ","|","Amount".ljust(3),"|","Avail_bal".rjust(8),"|")
        for row in rows:
            
            an=row[0]; dt=row[1]; txn=row[2]; amt=row[3]; avail=row[4];
            print("\n\t|", an,  "|", dt,"|", str(txn).ljust(5) , "|", str(amt).ljust(5) ,"|",avail,"|")
            found=True

        if found==False:
            print("\n\t\tAccount No",an,"does not exist..")

        mydb.close()

    except Exception as e:
        print("\n\n\t\tFailed to connect..",e)
            

      
        
        
    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        
      
      ##### Defining service_request function #####



def service_request():
    try:
        an = int(input("\n\tPlease Enter A/c No.         : "))
        nm = input("\tPlease Enter New Name        : ")
        g = input("\tPlease Enter gender          : ")
        msql = "update bank_acc set name=%s,gender=%s where accno=%s"
        l = [nm,g,an]

        cur = mydb.cursor()
        cur.execute(msql,l)

        if cur.rowcount ==1:
            print("\n\t\tRecord updated..")
            print("\n\t-----------------------------------------")

        else:
            print("\n\t\tAccount No. does not exist..")
            print("\n\t-----------------------------------------")
    
        mydb.commit()
        mydb.close()

    except Exception as e:
        print("\n\t\tFailed to connect..",e)

    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        
    #### Defining all_acc function ####

def all_acc():
    try:
        msql = "select * from bank_acc"

        cur = mydb.cursor()
        cur.execute(msql)
        rows = cur.fetchall()

        for row in rows:
            print("\n\t\tAccount No.         : ",row[0])
            print("\t\tCustomer Name       : ",row[1])
            print("\t\tAvailable Balance   : ",row[2])
            print("\t\tGender              : ",row[3])
            print("\n\t---------------------------------------")

        mydb.close()

    except Exception as e:
        print("\n\t\tFailed to connect..",e)

    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        
    #### Defining close_acc function ####

def close_acc():
    try:
        an = int(input("\n\tPlease Enter A/c No.         : "))

        msql = "delete from bank_acc where accno=%s"
        l = [an]

        cur = mydb.cursor()
        cur.execute(msql,l)

        if cur.rowcount ==1:
            print("\n\t\tAccount closed successfully..")
            print("\n\t-------------------------------------------")

        else:
            print("\n\t\tAccount No does not exist..")
            print("\n\t-------------------------------------------")

        mydb.commit()
        mydb.close()
        
    except Exception as e:
        print("\n\t\tFailed to connect..",e)

    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        
      
    
while True:
    mydb = sql.connect(user="root", password="", database="bankdb")
    
    
    ## Menu Driven for user ##

    
    print("\n\t****************************************")
    print("\n\t\t01. Open Acccount")
    print("\t\t02. Deposit")
    print("\t\t03. Withdraw")
    print("\t\t04. Balance enquiry")
    print("\t\t05. Transaction Details")
    print("\t\t06. Service Request")
    print("\t\t07. All A/c holder list")
    print("\t\t08. Close Account")
    print("\t\t09. Exit")
    print("\n\t****************************************")
    ch = int(input("\n\t\tPlease Enter Your choice (1-8) : "))

    if ch ==1:
        open()

    elif ch ==2:
        deposit()

    elif ch == 3:
        withdraw()

    elif ch == 4:
        enquiry()

    elif ch == 5:
        transaction()

    elif ch == 6:
        service_request()

    elif ch == 7:
        all_acc()

    elif ch == 8:
        close_acc()

    elif ch == 9:
        quit()

    else:
        print("\n\t~~~~~~~~~~~~~~~~~INVALID-INPUT~~~~~~~~~~~~~~~~~~~")
        
        
    

    

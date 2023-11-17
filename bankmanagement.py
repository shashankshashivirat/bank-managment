import mysql.connector
mydb=mysql.connector(host='localhost',user='root',password=' ',database='bms')
def open_account():
	name=input("enter your name:")
	acc=input("enter your acc no:")
	dob=input("enter your dob:")
	add=input("enter your address:")
	con=input("enter your contract")
	op_bal=int(input("enter your opening balancxe:")

        data1=(name,acc,dob,add,con,op_bal)
        data2=(name,acc,op_bal)

        sql1=('insert into account value(%s,%s,%s,%s,%s,%s)')
        sql2=('insert amount value(%s,%s,%s)')

        x=mydb.cursor()
        x.execute(sql1,data1)
        x.execute(sql2,data2)

        mydb.commit()
        print("data entered successfully")
        main()

def deposit():
    amount=input("enter the amount to deposit:")
    acc=input("enter your acc_no:")
    a="select balance from amount where acc_no=%s
    data1=(acc,)
    x=mydb.cursor()
    x.execute(a,data1)
    result=x.fetchone()
    t=result[0]+amount
    sql=("update amount set balance where acc_no=%s")
    d=(t,acc)
    x.execute(sql,d)
    mydb.commit()
    print("______________")
    main()
def withdraw():
     amount=input("enter the amount to withdraw:")
    acc=input("enter your acc_no:")
    a="select balance from amount where acc_no=%s
    data1=(acc,)
    x=mydb.cursor()
    x.execute(a,data1)
    result=x.fetchone()
    t=result[0]-amount
    sql=("update amount set balance where acc_no=%s")
    d=(t,acc)
    x.execute(sql,d)
    mydb.commit()
    print("______________")
    main()
def balance():
    ac=

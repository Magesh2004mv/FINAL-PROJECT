import smtplib
import datetime
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="election"    
)
mycursor=mydb.cursor()
sql="insert into election_vote(idname,magesh,vignesh,yuvaraj,vishva,rishi) values (%s,%s,%s,%s,%s,%s)"
idname=input("enter the idname:")
magesh=1
vignesh=1
yuvaraj=1
vishva=1
rishi=1
val=(idname,magesh,vignesh,yuvaraj,vishva,rishi)
mycursor.execute(sql,val)
mydb.commit()
print('data accessed vote')
print("magesh---->1")
print("vignesh--->2")
print("yuvaraj--->3")
print("vishva---->4")
print("rishi----->5")
def canditate():
    try:
        id=input("enter the your voter id name:")
        vote=int(input("enter the vote in (1 to 5)number only:"))
        def magesh():
            try:
                magesh=1
                if vote=="1":
                    print("yes canditated")
                    print(id)
                    sql1="update election_vote set magesh"
                    voted1=magesh+1
                    val=voted1
                    print(val)
                    mycursor.execute(sql1,voted1)
                    mydb.commit()
                    print("thanks for voting")
                    dt=datetime.datetime.now()
                    send1=open("voting.txt","a")
                    send1.write(f"thanks for voting\ndatetime:{dt}")
                    def send_vote(email):
                        voting1= send1
                        print(f"Generated vote: {voting1}")
                        try: 
                            s = smtplib.SMTP("smtp.gmail.com", 587)
                            s.starttls()
                            s.login("---#your emailid---", "#---use your app password---")
                            subject = "Thanks for voting"
                            body = f"Your voted in india  {voting1}"
                            message = f"Subject: {subject}\n\n{body}"
                            s.sendmail("---your mailid---", email, message)
                            s.quit()
                            print("Email has been successfully sent!")
                        except Exception as e:
                            print(f"Failed to send email: {e}")
                    mail = input('Enter your email ID: ')
                    send_vote(mail)
                else:
                    print("errored")
            except:
                print("pls finding error")
        magesh()
        def vignesh():
            try:
                vignesh=1
                if vote=="2":
                    print("yes canditated")
                    print(id)
                    sql1="update election_vote set magesh"
                    voted2=vignesh+1
                    val=voted2
                    print(val)
                    mycursor.execute(sql1,voted2)
                    mydb.commit()
                    print("thanks for voting")
                    dt=datetime.datetime.now()
                    send1=open("voting.txt","a")
                    send1.write(f"thanks for voting\ndatetime:{dt}")
                    def send_vote(email):
                        voting1= send1
                        print(f"Generated vote: {voting1}")
                        try: 
                            s = smtplib.SMTP("smtp.gmail.com", 587)
                            s.starttls()
                            s.login("---#your emailid---", "#---use your app password---")
                            subject = "Thanks for voting"
                            body = f"Your voted in india  {voting1}"
                            message = f"Subject: {subject}\n\n{body}"
                            s.sendmail("---your mailid---", email, message)
                            s.quit()
                            print("Email has been successfully sent!")
                        except Exception as e:
                            print(f"Failed to send email: {e}")
                    mail = input('Enter your email ID: ')
                    send_vote(mail)
                else:
                    print("errored")
            except:
                print("pls finding error")
        vignesh()
        def yuvaraj():
            try:
                yuvaraj=1
                if vote=="3":
                    print("yes canditated")
                    print(id)
                    sql1="update election_vote set magesh"
                    voted3=yuvaraj+1
                    val=voted3
                    print(val)
                    mycursor.execute(sql1,voted3)
                    mydb.commit()
                    print("thanks for voting")
                    dt=datetime.datetime.now()
                    send1=open("voting.txt","a")
                    send1.write(f"thanks for voting\ndatetime:{dt}")
                    def send_vote(email):
                        voting1= send1
                        print(f"Generated vote: {voting1}")
                        try: 
                            s = smtplib.SMTP("smtp.gmail.com", 587)
                            s.starttls()
                            s.login("---#your emailid---", "#---use your app password---")
                            subject = "Thanks for voting"
                            body = f"Your voted in india  {voting1}"
                            message = f"Subject: {subject}\n\n{body}"
                            s.sendmail("---your mailid---", email, message)
                            s.quit()
                            print("Email has been successfully sent!")
                        except Exception as e:
                            print(f"Failed to send email: {e}")
                    mail = input('Enter your email ID: ')
                    send_vote(mail)
                else:
                    print("errored")
            except:
                print("pls finding error")
        yuvaraj()
        def vishva():
            try:
                vishva=1
                if vote=="4":
                    print("yes canditated")
                    print(id)
                    sql1="update election_vote set magesh"
                    voted4=vishva+1
                    val=voted4
                    print(val)
                    mycursor.execute(sql1,voted4)
                    mydb.commit()
                    print("thanks for voting")
                    dt=datetime.datetime.now()
                    send1=open("voting.txt","a")
                    send1.write(f"thanks for voting\ndatetime:{dt}")
                    def send_vote(email):
                        voting1= send1
                        print(f"Generated vote: {voting1}")
                        try: 
                            s = smtplib.SMTP("smtp.gmail.com", 587)
                            s.starttls()
                            s.login("---#your emailid---", "#---use your app password---")
                            subject = "Thanks for voting"
                            body = f"Your voted in india  {voting1}"
                            message = f"Subject: {subject}\n\n{body}"
                            s.sendmail("---your mailid---", email, message)
                            s.quit()
                            print("Email has been successfully sent!")
                        except Exception as e:
                            print(f"Failed to send email: {e}")
                    mail = input('Enter your email ID: ')
                    send_vote(mail)
                else:
                    print("errored")
            except:
                print("pls finding error")
        vishva()
        def rishi():
            try:
                rishi=1
                if vote=="5":
                    print("yes canditated")
                    print(id)
                    sql1="update election_vote set magesh"
                    voted5=rishi+1
                    val=voted5
                    print(val)
                    mycursor.execute(sql1,voted5)
                    mydb.commit()
                    print("thanks for voting")
                    dt=datetime.datetime.now()
                    send1=open("voting.txt","a")
                    send1.write(f"thanks for voting\ndatetime:{dt}")
                    def send_vote(email):
                        voting1= send1
                        print(f"Generated vote: {voting1}")
                        try: 
                            s = smtplib.SMTP("smtp.gmail.com", 587)
                            s.starttls()
                            s.login("---#your emailid---", "#---use your app password---")
                            subject = "Thanks for voting"
                            body = f"Your voted in india  {voting1}"
                            message = f"Subject: {subject}\n\n{body}"
                            s.sendmail("---your mailid---", email, message)
                            s.quit()
                            print("Email has been successfully sent!")
                        except Exception as e:
                            print(f"Failed to send email: {e}")
                    mail = input('Enter your email ID: ')
                    send_vote(mail)
                else:
                    print("errored")
            except:
                print("pls finding error")
        rishi()
    except NameError:
        print("pls id name only")
canditate()    
    
                
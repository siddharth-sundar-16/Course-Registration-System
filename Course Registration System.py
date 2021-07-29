import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", passwd="sahana23g", database="customer")

mycursor = mydb.cursor()

temp=False
temp2=False
temp3=True
student='student'
faculty='faculty'
major1='Computer Science'
major2='Sports'
major3='Arts'

def student_registration():
    name=input("Enter your name!")
    roll_no=18500
    major=input("Enter your major!")
    dob=input("Enter your date of birth!")
    gender=input("Enter your gender")
    email=input("Enter your email!")
    contact=input("Enter your contact number")
    marks=input("Enter your marks")
    if(major==major1):
        check3=mycursor.execute("select coursename from course where courseid=1504 or courseid=1505")
        res3=mycursor.fetchall()
        print("Courses available for you are :")
        for i in res3:
            print(i)
        course=input("Enter your course!")
        check4=mycursor.execute("select vacancy from course where coursename=%s",(course ,))
        res4=mycursor.fetchall()
        for i in res4:
            if i[0]>=1:
                check5=mycursor.execute("update course set vacancy=vacancy-1 where coursename=%s",(course ,))
                check6=mycursor.execute("""insert into student(username,name,role,major,dob,gender,email,contact,overall_marks)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user_name , name , role , course , dob , gender , email , contact , marks))
                mydb.commit()
                print("Course Registration was successful!")
            else:
                print("Course cannot be registered")
    elif(major==major2):
        check7=mycursor.execute("select coursename from course where courseid=1606 or courseid=1607")
        res5=mycursor.fetchall()
        print("Courses available for you are :")
        for i in res5:
            print(i)
        course=input("Enter any course!")
        check8=mycursor.execute("select vacancy from course where coursename=%s",(course ,))
        res6=mycursor.fetchall()
        for i in res6:
            if i[0]>=1:
                check9=mycursor.execute("update course set vacancy=vacancy-1 where coursename=%s",(course ,))
                check10=mycursor.execute("""insert into student(username,name,role,major,dob,gender,email,contact,overall_marks)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user_name , name , role , course , dob , gender , email , contact , marks))
                mydb.commit()
                print("Course Registration was successful!")
            else:
                print("Course cannot be registered!")
    elif(major==major3):
        check11=mycursor.execute("select coursename from course where courseid=1708 or courseid=1709")
        res7=mycursor.fetchall()
        print("Courses available for you are :")
        for i in res7:
            print(i)
        course=input("Enter any course!")
        check12=mycursor.execute("select vacancy from course where coursename=%s",(course ,))
        res8=mycursor.fetchall()
        for i in res8:
            if i[0]>=1:
                check13=mycursor.execute("update course set vacancy=vacancy-1 where coursename=%s",(course ,))
                check14=mycursor.execute("""insert into student(username,name,role,major,dob,gender,email,contact,overall_marks)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user_name , name , role , course , dob , gender , email , contact , marks))
                mydb.commit()
                print("Course Registration is successful!")
            else:
                print("Course cannot be registered!")


user_name=input("Enter the username!")
check=mycursor.execute("select username from data where username=%s",(user_name ,))
res=mycursor.fetchall()
for i in res:
    if user_name in i:
        temp=True

if(temp):
    print("Entered username is correct!")
    pass_word=input("Enter your password!")
    check2=mycursor.execute("select password from data where username=%s",(user_name ,))
    res2=mycursor.fetchall()
    for j in res2:
        if pass_word in j:
            temp2=True

    if(temp2):
        role=input("Enter your role!")
        print("Login Successful!")
        if(role==student):
            student_registration()


    else:
        for i in range(0,3):
            print("Entered password is incorrect!")
            pass_word=input("Enter the password again!")
            check15=mycursor.execute("select password from data where username=%s",(user_name ,))
            res9=mycursor.fetchall()
            for j in res9:
                if pass_word in j:
                    temp2=True
            if(temp2):
                break
        if(temp2):
            print("Login was Successful!")
            role=input("Enter your role!")
            student_registration()
        else:
            print("Access has been denied!")

else:
    print("Your username does not exist!")
    while(7):
            x=1
            new_user=input("Enter your new username!")
            check22=mycursor.execute("select username from data where username=%s",(new_user ,))
            res10=mycursor.fetchall()
            for j in res10:
                if new_user in j:
                    print("Username already exists")
                    print("Retry")
                    x=0
                else:
                    x=1
                    break
            if(x==1):
                break
    new_password=input("Enter your password!")
    role=input("Enter your role!")
    check16=mycursor.execute("insert into data(username,password,role)values(%s,%s,%s)",(new_user, new_password, role))
    mydb.commit()
    if(role==student):
        student_registration()

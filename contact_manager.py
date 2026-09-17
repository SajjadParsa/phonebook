#mariadb اسم سرور یا همون cmd کامپیوتر ما هست که در اینجا برای اینکه cmd رو با پایتون وصل کنیم باید واردش کنیم
import mariadb

def person():
    contact=cursor.fetchone()
    
    print("--------------------------------")
    print(f"ID: {contact[0]}")
    print(f"Name: {contact[1]}")
    print(f"Phone: {contact[2]}")
    print(f"Adress: {contact[3]}")
    print(f"Gamil: {contact[4]}")
    print("--------------------------------")
def all_person():
    cursor.execute("select *from contacts")
    #cursor.fetchall means that take every value that returns from database and put it into contacts.
    contacts=cursor.fetchall()
    if contacts:
        for i in contacts:
            print("-----------------------------------")
            print(f"ID: {i[0]}")
            print(f"Name: {i[1]}")
            print(f"Phone: {i[2]}")
            print(f"Adress: {i[3]}")
            print(f"Gmail: {i[4]}")
            print("----------------------------------")
    else:
        print("There is NO contact✖")
        return
    


try:
    #con is just a variable it can be connection or sth else..
    con = mariadb.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="phonebook"
    )
    print("Connected successfully!")
    #we create a pointer to use it as a connector
    cursor = con.cursor()
    
    print(f"{'Phonebook':_^50}")
    print("")
    while True:
        #main MENU
        print("""

        1. Add contact
        2. Show contacts
        3. search contact
        4. update contact
        5. delete contact
        6. Exit


            """)
        #user have to insert numbers not anything else.
        try:
            user_choose=int(input("Please choose one action from top:   "))
        except ValueError:
            print("Please choose a valid number! ")
            continue
        #if user want to add a new contact into database
        if user_choose==1:
            name=input("Enter name:  ")
            phone=input("Enter phone number:  ")
            adress=input("Enter Adress:  ")
            gmail=input("Enter gmail:  ")
           #database action
           #by this sql codes we can insert the data into database table that named contacts
            sql= """ 
                insert into contacts(name,phone,adress,gmail) values(?,?,?,?)
            
            """
           #fromwhere we connected database with python we first execute the sql action part and then we give the values to sql
            cursor.execute(sql,(name,phone,adress,gmail))
            #save the changes to database
            con.commit()

            print("Contact added successfully✅")
        #if user want to see all contacts
        elif user_choose==2:
           all_person()
        #if user wants to search a speacific contact form database by searching the contact name
        elif user_choose==3:
            user_sch_name=input("Enter the contact name:  ")
            # ? it means that it is empty or not specified yet
            sql="""
                select *from contacts where name=?
                    """
            #user_sch_name, means that it is a tuple not just a simple given value
            cursor.execute(sql,(user_sch_name,))
            person()
        #update menu
        elif user_choose==4:
            print(f"{'Update contact':^50}")

            all_person()

            try:
                user_upd=int(input("Please enter the contact ID:  "))
            except ValueError:
                print("Please enter a valid ID number❗")
                continue
            cursor.execute("select *from contacts where id=?",(user_upd,))
            contact=cursor.fetchall()
            if contact:
                print("Contact Found✅")
                while True:
                    print("""

                    1. Update name
                    2. Update name and phone number
                    3. Update Adress and Gmail
                    4. Update All
                    5. Back

                        """)
                    try:
                        user_upd_choose=int(input("Please choose one action from top🔼  "))
                    except ValueError:
                        print("Please enter from number from given list❗")
                        continue
                    #update name
                    if user_upd_choose==1:
                        new_name=input("Enter new name: ")
                        cursor.execute("update contacts set name=? where id=?",(new_name,user_upd))
                        cursor.execute("select *from contacts where id=?",(user_upd,))
                        person()
                            
                        con.commit()
                       
                        print("Name updated successfully✅")
                    #update name and phone number
                    elif user_upd_choose==2:
                        new_name=input("Enter new name:  ")
                        new_phone=input("Enter new phone number:  ")
                            
                        cursor.execute("update contacts set name=?,phone=? where id=?",(new_name,new_phone,user_upd))
                        cursor.execute("select *from contacts where id=?",(user_upd,))
                        person()
                        con.commit()
                        print("New name and phone updated✅")
                    #update Adress and gmail
                    elif user_upd_choose==3:
                        new_addres=input("Enter the new Addres: ")
                        new_gmail=input("Enter the new gmail: ")

                        cursor.execute("update contacts set adress=?,gmail=? where id=?",(new_addres,new_gmail,user_upd))
                        cursor.execute("select *from contacts where id=?",(user_upd,))
                        person()
                        con.commit()
                        print("New adress and gmail has been updatet✅")
                    #update all
                    elif user_upd_choose==4:
                        new_name=input("Enter New name: ")
                        new_phone=input("Enter new phone number: ")
                        new_addres=input("Enter new Adress: ")
                        new_gmail=input("Enter new Gmail: ")

                        cursor.execute("update contacts set name=?,phone=?,adress=?,gmail=? where id=?",(new_name,new_phone,new_addres,new_gmail,user_upd))
                        cursor.execute("select *from contacts where id=?",(user_upd,))
                        person()
                        con.commit()
                    elif user_upd_choose==5:
                        print("Back to main page...")
                        break   
            else:
                print("Contact Not found❌")
                continue
            

        #delete one contact or all contacts
        elif user_choose==5:
            print(f"{'Delete contact menu':^50}")
            print("")
            all_person()
            
            while True:
                print("""

                1. Delete a contact 
                2. Delete all contact
                3. Back

                """)
                try:
                    user_del=int(input("Please choose one action:  "))
                except ValueError:
                    print("Please choose a valid number! ")
                    continue
                if user_del==1:
                    try:
                        user_del_one=int(input("Please enter the contact ID:  "))
                    except ValueError:
                        print("please enter just integers not anything else!")
                        continue
                    cursor.execute("delete from contacts where id=?",(user_del_one,))
                    con.commit()
                    print("Contact deleted successfully✅🚮")
                elif user_del==2:
                    print("""

                    Are you sure want to clear all the contacts from database?
                    1. YES
                    2. NO

                    """)
                    try:
                        user_del_all=int(input("please choose one action:  "))
                    except ValueError:
                        print("Please choose a valid number!")
                        continue
                    if user_del_all==1:
                        cursor.execute("truncate table contacts")
                        con.commit()
                        print("All contacts deleted successfully!")
                    elif user_del_all==2:
                        print("back to main page... ")
                        break
                elif user_del==3:
                    break
                else:
                    print("Please just choose action from the given menu!! ")
                    continue
        #exit from programm
        elif user_choose==6:
            print("Bye!")
            break
        else:
            print("Please enter a valid number❗❗")
    con.close()
except mariadb.Error as e:
    print("Connection failed",e)




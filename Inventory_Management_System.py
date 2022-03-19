import os
import time
import sqlite3


def connection(Database_Name):
    connection_object = sqlite3.connect(f"C:\\{Database_Name}.db")
    return connection_object


def createTable():
    try:
        cursor.execute('''
        CREATE TABLE USERDATA (
    		userName varchar(30),
    		password varchar(30),
            securityQusetionA varchar(40),
            securityQusetionB varchar(40)
    		);
        ''')
        conn.commit()
    except sqlite3.OperationalError:
        pass


def createTableForUser():
    try:
        cursor.execute(f'''
        CREATE TABLE {USER}CUSTOMERTABLE (
    		customerId varchar(30),
    		customerName varchar(30),
    		customerNumber varchar(10)
    		);
        ''')
        conn.commit()
    except sqlite3.OperationalError:
        pass
    try:
        cursor.execute(f'''
        CREATE TABLE {USER}PRODUCTTABLE (
    	productId varchar(30),
    	productName varchar(30),
        productQuantity varchar(30)
    	);
        ''')
        conn.commit()
    except sqlite3.OperationalError:
        pass
    try:
        cursor.execute(f'''
        CREATE TABLE {USER}SUPPLIERTABLE (
    	supplierId varchar(30),
    	supplierName varchar(30),
    	supplierNumber varchar(10)
    	);
        ''')
        conn.commit()
    except sqlite3.OperationalError:
        pass


def cleanScreen(a):
    if (a == 1):
        temp = input("\n\nPress enter key to Continue ..........")
        time.sleep(0.1)
        os.system('cls')
    elif (a == 2):
        time.sleep(0.1)
        os.system('cls')


def welcomeOrEndScreen(a):
    if a == 1:
        os.system('cls')
        for i in welcomeSciptList:
            time.sleep(1)
            print(i, flush=True)
        time.sleep(3)
        cleanScreen(2)
        mainMenu()
    elif a == 2:
        os.system('cls')
        for i in endSciptList:
            time.sleep(1)
            print(i, flush=True)
        time.sleep(3)
        cleanScreen(2)


def loginMenu():
    print("*"*70)
    print("1 : Login To User Account")
    print("2 : Create New User Account")
    print("3 : Change User Account Password")
    print("4 : Forgot User Account Password")
    print("5 : Exit")
    print("*"*70)
    choice = (input("Enter the choice (Numeric):"))
    choice_int = choice.isdigit()
    if choice_int == True:
        choice = int(choice)
        if choice == 1:
            cleanScreen(1)
            loginToAccount()
        elif choice == 2:
            cleanScreen(1)
            createAccount()
        elif choice == 3:
            cleanScreen(1)
            changePassword()
        elif choice == 4:
            cleanScreen(1)
            forgotPassword()
        elif choice == 5:
            cleanScreen(1)
            welcomeOrEndScreen(2)
            exit()
        else:
            print("You enter an invalid input. Please, enter a valid input.")
            cleanScreen(1)
            loginMenu()
    else:
        print("You enter an invalid input. Please, enter a valid input.")
        cleanScreen(1)
        loginMenu()


def mainMenu():
    print("*"*70)
    print("1 : Input Data")
    print("2 : Print Data")
    print("3 : Update data")
    print("4 : Delete Data")
    print("5 : Logout")
    print("*"*70)
    choice = (input("Enter the choice (Numeric):"))
    choice_int = choice.isdigit()
    if choice_int == True:
        choice = int(choice)
        if choice == 1:
            cleanScreen(1)
            inputDataMenu()
        elif choice == 2:
            cleanScreen(1)
            printDataMenu()
        elif choice == 3:
            cleanScreen(1)
            updateDataMenu()
        elif choice == 4:
            cleanScreen(1)
            deleteDataMenu()
        elif choice == 5:
            cleanScreen(1)
            print("Logging Out .....")
            time.sleep(1)
            cleanScreen(2)
            loginMenu()
        else:
            print("You enter an invalid input. Please, enter a valid input.")
            cleanScreen(1)
            mainMenu()
    else:
        print("You enter an invalid input. Please, enter a valid input.")
        cleanScreen(1)
        mainMenu()


def inputDataMenu():
    print("*"*70)
    print("1 : Input Supplier detail ")
    print("2 : Input Customer detail")
    print("3 : Input Product detail")
    print("4 : Go to the previous menu")
    print("*"*70)
    choice = input("Enter the choice (Numeric):")
    choice_int = choice.isdigit()
    if choice_int == True:
        choice = int(choice)
        if choice == 1:
            cleanScreen(1)
            addSupplierDetail()
        elif choice == 2:
            cleanScreen(1)
            addCustomerDetail()
        elif choice == 3:
            cleanScreen(1)
            addProductDetail()
        elif choice == 4:
            cleanScreen(1)
            mainMenu()
        else:
            print("You enter an invalid input. Please, enter a valid input.")
            cleanScreen(1)
            inputDataMenu()
    else:
        print("You enter an invalid input. Please, enter a valid input.")
        cleanScreen(1)
        inputDataMenu()


def printDataMenu():
    print("*"*70)
    print("1 : Print Supplier Details")
    print("2 : Print Customer Details")
    print("3 : Print Product Details")
    print("4 : Go to previous menu")
    print("*"*70)
    choice = input("Enter the choice (Numeric):")
    choice_int = choice.isdigit()
    if choice_int == True:
        choice = int(choice)
        if choice == 1:
            cleanScreen(1)
            printSupplierDetails()
        elif choice == 2:
            cleanScreen(1)
            printCustomerDetails()
        elif choice == 3:
            cleanScreen(1)
            printProductDetails()
        elif choice == 4:
            cleanScreen(1)
            mainMenu()
        else:
            print("You enter an invalid input. Please, enter a valid input.")
            cleanScreen(1)
            printDataMenu()
    else:
        print("You enter an invalid input. Please, enter a valid input.")
        cleanScreen(1)
        printDataMenu()


def updateDataMenu():
    print("*"*70)
    print("1 : Update Supplier detail")
    print("2 : Update Customer detail")
    print("3 : Update Product detail")
    print("4 : Go to previous menu")
    print("*"*70)
    choice = input("Enter the choice (Numeric):")
    choice_int = choice.isdigit()
    if choice_int == True:
        choice = int(choice)
        if choice == 1:
            cleanScreen(1)
            updateDetails(1)
        elif choice == 2:
            cleanScreen(1)
            updateDetails(2)
        elif choice == 3:
            cleanScreen(1)
            updateDetails(3)
        elif choice == 4:
            cleanScreen(1)
            mainMenu()
        else:
            print("You enter an invalid input. Please, enter a valid input.")
            cleanScreen(1)
            updateDataMenu()
    else:
        print("You enter an invalid input. Please, enter a valid input.")
        cleanScreen(1)
        updateDataMenu()


def deleteDataMenu():
    print("*"*70)
    print("1 : Delete Supplier detail")
    print("2 : Delete Customer detail")
    print("3 : Delete Product detail")
    print("4 : Go to previous menu")
    print("*"*70)
    choice = input("Enter the choice (Numeric):")
    choice_int = choice.isdigit()
    if choice_int == True:
        choice = int(choice)
        if choice == 1:
            cleanScreen(1)
            deleteDetails(1)
        elif choice == 2:
            cleanScreen(1)
            deleteDetails(2)
        elif choice == 3:
            cleanScreen(1)
            deleteDetails(3)
        elif choice == 4:
            cleanScreen(1)
            mainMenu()
        else:
            print("You enter an invalid input. Please, enter a valid input.")
            cleanScreen(1)
            deleteDataMenu()
    else:
        print("You enter an invalid input. Please, enter a valid input.")
        cleanScreen(1)
        deleteDataMenu()


def loginToAccount():
    global USER
    userNameList = []
    userPasswordList = []
    cursor.execute('''
    SELECT * FROM USERDATA;
    ''')
    fetachData = cursor.fetchall()
    for i in fetachData:
        userNameList.append(i[0])
        userPasswordList.append(i[1])
    userName = input("Enter Your User Name :")
    for i in range(0, len(userNameList)):
        if (userName == userNameList[i]):
            temp = 1
            while(temp < 4):
                userPassword = input("Enter Your Password :")
                if (userPassword == userPasswordList[i]):
                    cleanScreen(2)
                    USER = userName
                    print("Login successfully .....")
                    time.sleep(1)
                    createTableForUser()
                    cleanScreen(2)
                    welcomeOrEndScreen(1)
                    mainMenu()
                else:
                    print("Password not match !!!!!")
                temp += 1
            else:
                print("Maximum limit to login exceeded !!!!!")
                cleanScreen(1)
                loginMenu()
            break
    else:
        print("User Id Not Found !!!!!")
        cleanScreen(1)
        loginMenu()


def createAccount():
    global USER
    userNameList = []
    cursor.execute('''
    SELECT * FROM USERDATA;
    ''')
    fetchData = cursor.fetchall()
    for i in fetchData:
        userNameList.append(i[0])
    print("Your ID must contain some Alphabet (UPPERCASE) and Number(Optional).\nSpecial symbol(Except '_' Underscore) and Spaces are not allowed")
    print("\nFor Ex: Correct method: ABC123 , ABCD , ABC_123 etc.\n        Incorrect method: 1234 , Abc123 , abC123 , 123456 , AB-123 ,12ABC12, AB 123.\n")
    userName = input("Enter New User Name :")
    punctuation = ["!", "#", "$", "%", "&", "\\", "'", '"',
                   "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "`", "{", "|", "}", "~"]
    for i in userName:
        for j in punctuation:
            if i == j:
                print("You enter a special symbol which is not allowwed.")
                print("Account creation cancelled ......")
                cleanScreen(1)
                loginMenu()
    for i in userName:
        if i.isspace() == True:
            print("You enter a space which is not allowwed.")
            print("Account creation cancelled ......")
            cleanScreen(1)
            loginMenu()
    dig = userName.isdigit()
    upper = userName.isupper()
    if(dig == False and upper == True and userName[0].isdigit() == False and len(userName) != 0):
        count = userNameList.count(userName)
        if(count == 0):
            userPass1 = input("Enter Your Password :")
            temp = 1
            while(temp < 4):
                userPass2 = input("Renter Your Password :")
                if (userPass2 == userPass1):
                    print("\nSecurity Questions ")
                    securityQuestionA = input(
                        "What is your favourite teacher name :")
                    securityQuestionB = input(
                        "What is your favourite mobile company name :")
                    cursor.execute('''
                    INSERT INTO USERDATA 
                    VALUES(?,?,?,?);
                    ''', (userName, userPass2, securityQuestionA, securityQuestionB))
                    conn.commit()
                    USER = userName
                    createTableForUser()
                    cleanScreen(2)
                    print("Account created .....")
                    time.sleep(1)
                    cleanScreen(2)
                    print("Logging to account .....")
                    time.sleep(2)
                    cleanScreen(2)
                    welcomeOrEndScreen(1)
                    mainMenu()
                else:
                    print("Rentered Password Not Match !!!!!")
                temp += 1
            else:
                print("Entering limit exceeded !!!!!")
                cleanScreen(1)
                loginMenu()
        else:
            print("This Id Already Exist !!!!!")
            cleanScreen(1)
            loginMenu()
    elif(userName[0].isdigit() == True):
        print("Please enter a combination of alphabet(Uppercase) and number,\nId should not start with numeric value.")
        print("Account creation cancelled ......")
        cleanScreen(1)
        loginMenu()
    elif(dig == True):
        print("Please enter a combination of alphabet(Uppercase) and number,Only Number not allowed.")
        print("Account creation cancelled ......")
        cleanScreen(1)
        loginMenu()
    elif(len(userName) == 0):
        print("Please enter a combination of alphabet(Uppercase) and number,\nYou doesn't enter anything which is not allowed.")
        print("Account creation cancelled ......")
        cleanScreen(1)
        loginMenu()
    else:
        print("Please enter a combination of alphabet(Uppercase) and number,\nYou enter a invalid username.")
        print("Account creation cancelled ......")
        cleanScreen(1)
        loginMenu()


def changePassword():
    userNameList = []
    userPasswordList = []
    cursor.execute('''
    SELECT * FROM USERDATA;
    ''')
    fetchData = cursor.fetchall()
    for i in fetchData:
        userNameList.append(i[0])
        userPasswordList.append(i[1])
    userName = input("Enter Your User Id :")
    for i in range(0, len(userNameList)):
        if (userName == userNameList[i]):
            te = 1
            while(te < 4):
                userPass1 = input("Enter Your Password :")
                if (userPass1 == userPasswordList[i]):
                    tem = 1
                    while(tem < 4):
                        userPass2 = input("Enter Your New Password :")
                        temp = 1
                        while(temp < 4):
                            userPass3 = input("Renter Your New Password :")
                            if (userPass2 == userPass3):
                                cursor.execute(f'''
                                UPDATE USERDATA
                                SET password = ?
                                WHERE userName =?;
                                ''', (userPass3, userName))
                                conn.commit()
                                print("Password change succesfully .....")
                                cleanScreen(1)
                                loginMenu()
                            else:
                                print("Rentered Password not match !!!!!")
                            temp += 1
                        else:
                            print("Entering limit exceeded !!!!!")
                            cleanScreen(1)
                            loginMenu()
                    else:
                        print("Password not match !!!!!")
                    tem += 1
                else:
                    print("Password not Match !!!!!")
                te += 1
            else:
                print("Entering limit exceeded !!!!!")
                cleanScreen(1)
                loginMenu()
            break
    else:
        print("Id not found !!!!!")
        cleanScreen(1)
        loginMenu()


def forgotPassword():
    userNameList = []
    securityQuestionAList = []
    securityQuestionBList = []
    cursor.execute('''
    SELECT * FROM USERDATA;
    ''')
    fetchData = cursor.fetchall()
    for i in fetchData:
        userNameList.append(i[0])
        securityQuestionAList.append(i[2])
        securityQuestionBList.append(i[3])
    userName = input("Enter Your User Id :")
    for i in range(0, len(userNameList)):
        if (userName == userNameList[i]):
            print("Security Questions ")
            temp = 1
            while(temp < 4):
                securityQuestionA = input(
                    "What is your favourite teacher name name :")
                if(securityQuestionA == securityQuestionAList[i]):
                    tem = 1
                    while(tem < 4):
                        securityQuestionB = input(
                            "What is your favourite mobile company name :")
                        if(securityQuestionB == securityQuestionBList[i]):
                            userPass = input("Enter New Password :")
                            te = 1
                            while(te < 4):
                                userPass2 = input("Renter New Password :")
                                if(userPass == userPass2):
                                    cursor.execute(f'''
                                    UPDATE USERDATA
                                    SET password = ?
                                    WHERE userName =?;
                                    ''', (userPass2, userName))
                                    conn.commit()
                                    print("Password change succesfully .....")
                                    cleanScreen(1)
                                    loginMenu()
                                else:
                                    print("Rentered Password Not Match !!!!!")
                                te += 1
                            else:
                                print(
                                    "Entering limit exceeded!!!!!\nPassword not change !!!!!")
                                cleanScreen(1)
                                loginMenu()
                        else:
                            print("Your answer is incorrect !!!!!")
                        tem += 1
                    else:
                        print("Entering limit exceeded !!!!!")
                        cleanScreen(1)
                        loginMenu()
                else:
                    print("Your answer is incorrect")
                temp += 1
            else:
                print("Entering limit exceeded !!!!!")
                cleanScreen(1)
                loginMenu()
            break
    else:
        print("Id not found !!!!!")
        cleanScreen(1)
        loginMenu()


def deleteDetails(a):
    idList = []
    if a == 1:
        cursor.execute(f'''
            SELECT supplierId FROM {USER}SUPPLIERTABLE;
            ''')
    elif a == 2:
        cursor.execute(f'''
            SELECT customerId FROM {USER}CUSTOMERTABLE;
            ''')
    elif a == 3:
        cursor.execute(f'''
            SELECT productId FROM {USER}PRODUCTTABLE;
            ''')
    allIdList = cursor.fetchall()
    for element in allIdList:
        idList.append(element[0])
    if a == 1:
        supplierId = input(
            "Enter the ID of supplier whose details you want to delete :")
        check = idList.count(supplierId)
        if check != 0:
            cursor.execute(f'''
            SELECT supplierName FROM {USER}SUPPLIERTABLE 
            WHERE supplierId =?;
            ''', (supplierId,))
            supplierName = cursor.fetchall()
            print(
                f"\nYou really want to delete detail of Supplier Name :{supplierName[0][0]}")
            print("If 'Yes' Enter Yes or y ,Else 'NO' Enter No or n")
            yOrN = input("Enter your choice :")
            no = ["NO" == yOrN, "No" == yOrN, "no" ==
                  yOrN, "N" == yOrN, "n" == yOrN]
            yes = ["YES" == yOrN, "Yes" == yOrN,
                   "yes" == yOrN, "Y" == yOrN, "y" == yOrN]
            if any(yes):
                cursor.execute(f'''
                DELETE FROM {USER}SUPPLIERTABLE
                WHERE supplierId =?;
                ''', (supplierId,))
                conn.commit()
                print("Detalis Deleted Succesfully .....")
            elif any(no):
                print("Deletation Canceled .....")
            else:
                print("\nYou enter an invalid choice")
                print("Deletation Canceled .....")
            cleanScreen(1)
            deleteDataMenu()
        elif check == 0:
            print("Entered customer ID doesn't exists")
            cleanScreen(1)
            deleteDataMenu()
    elif a == 2:
        customerId = input(
            "Enter the ID of customer whose details you want to delete :")
        check = idList.count(customerId)
        if check != 0:
            cursor.execute(f'''
            SELECT customerName FROM {USER}CUSTOMERTABLE 
            WHERE customerId =?;
            ''', (customerId,))
            customerName = cursor.fetchall()
            print(
                f"\nYou really went to delete detail of Customer Name:{customerName[0][0]}")
            print("If 'Yes' Enter Yes or y ,Else 'NO' Enter No or n")
            yOrN = input("Enter your choice :")
            no = ["NO" == yOrN, "No" == yOrN, "no" ==
                  yOrN, "N" == yOrN, "n" == yOrN]
            yes = ["YES" == yOrN, "Yes" == yOrN,
                   "yes" == yOrN, "Y" == yOrN, "y" == yOrN]
            if any(yes):
                cursor.execute(f'''
                DELETE FROM {USER}CUSTOMERTABLE
                WHERE customerId =?;
                ''', (customerId,))
                conn.commit()
                print("Detalis Deleted Succesfully .....")
            elif any(no):
                print("Deletation Canceled .....")
            else:
                print("\nYou enter an invalid choice")
                print("Deletation Canceled .....")
            cleanScreen(1)
            deleteDataMenu()
        elif check == 0:
            print("Entered customer ID doesn't exists")
            cleanScreen(1)
            deleteDataMenu()
    elif a == 3:
        productId = input(
            "Enter the ID of product whose details you want to delete :")
        check = idList.count(productId)
        if check != 0:
            cursor.execute(f'''
            SELECT productName FROM {USER}PRODUCTTABLE 
            WHERE productId =?;
            ''', (productId,))
            productName = cursor.fetchall()
            print(
                f"\nYou really went to delete detail of Product Name :{productName[0][0]}")
            print("If 'Yes' Enter Yes or y ,Else 'NO' Enter No or n")
            yOrN = input("Enter your choice :")
            no = ["NO" == yOrN, "No" == yOrN, "no" ==
                  yOrN, "N" == yOrN, "n" == yOrN]
            yes = ["YES" == yOrN, "Yes" == yOrN,
                   "yes" == yOrN, "Y" == yOrN, "y" == yOrN]
            if any(yes):
                cursor.execute(f'''
                DELETE FROM {USER}PRODUCTTABLE
                WHERE productId =?;
                ''', (productId,))
                conn.commit()
                print("Detalis Deleted Succesfully .....")
            elif any(no):
                print("Deletation Canceled .....")
            else:
                print("\nYou enter an invalid choice")
                print("Deletation Canceled .....")
            cleanScreen(1)
            deleteDataMenu()
        elif check == 0:
            print("Entered customer ID doesn't exists")
            cleanScreen(1)
            deleteDataMenu()


def updateDetails(a):
    idList = []
    if a == 1:
        cursor.execute(f'''
            SELECT supplierId FROM {USER}SUPPLIERTABLE;
            ''')
    elif a == 2:
        cursor.execute(f'''
            SELECT customerId FROM {USER}CUSTOMERTABLE;
            ''')
    elif a == 3:
        cursor.execute(f'''
            SELECT productId FROM {USER}PRODUCTTABLE;
            ''')
    allIdList = cursor.fetchall()
    for element in allIdList:
        idList.append(element[0])
    if a == 1:
        supplierId = input(
            "Enter the ID of supplier whose details you want to update :")
        check = idList.count(supplierId)
        if check != 0:
            cursor.execute(f'''
            SELECT supplierName ,supplierNumber FROM {USER}SUPPLIERTABLE
            WHERE supplierId =?;
            ''', (supplierId,))
            supplierDeatil = cursor.fetchall()
            print(
                f"\nPresent details of supplier :\nName : {supplierDeatil[0][0]}\nContact Number: {supplierDeatil[0][1]}")
            print("\nEnter New Supplier details :-")
            supplierName = input("Enter the Supplier name :")
            phoneNoVerification(1)
            cursor.execute(f'''
            UPDATE {USER}SUPPLIERTABLE
            SET supplierName = ?, supplierNumber = ?
            WHERE supplierId =?;
            ''', (supplierName, supplierNumber, supplierId))
            conn.commit()
            print("Details Updated Succesfully ....")
            cleanScreen(1)
            updateDataMenu()
        elif(check == 0):
            print("Entered Supplier ID doesn't exists")
            cleanScreen(1)
            updateDataMenu()
    elif a == 2:
        customerId = input(
            "Enter the ID of customer whose details you want to update :")
        check = idList.count(customerId)
        if check != 0:
            cursor.execute(f'''
            SELECT customerName ,customerNumber FROM {USER}CUSTOMERTABLE
            WHERE customerId =?;
            ''', (customerId,))
            customerDeatil = cursor.fetchall()
            print(
                f"\nPresent details of customer :\nName : {customerDeatil[0][0]}\nContact Number: {customerDeatil[0][1]}")
            print("\nEnter New customer details :-")
            customerName = input("Enter the customer name :")
            phoneNoVerification(2)
            cursor.execute(f'''
            UPDATE {USER}CUSTOMERTABLE
            SET customerName = ?, customerNumber = ?
            WHERE customerId =?;
            ''', (customerName, customerNumber, customerId))
            conn.commit()
            print("Details Updated Succesfully ....")
            cleanScreen(1)
            updateDataMenu()
        elif(check == 0):
            print("Entered customer ID doesn't exists")
            cleanScreen(1)
            updateDataMenu()
    elif a == 3:
        productId = input(
            "Enter the ID of product whose details you want to update :")
        check = idList.count(productId)
        if check != 0:
            cursor.execute(f'''
            SELECT productName ,productQuantity FROM {USER}PRODUCTTABLE
            WHERE productId =?;
            ''', (productId,))
            productDeatil = cursor.fetchall()
            print(
                f"\nPresent details of product :\nName : {productDeatil[0][0]}\nQuantity:{productDeatil[0][1]}")
            print("\nEnter New product details :-")
            productName = input("Enter the Product name :")
            productQuantity = input("Enter the Product quantity :")
            cursor.execute(f'''
            UPDATE {USER}PRODUCTTABLE
            SET productName = ?, productQuantity = ?
            WHERE productId =?;
            ''', (productName, productQuantity, productId))
            conn.commit()
            print("Details Updated Succesfully ....")
            cleanScreen(1)
            updateDataMenu()
        elif(check == 0):
            print("Entered product ID doesn't exists")
            cleanScreen(1)
            updateDataMenu()


def printSupplierDetails():
    maxLenCol1 = 11
    maxLenCol2 = 13
    maxLenCol3 = 20
    heading = maxLenCol1+maxLenCol2+maxLenCol3+4
    cursor.execute(f'''
        SELECT * FROM {USER}SUPPLIERTABLE
        ORDER BY supplierName;
        ''')
    supplierDetail = cursor.fetchall()
    for i in supplierDetail:
        if len(i[0]) > maxLenCol1:
            maxLenCol1 = len(i[0])
    for i in supplierDetail:
        if len(i[1]) > maxLenCol2:
            maxLenCol2 = len(i[1])
    for i in supplierDetail:
        if len(i[2]) > maxLenCol3:
            maxLenCol3 = len(i[2])
    print(" "*((heading//2)-9), "SUPPLIER DETAILS")
    print(" "+"─"*maxLenCol1+" "+"─"*maxLenCol2+" "+"─"*maxLenCol3+" ")
    print("│"+"Supplier ID"+" "*(maxLenCol1-11)+"│"+"Supplier Name"+" " *
          (maxLenCol2-13)+"│"+"Supplier Contact No."+" "*(maxLenCol3-20)+"│")
    for i in range(len(supplierDetail)):
        print("│"+"─"*maxLenCol1+"│"+"─"*maxLenCol2+"│"+"─"*maxLenCol3+"│")
        print("│"+supplierDetail[i][0]+" "*(maxLenCol1-len(supplierDetail[i][0]))+"│"+supplierDetail[i][1]+" "*(
            maxLenCol2-len(supplierDetail[i][1])) + "│"+supplierDetail[i][2]+" "*(maxLenCol3-len(supplierDetail[i][2]))+"│")
    print(" "+"─"*maxLenCol1+" "+"─"*maxLenCol2+" "+"─"*maxLenCol3+" ")
    cleanScreen(1)
    printDataMenu()


def printCustomerDetails():
    maxLenCol1 = 11
    maxLenCol2 = 13
    maxLenCol3 = 20
    heading = maxLenCol1+maxLenCol2+maxLenCol3+4
    cursor.execute(f'''
        SELECT * FROM {USER}CUSTOMERTABLE
        ORDER BY customerName;
        ''')
    customerDetail = cursor.fetchall()
    for i in customerDetail:
        if len(i[0]) > maxLenCol1:
            maxLenCol1 = len(i[0])
    for i in customerDetail:
        if len(i[1]) > maxLenCol2:
            maxLenCol2 = len(i[1])
    for i in customerDetail:
        if len(i[2]) > maxLenCol3:
            maxLenCol3 = len(i[2])
    print(" "*((heading//2)-10), "CUSTOMER DETAILS")
    print(" "+"─"*maxLenCol1+" "+"─"*maxLenCol2+" "+"─"*maxLenCol3+" ")
    print("│"+"Customer ID"+" "*(maxLenCol1-11)+"│"+"Customer Name"+" " *
          (maxLenCol2 - 13)+"│"+"Customer Contact No."+" "*(maxLenCol3-20)+"│")
    for i in range(len(customerDetail)):
        print("│"+"─"*maxLenCol1+"│"+"─"*maxLenCol2+"│"+"─"*maxLenCol3+"│")
        print("│"+customerDetail[i][0]+" "*(maxLenCol1-len(customerDetail[i][0]))+"│"+customerDetail[i][1]+" "*(
            maxLenCol2-len(customerDetail[i][1]))+"│"+customerDetail[i][2]+" "*(maxLenCol3-len(customerDetail[i][2]))+"│")
    print(" "+"─"*maxLenCol1+" "+"─"*maxLenCol2+" "+"─"*maxLenCol3+" ")
    cleanScreen(1)
    printDataMenu()


def printProductDetails():
    maxLenCol1 = 10
    maxLenCol2 = 12
    maxLenCol3 = 16
    heading = maxLenCol1+maxLenCol2+maxLenCol3+4
    cursor.execute(f'''
        SELECT * FROM {USER}PRODUCTTABLE
        ORDER BY productName;
        ''')
    productDetail = cursor.fetchall()
    for i in productDetail:
        if len(i[0]) > maxLenCol1:
            maxLenCol1 = len(i[0])
    for i in productDetail:
        if len(i[1]) > maxLenCol2:
            maxLenCol2 = len(i[1])
    for i in productDetail:
        if len(i[2]) > maxLenCol3:
            maxLenCol3 = len(i[2])
    print(" "*((heading//2)-8), "PRODUCT DETAILS")
    print(" "+"─"*maxLenCol1+" "+"─"*maxLenCol2+" "+"─"*maxLenCol3+" ")
    print("│"+"Product ID"+" "*(maxLenCol1-10)+"│"+"Product Name"+" "*(maxLenCol2 -
          12)+"│"+"Product Quantity"+" "*(maxLenCol3-19)+"│")
    for i in range(len(productDetail)):
        print("│"+"─"*maxLenCol1+"│"+"─"*maxLenCol2+"│"+"─"*maxLenCol3+"│")
        print("│"+productDetail[i][0]+" "*(maxLenCol1-len(productDetail[i][0]))+"│"+productDetail[i][1]+" "*(
            maxLenCol2-len(productDetail[i][1]))+"│"+productDetail[i][2]+" "*(maxLenCol3-len(productDetail[i][2]))+"│")
    print(" "+"─"*maxLenCol1+" "+"─"*maxLenCol2+" "+"─"*maxLenCol3+" ")
    cleanScreen(1)
    printDataMenu()


def idVerification(a):
    global supplierId, customerId, productId
    idList = []
    if a == 1:
        cursor.execute(f'''
        SELECT supplierId FROM {USER}SUPPLIERTABLE;
        ''')
        supplierId = input("Enter the ID of Supplier :")
    elif a == 2:
        cursor.execute(f'''
        SELECT customerId FROM {USER}CUSTOMERTABLE;
        ''')
        customerId = input("Enter the ID of Customer :")
    elif a == 3:
        cursor.execute(f'''
        SELECT productId FROM {USER}PRODUCTTABLE;
        ''')
        productId = input("Enter the ID of Product :")
    allIdList = cursor.fetchall()
    for element in allIdList:
        idList.append(element[0])
    t = len(idList)
    if(t == 0):
        pass
    else:
        if a == 1:
            check = idList.count(supplierId)
        elif a == 2:
            check = idList.count(customerId)
        elif a == 3:
            check = idList.count(productId)
        if(check == 0):
            pass
        else:
            if(check != 0):
                nameList = []
                if a == 1:
                    cursor.execute(f'''
                        SELECT supplierName FROM {USER}SUPPLIERTABLE;
                        ''')
                    allNameList = cursor.fetchall()
                    i = idList.index(supplierId)
                    for element in allNameList:
                        nameList.append(element[0])
                    print("This ID is already given to Supplier name :",
                          nameList[i])
                    idVerification(1)
                elif a == 2:
                    cursor.execute(f'''
                        SELECT customerName FROM {USER}CUSTOMERTABLE;
                        ''')
                    allNameList = cursor.fetchall()
                    i = idList.index(customerId)
                    for element in allNameList:
                        nameList.append(element[0])
                    print("This ID is already given to Customer name :",
                          nameList[i])
                    idVerification(2)
                elif a == 3:
                    cursor.execute(f'''
                        SELECT productName FROM {USER}PRODUCTTABLE;
                        ''')
                    allNameList = cursor.fetchall()
                    i = idList.index(productId)
                    for element in allNameList:
                        nameList.append(element[0])
                    print("This ID is already given to Product name :",
                          nameList[i])
                    idVerification(3)


def phoneNoVerification(a):
    global supplierNumber, customerNumber
    if a == 1:
        supplierNumber = (input("Enter the Mobile No. of Supplier:"))
        number = supplierNumber.isdigit()
    elif a == 2:
        customerNumber = (input("Enter the Mobile No. of Customer:"))
        number = customerNumber.isdigit()
    if (number == True):
        if a == 1:
            number2 = int(supplierNumber)
            numberLen = len(supplierNumber)
        elif a == 2:
            number2 = int(customerNumber)
            numberLen = len(customerNumber)
        if (number2 > 999999999) and (number2 < 10000000000):
            pass
        elif(numberLen == 10 and number2 <= 999999999):
            print("Phone no can't be exixt")
            if a == 1:
                phoneNoVerification(1)
            elif a == 2:
                phoneNoVerification(2)
        else:
            print(
                f"Contact no. is not a 10 digit no. you enter a {len(str(supplierNumber))} digit no.\nPlease, Enter a valid number")
            if a == 1:
                phoneNoVerification(1)
            elif a == 2:
                phoneNoVerification(2)
    else:
        print("Please, Enter only numeric value")
        if a == 1:
            phoneNoVerification(1)
        elif a == 2:
            phoneNoVerification(2)


def addSupplierDetail():
    supplierName = input("Enter the Name of Supplier :")
    idVerification(1)
    phoneNoVerification(1)
    cursor.execute(f'''
        INSERT INTO {USER}SUPPLIERTABLE 
        VALUES(?,?,?);
        ''', (supplierId, supplierName, supplierNumber))
    conn.commit()
    print("Supplier Detail Added Succesfully .......")
    cleanScreen(1)
    inputDataMenu()


def addCustomerDetail():
    customerName = input("Enter the Name of customer :")
    idVerification(2)
    phoneNoVerification(2)
    cursor.execute(f'''
        INSERT INTO {USER}CUSTOMERTABLE 
        VALUES(?,?,?);
        ''', (customerId, customerName, customerNumber))
    conn.commit()
    print("Customer Detail Added Succesfully .......")
    cleanScreen(1)
    inputDataMenu()


def addProductDetail():
    productName = input("Enter the Name of Product :")
    idVerification(3)
    productQuantity = input("Enter the Quantity of Product :")
    cursor.execute(f'''
        INSERT INTO {USER}PRODUCTTABLE
        VALUES(?,?,?);
        ''', (productId, productName, productQuantity))
    conn.commit()
    print("Product Detail Added Succesfully .......")
    cleanScreen(1)
    inputDataMenu()


welcomeSciptList = [("*"*70), (" "*20+"Welcome user to the program"),
                    (" "*6+"This program make your inventory management easy to handle"), ("*"*70)]
endSciptList = [("*"*70), (" "*20+"Thanks for using our services"), ("*"*70)]
supplierId = None
supplierNumber = None
customerId = None
customerNumber = None
productId = None
USER = None

cleanScreen(2)

conn = connection("INVENTORY_DATABASE")
cursor = conn.cursor()

createTable()

try:
    loginMenu()
except Exception as error:
    print(error)
    cleanScreen(1)
    exit()

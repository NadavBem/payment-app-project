import MySQLdb
import os
from validation import check_if_user_exists, check_if_creditcard_exists, check_if_bankaccount_exists

host_var = "localhost" if os.getenv("SQL_HOST")== None else os.getenv("SQL_HOST")
user_var = "root" if os.getenv("SQL_USER") == None else os.getenv("SQL_USER")
password_var = "123456" if os.getenv("SQL_PASSWORD") == None else os.getenv("SQL_PASSWORD")
database_name_var = "paymant_app" if os.getenv("SQL_DB_NAME") == None else os.getenv("SQL_DB_NAME")
port_var = 3309 if os. getenv("SQL_PORT")== None else int(os.getenv("SQL_PORT"))


@check_if_user_exists
def add_new_user (User):
    db_connection = MySQLdb.connect(
    host = "127.0.0.1",
    user = "root",
    password = "123456",
    database = "paymant_app",
    port = 3309
    )

    cursor = db_connection.cursor()
    cursor.execute(f"INSERT INTO PaymentAppUser (UserID ,FirstName, LastName, PhoneNum, Email, PassWD) VALUES ('{User.UserID}','{User.FirstName}', '{User.LastName}','{User.PhoneNum}','{User.Email}','{User.PassWD}')")
    db_connection.commit()
    print("User added successfully!")
    db_connection.close()
    return (f"hi {User.FirstName} welcome to Just To Pay")

@check_if_creditcard_exists
def add_creditcard(creditcard):
    db_connection = MySQLdb.connect(
    host = "127.0.0.1",
    user = "root",
    password = "123456",
    database = "paymant_app",
    port = 3309
    )

    cursor = db_connection.cursor()
    cursor.execute(f"INSERT INTO CreditCard (UserID, FirstName, LastName, CreditNum, Validity, CVV ) VALUES ('{creditcard.UserID}','{creditcard.FirstName}', '{creditcard.LastName}','{creditcard.CreditNum}','{creditcard.Validity}','{creditcard.CVV}')")
    db_connection.commit()
    print("Credit card added successfully!")
    db_connection.close()
    return (f"hi {creditcard.FirstName} you just added a credit card that end with the 4 digit:{creditcard.CreditNum[-4:]}")

@check_if_bankaccount_exists
def add_bankaccount(bankaccount):
    db_connection = MySQLdb.connect(
    host = "127.0.0.1",
    user = "root",
    password = "123456",
    database = "paymant_app",
    port = 3309
    )

    cursor = db_connection.cursor()
    cursor.execute(f"INSERT INTO BankAccount (UserID, FirstName, LastName, BankNum, Branch, AccountNum ) VALUES ('{bankaccount.UserID}','{bankaccount.FirstName}', '{bankaccount.LastName}','{bankaccount.BankNum}','{bankaccount.Branch}','{bankaccount.AccountNum}')")
    db_connection.commit()
    print("Bank account added successfully!")
    db_connection.close()  
    return (f"hi {bankaccount.FirstName} you just added your bank account that his number:{bankaccount.AccountNum}")
    
def send_money(transfer_details):
    db_connection = MySQLdb.connect(
    host = "127.0.0.1",
    user = "root",
    password = "123456",
    database = "paymant_app",
    port = 3309
    )

    cursor = db_connection.cursor()
    cursor.execute(f"SELECT * FROM CreditCard WHERE UserID = '{transfer_details.UserID}'")
    db_connection.commit()
    credit_card_results = cursor.fetchall()
    cursor.execute(
    "SELECT BankAccount.* FROM BankAccount "
    "JOIN PaymentAppUser ON BankAccount.UserID = PaymentAppUser.UserID "
    f"WHERE PaymentAppUser.PhoneNum = '{transfer_details.PhoneNum_to_how}'"
    )
    bank_account_results = cursor.fetchall()
    db_connection.close()
    return credit_card_results, bank_account_results 
    

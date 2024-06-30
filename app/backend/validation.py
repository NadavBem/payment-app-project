import MySQLdb
import os

def get_db_connection():
    db_connection = MySQLdb.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME', 'paymant_app'),  
        port=int(os.getenv('DB_PORT', 3306))  
    )
    return db_connection

def check_if_user_exists(func):
    def wrapper(User):
        db_connection = get_db_connection()
        cursor = db_connection.cursor()
        
        cursor.execute(f"SELECT COUNT(*) FROM PaymentAppUser WHERE UserID = '{User.UserID}' OR PhoneNum = '{User.PhoneNum}' OR Email = '{User.Email}' OR PassWD = '{User.PassWD}'")
        result = cursor.fetchone()
        if result and result[0] > 0:
            return "User details already exist in the database. User not added."
        else:
            func(User)
        
        db_connection.close()
    
    return wrapper

def check_if_creditcard_exists(func):
    def wrapper(creditcard):
        db_connection = get_db_connection()
        cursor = db_connection.cursor()
        
        cursor.execute(f"SELECT COUNT(*) FROM CreditCard WHERE UserID = '{creditcard.UserID}' OR CreditNum = '{creditcard.CreditNum}'")
        result = cursor.fetchone()
        if result and result[0] > 0:
            return "Credit card details already exist in the database. card not added."
        else:
            func(creditcard)
        
        db_connection.close()
    
    return wrapper
    

def check_if_bankaccount_exists(func):
    def wrapper(bankaccount):
        db_connection = get_db_connection()
        cursor = db_connection.cursor()
        
        cursor.execute(f"SELECT COUNT(*) FROM BankAccount WHERE UserID = '{bankaccount.UserID}' OR AccountNum = '{bankaccount.AccountNum}'")
        result = cursor.fetchone()
        if result and result[0] > 0:
            return "Bank account details already exist in the database. bank account not added."
        else:
            func(bankaccount)
        
        db_connection.close()
    
    return wrapper

class BankAccount():
    def __init__(self,UserID, FirstName, LastName, BankNum, Branch, AccountNum,):
        self.UserID = UserID
        self.FirstName = FirstName
        self.LastName = LastName
        self.BankNum = BankNum
        self.Branch = Branch
        self.AccountNum = AccountNum

    def __str__(self):
        return f"'{self.UserID}', '{self.FirstName}', '{self.LastName}', {self.BankNum}, '{self.Branch}', '{self.AccountNum}'"
            

class CreditCard():
    def __init__(self, UserID, FirstName, LastName, CreditNum, Validity, CVV):
        self.UserID = UserID
        self.FirstName = FirstName
        self.LastName = LastName
        self.CreditNum = CreditNum
        self.Validity = Validity
        self.CVV = CVV

    def __str__(self):
        return f"'{self.UserID}', '{self.FirstName}', '{self.LastName}', {self.CreditNum}, '{self.Validity}', '{self.CVV}'"    
        
class PaymentAppUser():
    def __init__(self, UserID, FirstName, LastName, PhoneNum, Email, PassWD,CreditCard: CreditCard = None, BankAccount: BankAccount = None, ID = None ):
        self.UserID = UserID
        self.FirstName = FirstName
        self.LastName = LastName
        self.PhoneNum = PhoneNum
        self.Email = Email
        self.PassWD = PassWD
        self.CreditCard = CreditCard
        self.BankAccount = BankAccount
        self.ID = ID
    
    def __str__(self):
        return f"'{self.UserID}', '{self.FirstName}', '{self.LastName}', '{self.PhoneNum}', '{self.Email}', '{self.PassWD}', '{self.CreditCard}', '{self.BankAccount}', '{self.Email}'"    
        
        
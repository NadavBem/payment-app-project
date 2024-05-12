import uvicorn
from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import paymentapp
payment_app = FastAPI()

class PaymentAppUser(BaseModel):
    UserID: str
    FirstName: str
    LastName: str 
    PhoneNum: str 
    Email: str 
    PassWD: str

class CreditCard(BaseModel):
    UserID: str
    FirstName: str
    LastName: str 
    CreditNum: str 
    Validity: str 
    CVV: str

class BankAccount(BaseModel):
    UserID: str
    FirstName: str
    LastName: str 
    BankNum: str 
    Branch: str 
    AccountNum: str  

class SendMoney(BaseModel):
    UserID : str
    Amount : int
    PhoneNum_to_how : str 
    PassWD : str 


@payment_app.get("/")
async def root():
    return {"message": "Welcome to JUST TO PAY"}         

@payment_app.post("/add_user/")
async def create_account(new_user: PaymentAppUser):
   return paymentapp.add_new_user(new_user)
  
@payment_app.post("/add_creditcard/")
async def add_creditcard_to_user(new_creditcard: CreditCard):
    return paymentapp.add_creditcard(new_creditcard)

@payment_app.post("/add_bankaccount/")
async def add_bankaccount_to_user(new_bankaccount: BankAccount):
    return paymentapp.add_bankaccount(new_bankaccount)

@payment_app.put("/send_money/")
async def send_money_to_user(transfer_details: SendMoney):
   return paymentapp.send_money(transfer_details)

if __name__ == '__main__':
    uvicorn.run(payment_app, host="0.0.0.0", port=8000)
        # http://127.0.0.1:8000/docs#/    

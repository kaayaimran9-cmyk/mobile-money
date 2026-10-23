import json
import datetime
from functions import *

now = datetime.datetime.now()



class Customer:
    def __init__ (self,customer_id,first_name,last_name,date_of_birth,gender,address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address


class Account:
    def __init__(self,account_number,account_name,pin):
        self.account_number = account_number
        self.account_name = account_name
        self._balance:int = 0
        self.pin = pin

    
    def set_balance(self):

        

        for key, value in account_data.items():
        
            if self.account_name == value["account_name"]:

                value["account_balance"] = self._balance 

                return self._balance


    
        

class Transaction(Account):

    
    def __init__(self,account_number,account_name,pin,type,amount):

        super().__init__(account_number,account_name,pin)
        self.type = type
        self.__transaction_id = "none"
        self.amount:int = amount

        self.__status = "" 
        self._new_balance = 0
        


    def change_status(self,amount):
        
    

        if amount >= self._balance:

            self.__status = "failed"
            
            return f"{self.__status}"
        else:

            self.__status = "success"

                             
            return f"{self.__status}"
            

    def update_sender_balance(self, amount):

        #deduct money


        if self.type == "send":
            if self._balance >= amount:

                self._balance -= amount
                for key, value in account_data.items():
                
                    if self.account_name == value["account_name"]:
                
                        value["account_balance"] = self._balance
                        update_account_data()


        elif self.type == "withdraw":

            if self._balance >= amount:
            
                self._balance -= amount
                for key, value in account_data.items():
            
                    if self.account_name == value["account_name"]:
            
                        value["account_balance"] = self._balance
                        update_account_data()

        elif self.type == "deposit":

            self._balance += amount
            for key, value in account_data.items():
            
                if self.account_name == value["account_name"]:
            
                    value["account_balance"] = self._balance
                    update_account_data()


    def update_receiver_balance(self, amount):

        
        if self._balance >= amount:
            for key, value in account_data.items():
            
                if self.account_number == value["account_number"]:
            
                    value["account_balance"] += amount 
                    update_account_data()

    def set_transaction_id(self):

        if self.type == "send":


            if self.__status == "success":

                return f"success, sent ugx {self.amount} at {now}"
            else:
                return f"transaction of ugx {self.amount} failed at {now} "


        elif self.type ==  "withdraw":


            if self.__status == "success":
            
                return f"success, withdrawn ugx {self.amount} at {now}"
            else:
                return f"withdraw of ugx {self.amount} failed at {now} due to insufficient balance "


        elif self.type ==  "deposit":

            return f"success, deposited ugx {self.amount} at {now}"
           





       

    
                
                


    
    




class Agent:
    def __init__(self,agent_id,first_name,last_name,gender,address,contact):
        self.agent_id = agent_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.address = address
        self.contact = contact

class Money_transfer:
    def __init__(self,amount,receiver_number,pin):
        #self.__transfer_id = ""
        self.receiver_number = receiver_number
        self.amount:int = amount
        self.__status = "none"
        self.pin = pin      #amount

 

class Deposit:
    def __init__(self,customer_id,account_number,amount):
        self.customer_id = customer_id
        self.account_number = account_number
        self.amount:int = amount   
        self.__status = "" #amount
        
        

class Withdraw:
    def __init__(self,customer_id,amount):
        self.customer_id = customer_id
        self.__withdraw_id = "none"
        self.amount:int = amount
        self.__agent_id = ""  #agent
        self.__status = ""  #amount

    


    def set_withdraw_id(self):

        self.__withdraw_id = f"withdrawn ugx {self.amount} "

        return self.__withdraw_id
       

class Merchant:
    def __init__(self,merchant_code,merchant_name,contact,business_name):
        self.merchant_code = merchant_code
        self.merchant_name = merchant_name
        self.contact = contact
        self.business_name = business_name

class Payment:
    def __init__(self,merchant_code,payment_method,amount):
        self.merchant_code = merchant_code
        self.__payment_id = "none"
        self.payment_method = payment_method
        self.amount:int = amount
      
        self.__status = "Success"  #amount

    def set_payment_id(self):

        self.__payment_id = f"Paid ugx {self.amount}"

        return self.__payment_id


     
import json


#LOADING DATA

def load_customer_data():
    with open("customer_data.json", "r")as file:
        return json.load(file)

def load_account_data():
    with open("account.json", "r")as file:
        return json.load(file)

def load_agent_data():
    with open("agent.json", "r")as file:
        return json.load(file)
    
def load_transaction_data():
    with open("transaction.json", "r")as file:
        return json.load(file)

def load_money_transfer_data():
    with open("money_transfer.json", "r")as file:
        return json.load(file)

def load_deposit_data():
    with open("deposit.json", "r")as file:
        return json.load(file)
    
def load_withdraw_data():
    with open("withdraw.json", "r")as file:
        return json.load(file)
    
def load_merchant_data():
    with open("merchant.json", "r")as file:
        return json.load(file)
def load_payment_data():
    with open("payment.json","r") as file:
        return json.load(file)



#UPDATING DATA

def update_customer_data():
    with open("customer_data.json" , "w")as file:
        json.dump(customer_data,file, indent = 4)

def update_account_data():
    with open("account.json" , "w")as file:
        json.dump(account_data,file, indent = 4)

def update_transaction_data():
    with open("transaction.json" , "w")as file:
        json.dump(transaction_data,file, indent = 4)

def update_agent_data():
    with open("agent.json" , "w")as file:
        json.dump(agent_data,file, indent = 4)

def update_money_transfer_data():
    with open("money_transfer.json" , "w")as file:
        json.dump(Money_transfer_data,file, indent = 4)

def update_deposit_data():
    with open("deposit.json" , "w")as file:
        json.dump(deposit_data,file, indent = 4)

def update_withdraw_data():
    with open("withdraw.json" , "w")as file:
        json.dump(withdraw_data,file, indent = 4)

def update_merchant_data():
    with open("merchant.json" , "w")as file:
        json.dump(merchant_data,file, indent = 4)
def update_payment_data():
    with open("payment.json","w")as file:
        json.dump(payment_data,file,indent=4)


#ASSIGNING VARIABLES TO JSON DATA
payment_data =load_payment_data()
merchant_data = load_merchant_data()
withdraw_data = load_withdraw_data()
deposit_data = load_deposit_data()
Money_transfer_data = load_money_transfer_data()
agent_data = load_agent_data()
transaction_data = load_transaction_data()
account_data = load_account_data()
customer_data = load_customer_data()
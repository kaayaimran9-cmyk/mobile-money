

from functions import *

from classes import Customer,Account,Transaction,Agent,Money_transfer,Deposit,Withdraw,Merchant,Payment


#program starts


print("---WELCOME--TO--MOBILE MONEY------")
print()

print("Menu:")
print()
print("1.Register customer")
print("2.Login")
print("3.exit")


print()

option = input("enter option: ")




if option == "1":

    #CUSTOMER
    print("CUSTOMER")
    while True:
        customer_id = input("enter customer-id: ")
    
        for customer, customer_details in customer_data.items():
    
            if customer_id == customer_details["customer_id"]:
    
                print("customer_id provided is already taken")
    
                break
        else:
    
            first_name = input("enter first-name: ") 
            last_name = input("enter last-name: ")
            print()
            date_of_birth = input("enter date-of-birth: ")
            gender = input("enter your gender: ")
            address = input("enter address: ")
    
            customer = Customer(customer_id,first_name,last_name,date_of_birth,gender,address,)
    
            dictionary = {
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "gender": gender,
            "address": address
    
    
        }
    
            ID = f"Customer_ {len(customer_data) + 1:003} "
            customer_data[ID] = dictionary
    
            update_customer_data()
    
            print()
            more = input("Are you still registering(y/n): ").lower().strip()
    
            if more == "y" or more == "yes":
                continue
    
            else:
    
                for key,value in customer_data.items():
    
                    print()
    
                    print(key)
                    print(f"CUSTOMER ID: {value["customer_id"]}")
                    print(f"ADDRESS: {value["address"]}")
    
    
                break


    
elif option =="2":

    check_name = input("enter account-name to continue: ")
    check_pin = input("enter pin to continue: ")


    for key, value in account_data.items():

        if check_name == value["account_name"] and check_pin == value["pin"]:

            print()
            print("WELCOME TO MOBILE MONEY")

            print(f"CURRENT USER: {check_name.upper()}")


            print("1.Register account")
            print("2.Make transactions")
            print("3.Register an agent")
            print()
            print("4.Transfer money")
            print("5.Deposit")
            print("6.Withdraw")
            print("7.Merchant")
            print("8.Payment")
            print("9.exit")
            
            print()
            
            option = input("enter option: ").strip()
            
            
            
            
            
            
            if option == "1":
            
            
                #ACCOUNT
                print("ACCOUNT")
            
                while True:
            
                    account_name = input("enter account-name: ")
                    account_number = input("enter account number: ")
                    pin = int(input("enter pin: "))
            
            
                    customer = Account(account_number,account_name,pin)
            
                    customer.set_balance()
            
            
                    dictionary = {
                        "account_number": account_number,
                        "account_name": account_name,
                        "pin": pin,
                        "account_balance":customer.set_balance()
                    }
            
                    ID = f"Customer_ {len(account_data) + 1:003} "
            
                    account_data[ID] = dictionary
            
                    update_account_data()
            
                    print()
                    more = input("Are you still registering(y/n): ").lower().strip()
            
                    if more == "y" or more == "yes":
                        continue
            
                    else:
            
            
                        for key,value in account_data.items():
            
                            print()
            
                            print(key)
                            print(f"ACCOUNT-NAME: {value["account_name"]}")
                            print(f"ACCOUNT-NUMBER: {value["account_number"]}")
            
            
                        break            
            
            
            elif option == "2":
            
                #TRANSACTION
                print("TRANSACTION")
            
                while True:
            
            
            
                    account_number = input("enter account number: ")
                    account_name = input("enter account name: ")
                    pin = input("enter pin: ")
                    type = input("enter type: ")
                    amount = int(input("enter amount: "))
                    date = input("enter date: ")
                    time = input("enter time: ")
            
            
                    customer = Transaction(account_number,account_name,pin,type,amount,date,time) 
            
                    check = customer.change_status()
            
                    customer.deposit()
            
                    dictionary = {
            
                        "transaction_id":"send",
                        "amount":amount,
                        "date":date,
                        "time":time,
                        "status":check
            
            
            
                    }
            
                    ID = f"Customer_ {len(transaction_data) + 1:003} "
            
                    transaction_data[ID] = dictionary
            
                    update_transaction_data()
            
                    print()
                    more = input("Are you still registering(y/n): ").lower().strip()
            
                    if more == "y" or more == "yes":
                        continue
            
                    else:
            
            
                        for key,value in transaction_data.items():
            
                            print()
            
                            print(key)
                            print(f"AMOUNT: {value["amount"]}")
                            print(f"TRANSACTION-TYPE: {value["transaction_id"]}")
                            print(f"TIME: {value["time"]}")
            
            
                        break  
            
            
            
            elif option == "3":
            
                #AGENT
                print("AGENT")
            
                while True:
                    agent_id = input("enter your agent-id: ")   
                    first_name = input("enter first-name: ")
                    last_name = input("enter last-name: ")
                    gender = input("enter gender: ")    
                    address = input("enter addresss: ")
                    contact = input("privide your contact: ")
            
                    agent = Agent(agent_id,first_name,last_name,gender,address,contact)
            
                    dictionary = {
                        "agent_id": agent_id,
                        "first_name": first_name,
                        "last_name": last_name,
                        "gender": gender,
                        "address": address,
                        "contact": contact
                    }
            
                    ID = f"Agent_ {len(agent_data) + 1:003} "
            
                    agent_data[ID] = dictionary
            
                    update_agent_data()
            
                    print()
                    more = input("Are you still registering(y/n): ").lower().strip()
            
                    if more == "y" or more == "yes":
                        continue
            
                    else:
            
                        for key,value in agent_data.items():
            
                            print()
            
                            print(key)
                            print(f"AGENT-ID: {value["agent_id"]}")
                            print(f"CONTACT: {value["contact"]}")
            
            
                        break
            
            
            elif option == "4":
            
                #MONEY TRANSFER
                print("TRANSFER")
            
                while True:
            
                    amount = int(input("enter amount: "))
            
                    receiver_number = input("enter receiving number: ")
            
                    customer = Money_transfer(amount,receiver_number)
            
                    dictionary = {
                        "amount":amount,
                        "receiver": receiver_number
                    }
            
                    ID = f"Money_transfer_ {len(Money_transfer_data) + 1:003} "
            
                    Money_transfer_data[ID] = dictionary
            
                    update_money_transfer_data()
            
                    print()
                    more = input("Are you still registering(y/n): ").lower().strip()
            
                    if more == "y" or more == "yes":
                        continue
            
                    else:
            
                        for key,value in Money_transfer_data.items():
            
                            print()
            
                            print(key)
                            print(f"AMOUNT: {value["amount"]}")
                            print(f"RECEIVER: {value["receiver"]}")
            
                        break
            
            
            elif option == "5":
            
                #DEPOSIT
                print("DEPOSIT")
            
            
                while True:
            
                    account_id = input("enter account id: ")
            
                    account_number= input("enter account number:")
                    amount = int(input("enter amount: "))
            
                    customer = Deposit(account_id,account_number,amount)
            
                    dictionary = {
                        "account_id": account_id,
            
                        "account_number":account_number,
                        "amount":amount
                    }
            
            
                    ID = f"Deposit_ {len(deposit_data) + 1:003} "
            
                    deposit_data[ID] = dictionary
            
                    update_deposit_data()
            
                    print()
                    more = input("Are you still registering(y/n): ").lower().strip()
            
                    if more == "y" or more == "yes":
                        continue
            
                    else:
            
                        for key,value in deposit_data.items():
            
                            print()
            
                            print(key)
                            print(f"ACCOUNT-ID: {value["account_id"]}")
                            print(f"AMOUNT: {value["amount"]}")
            
            
            
                        break
            
            
            
            elif option == "6":
            
                #WIHDRAW
                print("WITHDRAW")
            
            
            
                while True:
            
                    customer_id = input("enter customer_id: ")
                    amount = int(input("enter amount:"))
            
                    customer = Withdraw(customer_id,amount)
            
                    customer.set_withdraw_id()
            
                    dictionary ={
                        "customer_id":customer_id,
                        "amount":amount,
                        "withdraw_id": customer.set_withdraw_id()
                    }
            
                    ID = f"Withdraw_ {len(withdraw_data) + 1:003} "
            
                    withdraw_data[ID] = dictionary
            
                    update_withdraw_data()
            
                    print()
                    more = input("Are you still registering(y/n): ").lower().strip()
            
                    if more == "y" or more == "yes":
                        continue
            
                    else:
            
                        for key,value in withdraw_data.items():
            
                            print()
            
                            print(key)
                            print(f"CUSTOMER-ID: {value["customer_id"]}")
                            print(f"AMOUNT: {value["amount"]}")
                            print(f"WITHDRAW: {value["withdraw_id"]}")
            
                        break
            
            
            elif option == "7":
                #MERCHANT
            
                print("MERCHANT")
            
                while True:
                    merchant_code =input("enter merchant code: ")
                    merchant_name = input("enter merchant name: ")
                    contact = input("enter contact: ")
                    business_name =input ("enter business name: ")
            
            
                    customer = Merchant(merchant_code,merchant_name,contact,business_name)
            
                    dictionary = {
                        "merchant_code":merchant_code,
                        "merchant_name" : merchant_name,
                        "contact": contact,
                        "business_name": business_name
            
                    }
            
            
            
            
                    ID = f"Merchant_ {len(merchant_data) + 1:003} "
            
                    merchant_data[ID] = dictionary
            
                    update_merchant_data()
            
                    print()
                    more = input("Are you still registering(y/n): ").lower().strip()
            
                    if more == "y" or more == "yes":
                        continue
            
                    else:
            
                        for key,value in merchant_data.items():
            
                            print()
            
                            print(key)
                            print(f"MERCHANT-NAME: {value["merchant_name"]}")
                            print(f"BUSINESS-NAME: {value["business_name"]}")
                            print(f"MERCHANT-CODE: {value["merchant_code"]}")
            
            
                        break
            
            elif option == "8":
                #payment
                print("PAYMENT")
                while True:
            
                    merchant_code =input("enter merchant code: ")
                    payment_method = input("enter payment method: ")
                    amount = int(input("enter amount: "))
            
            
            
                    customer = Payment(merchant_code,payment_method,amount)
            
                    payment = customer.set_payment_id()
            
                    dictionary = {
                        "merchant_code":merchant_code,
                        "payment_method" : payment_method,
                        "amount" : amount,
                        "payment_id": payment
            
                    }
            
            
            
            
                    ID = f"Payment_ {len(payment_data) + 1:003} "
            
                    payment_data[ID] = dictionary
            
                    update_payment_data()
            
                    print()
                    more = input("Are you still registering(y/n): ").lower().strip()
            
                    if more == "y" or more == "yes":
                        continue
            
                    else:
            
                        for key,value in payment_data.items():
            
                            print()
            
                            print(key)
                            print(f"MERCHANT CODE: {value["merchant_code"]}")
                            print(f"PAYMENT METHOD: {value["payment_method"]}")
                            print(f"PAYMENT_ID: {value["payment_id"]}")
                            print(f"AMOUNT: {value["amount"]}")
            
            
                        break
            
            elif option == "9":
                print("bye")
                pass
            
            else:
                print("invalid option, sir/madam")
            
        


            #end here
            break

    else:
        print()
        print("invalid username or password...")
        


elif option == "3":
    

    print("bye")

    pass

else:

    print()

    print("option is invalid")






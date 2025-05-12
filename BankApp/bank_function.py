import random


accounts = []


#########Display Menu###########

def Menu():
  print("1. Exit \n2. Create \n3. Deposit Money \n4. Withdraw Money \n5. Transfer Money \n6. Account Summary \n7. Display All Accounts \n8. Save Accounts \n9. Load Accounts")

#########Uer input###########

def get_user_input(prompt):
  return input(prompt)

#########Create Accounts features###########

def create_account(name, account_number , balance):
  return {"name" : name, "account_number": account_number, "balance" : balance}

#########Generate Accounts Number###########

def generate_account_number():
  return random.randint(10000,99999)

  
#########Create Accounts###########
def create_account_features():
  name = get_user_input("Enter user name here :")
  account_number = generate_account_number()
  try:
    balance = float(get_user_input("Enter user account balance here :"))
    if balance < 0 :
      print("Invalid balance")
  except:
    print("Invalid balance")
  account = create_account(name,account_number,balance)
  accounts.append(account)
  print("Account created successfully!")


#########Find account###########

def find_account(account_number):
    for account in accounts:
      if account["account_number"] == account_number:
        return account
    return None
  
#########deposit money###########
def deposit_money(account, amount):
    account["balance"] += amount

def deposit_features():
    account_number = int(get_user_input("Enter account number :"))
    account = find_account(account_number)
    if account:
        try:
            amount = float(get_user_input("Enter amount to deposit :"))
            if amount < 0:
               print("Enter valid amount")
            else:
               deposit_money(account,amount)
        except:
            print("Enter valid amount")
    else:
       print("Account not found!")
    print("Operation complete !")
   

#########deposit money###########
def withdraw_money(account,amount):
   if amount <= account["balance"]:
       account["balance"] -= amount

def withdraw_features():
    account_number = int(get_user_input("Enter account number :"))
    account = find_account(account_number)
    if account:
        try:
            amount = float(get_user_input("Enter amount to withdrawn :"))
            if amount < 0 or amount > account["balance"]:
               print("Enter valid amount")
            else:
               withdraw_money(account,amount)
        except:
            print("Enter valid amount")
    else:
       print("Account not found!")
    print("Operation complete !")

#########transfer money###########

def transfer_money(from_account,to_account,amount):
    if from_account["balance"] >= amount:
       from_account["balance"] -= amount
       to_account["balance"] += amount
       return True
    return False
   

def transfer_features():
  
    from_account_number = int(get_user_input("Enter your account number : ") )
    from_account = find_account(from_account_number)
    if from_account :
      to_account_number = int(get_user_input("Enter recipient account number : "))
      to_account = find_account(to_account_number)
      if to_account :
          amount = float (get_user_input("Enter transfer amount :") )
          if transfer_money(from_account , to_account , amount ):
            print("Transfer successful!")
          else :
            print("Insufficient balance")
      else :
        print("Recipient account not found .")
    else :
      print("Your account not found .")


#########Dispplay feaatures###########
def display_all_accounts_feature () :
   for account in accounts:
      print(f"Account Number :{account ['account_number']} , Name :{account ['name']} , Balance : ${ account ['balance']:.2f}")


#########save  accounts###########
def save_accounts():
    try:
        f = open("accounts.txt", "w")
        for account in accounts:
            f.write(f"Account Number: {account['account_number']}, Name: {account['name']}, Balance: ${account['balance']:.2f}\n")
        print("Accounts saved successfully to accounts.txt.")
    except IOError:
        print("Error saving accounts to file.")

#########load accounts###########
def load_accounts():
    global accounts
    try:
        f = open("accounts.txt", "r")
        accounts = []
        for line in f:
            parts = line.strip().split(", ")
            account_number = int(parts[0].split(": ")[1])
            name = parts[1].split(": ")[1]
            balance = float(parts[2].split(": $")[1])
            accounts.append(create_account(name, account_number, balance))
        print("Accounts loaded successfully from accounts.txt.")
    except:
        print("Error loading accounts or file not found.")



#########Summary of accounts###########
def account_summary_feature():
    account_number = int(get_user_input("Enter account number for summary: "))
    account = find_account(account_number)
    if account:
        print(f"Account Summary:")
        print(f"Account Number: {account['account_number']}")
        print(f"Name: {account['name']}")
        print(f"Balance: ${account['balance']:.2f}")
    else:
        print("Account not found.")



# #########valid numbers###########
# def get_valid_number(prompt):
#   while True :
#     try :
#       return float(input(prompt))
#     except ValueError :
#       print ("Invalid input . Please enter a valid number .")

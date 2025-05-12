from bank_function import Menu , create_account_features, deposit_features,withdraw_features ,transfer_features,display_all_accounts_feature, save_accounts,load_accounts, account_summary_feature


def main():
    while True:
        Menu()
        try:
            choice = int(input("Enter your choice (1-9) here :"))
            if choice == 1:
              break
            elif choice == 2:
               create_account_features() 
            elif choice == 3:
              deposit_features()
            elif choice == 4:
              withdraw_features()
            elif choice == 5:
              transfer_features()
            elif choice == 6:
              account_summary_feature()
            elif choice == 7:
              display_all_accounts_feature()
            elif choice == 8:
              save_accounts ()
            elif choice == 9:
              load_accounts()
            else:
              print("Choice is incorrect select(1-9)")
            continue
            
        except:
          print("Choice is incorrect select(1-9)")
       
    
    
    
if __name__ == "__main__":
   main()
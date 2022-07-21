with open("accounts.txt", "r+") as accounts:
    def add_account():
        account_user_name = str(input("What's your full name? ")).strip()
        accounts.write(f"\n{account_user_name}")
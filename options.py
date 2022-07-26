def get_all():
    account_list = []
    with open("accounts.txt", "r") as accounts:
        line = accounts.readline()
        while (line != ''):
            line = line.strip('\n').split(',')
            account_owner = line[0]
            account_number = int(line[1])
            account_balance = float(line[2])
            account = [account_owner, account_number, account_balance]
            account.append(account)
            line = accounts.readline()
    return account_list


def save_all(list):
    with open('accounts.txt', 'w') as accounts:
        for account in list:
            accounts.write(f'{int(account[0])};{account[1]};{account[2]} \n')


def read_account():
    account_list = []
    with open ("accounts.txt", "r") as account_file:
        for line in account_file:
            line = line.rstrip("\n")
            line = line.split(",")
            account_list.append({"account_owner" : line[0], "account_number" : line[1], "account_balance" : line[2]})
    return account_list


def display_accounts(accounts_list):
    for account in accounts_list:
        print(account["account_owner"])


def add_account(account_list, account_owner, account_number, account_balance):
    account = {"account_owner" : account_owner, "account_number" : account_number, "account_balance" : account_balance}
    account_list.append(account)
    return account_list


def rem_account(account_list, account_number):
    for i in range(len(account_list)):
        if account_list[i]['account_number'] in account_list:
            del account_list[i]
    return account_list


def save_account(account_list):
    account_file = open("accounts.txt", "a")
    for account in account_list:
        print(account["account_owner"], account["account_number"], account["account_balance"], sep=",", file=account_file)
    account_file.close()


def menu():
    print("0 - Exit")
    print("1 - Display accounts owners")
    print("2 - Add account")
    print("3 - Remove account by owner")
    print("4 - Save account information to file")
    print("5 - Load student information from file")
    print("6 - Display menu")


def run():
    run_program = True
    account_list = []
    menu()
    print("\nList is empty by default, to load accounts select option 5")
    while run_program is True:
        invalid_option = False
        option = input("\nSelect a menu option: ")
        if option.isdigit():
            option = int(option)

            if option == 0:
                run_program = False
                print("Goodbye!")
            elif option == 1:
                get_all()
            elif option == 2:
                name = input("Who's the owner of the account? ")
                number = input("Enter the " + name + "'s account number: ")
                balance = input("What's the balance of the account? ")
                add_account(account_list, name, number, balance)
            elif option == 3:
                name = input("Enter the number of the account you want to remove: ")
                rem_account(account_list, name)
            elif option == 4:
                save_all(account_list)
            elif option == 5:
                account_list = read_account()
            elif option == 6:
                menu()
            else:
                invalid_option = True
            if invalid_option:
                print("Invalid Option")


run()
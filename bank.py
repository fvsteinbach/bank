from os import sep


account_list = []

def get_all():
    account_list = []
    with open('accounts.txt', 'r') as accounts:
        line = accounts.readline()
        while (line != ''):
            line = line.strip('\n').split(',')
            account_owner = line[0]
            account_number = int(line[1])
            account_balance = float(line[2])
            account = [account_owner, account_number, account_balance]
            account_list.append(account)
            line = accounts.readline()
    return account_list


def save_all(list):
    with open('accounts.txt', 'w') as accounts:
        for account in list:
            accounts.write(f'{account[0]}, {int(account[1])}, {float(account[2])}')

def add_account(account_list):
    save_all(account_list)
    with open('accounts.txt', 'a') as accounts:
        account_list = get_all()
        account_owner = str(input("What your full name? "))
        account_number = int(input('What account number you want? '))
        account_balance = float(input('How much will be your first deposit? '))
        new_account = [account_owner, account_number,  account_balance]
        account_list.append(new_account)
        print(account_list)
        for account in account_list:
            accounts.append(f'{account[0]}, {int(account[1])}, {float(account[2])}')
    return account_list

def display_accounts(account_list):
    for account in account_list:
        print(f'The account number is: {account[1]}')

def menu():
    print("0 - Exit")
    print("1 - Display accounts owners")
    print("2 - Add account")
    print("3 - Remove account by number")
    print("4 - Save account information to file")
    print("5 - Load student information from file")
    print("6 - Display menu")


def run():
    frango = get_all()
    account_list = frango
    menu()
    print("\nList is empty by default, to load accounts select option 5")
    while True:
        option = input("\nSelect a menu option: ")
        if option.isdigit():
            option = int(option)

            if option == 0:
                save_all(account_list)
                print("Goodbye!")
                break
            elif option == 1:
                display_accounts(account_list)
            elif option == 4:
                save_all(account_list)
            elif option == 5:
                account_list = get_all()
            elif option == 4:
                menu()
            elif option == 2:
                add_account(account_list)
            if option != 0 and option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
                print("\nInvalid Option\n")
                menu()
run()
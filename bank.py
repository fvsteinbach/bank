from email import message


account_list = []

#opens the file and updates the account_list list with the data on the txt file

def get_all():
    account_list = []
    with open('accounts.txt', 'r') as accounts:
        line = accounts.readline()
        while (line != ''):
            line = line.strip('\n').split(';')
            account_owner = line[0]
            account_number = int(line[1])
            account_balance = float(line[2])
            account = [account_owner, account_number, account_balance]
            account_list.append(account)
            line = accounts.readline()
    return account_list

#
def display_accounts(account_list):
    for account in account_list:
        print(f'The account number is: {account[1]}')


def accounts_over_100(account_list):
    for account in account_list:
        account_balance = account[2]
        if account_balance > 100:
            print(account)

#function that only runs when the program ends. It opens the txt file, gets the list of accounts and writes
def save_all(account_list):
    with open('accounts.txt', 'w') as accounts:
        for account in account_list:
            accounts.write(f'{account[0]}; {int(account[1])}; {float(account[2])}\n')


def add_account(account_list):
    while True:
        account_owner = str(input("What is your full name? ")).strip()
        if ' ' in account_owner:
            break
        print('We need your first and second name, try again')
    while True:
        account_number = int(input('What account number you want? '))
        acc_numbers = get_acc_numbers(account_list)
        if account_number not in acc_numbers:
            break
        print("This account in already being used, please try again!")
    while True:
        account_balance = float(input('How much will be your first deposit? '))
        if account_balance > 0:
            break
        print('Your first deposit must be more than U$0')
    new_account = [account_owner, account_number,  account_balance]
    account_list.append(new_account)
    return account_list


def get_acc_numbers(account_list):
    acc_numbers = []
    for account in account_list:
        acc_numbers.append(int(account[1]))
    print(acc_numbers)
    return acc_numbers


def remove_account(account_list):
    while True:
        index = get_index(account_list)
        if index != -1:
            print('Confirm your account number: ')
            balance = get_balance(account_list)
            if balance <= 0:
                del(account_list[index])
                print('Account deleted')
                break
            print('You still have money in your account, you must withdraw it in order to delete the account.')
            break
        print('Account not found, try again!')
    return account_list


def get_number():
    acc_number = int(input('Enter the Account Number: '))
    return acc_number


def get_index(account_list):
    index = 0
    acc_number = get_number()
    for account in account_list:
        if account[1] == acc_number:
            return index
        index += 1
    if account_list == []:
        print("No accounts were found. Try to add one first.")
    return -1


def get_balance(account_list):
    while True:
        index = get_index(account_list)
        if index != -1:
            account = account_list[index]
            balance = account[2]
            print(f"Your balance is U$D{balance} Sr. {account[0]}")
            return balance
        print('Invalid account, try again!')


def get_operation():
    operation = int(input("0 to get back to menu - 1 to make a withdraw - 2 to make a deposit:\n "))
    return operation


def get_withdraw():
    withdraw = float(input("How much do you want to withdraw? "))
    return withdraw


def get_deposit():
    deposit = int(input("How much do you want to deposit? "))
    return deposit


def get_message(message):
    user_input = int(input(message))
    return user_input

#Function that uses the index of the account provided, in the account list, and changes the 3º position aka balance of the list aka account to the new balance.
def change_balance(account_list):
    while True:
        index = get_index(account_list)
        if index != -1:
            operation = get_operation()
            account = account_list[index]
            if operation == 0:
                menu()
                break
            if operation == 1:
                balance = get_balance(account_list)
                withdraw = get_withdraw()
                if withdraw < balance:
                    make_withdraw(balance, withdraw, account)
                    return account_list
            if operation == 2:
                balance = get_balance(account_list)
                deposit = get_deposit()
                make_deposit(account, deposit, balance)
                return account_list
            print('Invalid option, Try Again')
        print('Invalid account')
    operation = get_operation()

#function that removes the 3º element on the list aka as balance, and then adds a new element also on the 3º position with the new balance
def make_deposit(account, deposit, balance):
    new_balance = balance + deposit
    account.pop(2)
    account.insert(2, new_balance)
    print(account)
    return account_list


def make_withdraw(balance, withdraw, account):
    new_balance = balance - withdraw
    account.pop(2)
    account.insert(2, new_balance)
    return account_list


def menu():
    print("0 - Exit")
    print("1 - Display accounts numbers")
    print("2 - Add account")
    print("3 - Remove account by number")
    print("4 - Change balance")
    print("5 - Display current balance")
    print("6 - Display menu")


def menu_reports():
    print("1 - Display all accounts")
    print("2 - Display accounts with over U$D100 of balance")


def run():
    account_list = get_all()
    menu()
    while True:
        option = input("\nSelect a menu option: ")
        if option.isdigit():
            option = int(option)
            if option == 0:
                save_all(account_list)
                print("Goodbye!")
                break
            elif option == 1:
                menu_reports()
                report = input("What reports do you wanna see? ")
                if report.isdigit():
                    report = int(report)
                    if report == 1:
                        display_accounts(account_list)
                    elif report == 2:
                        accounts_over_100(account_list)
                    elif option != 1 and option != 2:
                        print("\nInvalid Option\n")
            elif option == 2:
                add_account(account_list)
            elif option == 3:
                remove_account(account_list)
            elif option == 4:
                change_balance(account_list)
            elif option == 5:
                get_balance(account_list)
            elif option == 6:
                menu()
            elif option == 7:
                get_acc_numbers(account_list)
            elif option == 8:
                get_message('Type in your account number')
            else:
                print("\nInvalid Option\n")
                menu()


run()
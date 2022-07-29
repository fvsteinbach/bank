account_list = []
acc_index = 0

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


def display_accounts(account_list):
    for account in account_list:
        print(f'The account number is: {account[1]}')


def save_all(account_list):
    with open('accounts.txt', 'w') as accounts:
        for account in account_list:
            accounts.write(f'{account[0]}; {int(account[1])}; {float(account[2])}\n')


def add_account(account_list):
    account_owner = str(input("What your full name? "))
    if ' ' not in account_owner:
        print('We need your first and second name, try again')
        account_owner = str(input("What's your full name? ")).strip()
    account_number = int(input('What account number you want? '))
    account_balance = float(input('How much will be your first deposit? '))
    if account_balance < 0:
        print('Your first deposit must be more than U$0')
        account_balance = float(input('How musch will be your first deposit? '))
    new_account = [account_owner, account_number,  account_balance]
    account_list.append(new_account)
    print(account_list)
    save_all(account_list)
    return account_list


def remove_account(account_list):
    index = 0
    acc_number = get_number()
    while index < len(account_list):
        for account in account_list:
            if acc_number in account:
                del(account_list[index])
            index = index + 1
    save_all(account_list)
    return account_list


def get_number():
    acc_number = int(input('Enter the Account Number or Press 0 to go back to menu: '))
    return acc_number

def index(account_list):
    index = 0
    acc_number = get_number()
    for account in account_list:
        if account[1] == acc_number:
            print(account_list[index])
            return index
        index += 1
    return -1


def menu():
    print("0 - Exit")
    print("1 - Display accounts owners")
    print("2 - Add account")
    print("3 - Remove account by number")
    print("4 - Change balance")
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
            elif option == 2:
                add_account(account_list)
            elif option == 3:
                remove_account(account_list)
            elif option == 4:
                index(account_list)
            elif option == 5:
                account_list = get_all()
            elif option == 6:
                menu()
            if option != 0 and option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6:
                print("\nInvalid Option\n")
                menu()


run()
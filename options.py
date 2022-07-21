def readAccount():
    accountList = []
    accountFile = open("accounts.txt", "r")
    for line in accountFile:
        line = line.rstrip("\n")
        line = line.split(",")
        accountList.append({"account_owner" : line[0], "account_number" : line[1], "account_balance" : line[2]})
    accountFile.close()
    return accountList


def displayAccounts(accountsList):
    for account in accountsList:
        print(account["account_number"])


def addAccount(accountlist, account_owner, account_number, account_balance):
    account = {"account_owner" : account_owner, "account_number" : account_number, "account_balance" : account_balance}
    accountlist.append(account)
    return accountlist

def rem_account(accountList, account_owner):
    index = 0
    removeIndex = -1
    while index < len(accountList):
        if accountList[index]["account_owner"] == account_owner:
            removeIndex = index
            index = len(accountList)
        index = index + 1
    if removeIndex >= 0:
        del(accountList[removeIndex])
    return accountList


def saveAccount(accountList):
    accountFile = open("accounts.txt", "a")
    for account in accountList:
        print(account["account_owner"], account["account_number"], account["account_balance"], sep=",", file=accountFile)
    accountFile.close()


def menu():
    print("0 - Exit")
    print("1 - Display accounts owners")
    print("2 - Add account")
    print("3 - Remove account by owner")
    print("4 - Save account information to file")
    print("5 - Load student information from file")
    print("6 - Display menu")


def run():
    runProgram = True
    accountList = []
    menu()
    print("\nList is empty by default, to load accounts select option 5")
    while runProgram is True:
        invalidOption = False
        option = input("\nSelect a menu option: ")
        if option.isdigit():
            option = int(option)

            if option == 0:
                runProgram = False
                print("Goodbye!")
            elif option == 1:
                displayAccounts(accountList)
            elif option == 2:
                name = input("Who's the owner of the account? ")
                number = input("Enter the " + name + "'s account number: ")
                balance = input("What's the balance of the account? ")
                addAccount(accountList, name, number, balance)
            elif option == 3:
                name = input("Enter the name of the account you want to remove")
                rem_account(accountList, name)
            elif option == 4:
                saveAccount(accountList)
            elif option == 5:
                accountList = readAccount()
            elif option == 6:
                menu()
            else:
                invalidOption = True
            if invalidOption:
                print("Invalid Option")

run()

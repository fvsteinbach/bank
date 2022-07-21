def readAccountNumber():
    accountList = []
    accountFile = open("accounts.txt", "r")
    for line in accountFile:
        line = line.rstrip("\n")
        line = line.split(",")
        accountList.append({"account_number" : line[0], "account_owner" : line[1], "account_balance" : line[2]})
    accountFile.close()
    return accountList


def displayAccounts(accountsList):
    for account in accountsList:
        print(account["account_number"])


def addAccount(accountlist, account_number, account_owner, account_balance):
    account = {"account_number" : account_number, "account_owner" : account_owner, "account_balance" : account_balance}
    accountlist.append(account)
    return accountlist

def remAccount(accountList, account_number)
    index = 0
    removeIndex = -1
    while index < len(accountList):
        if accountList[index]["account_number"] == account_number:
            removeIndex = index
            index = len(accountList)
        index = index + 1
    if removeIndex >= 0:
        del(accountList[removeIndex])
    return accountList


def saveAccount(accountList):
    accountFile = open("accounts.txt", "a")
    for account in accountList:
        print(account["account_number"], account["account_owner"], account["account_balance"], sep=",", file=accountFile)
    accountFile.close()
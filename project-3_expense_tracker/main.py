# tid,item name,category,spent
from tabulate import tabulate
from termcolor import colored
transactions = [['T01','apple','food',100],
         ['T02','jeans','clothes',1000],
         ['T03','hair cut','saloon',200]]
tno = 4
#Create transaction
def takeInput():
    global tno
    tid = "T0"+str(tno)
    tno = tno+1
    item = input("Enter the item name: ")
    category = input("Enter the category name: ")
    spent = int(input("Enter the amount spent: "))
    transaction = [tid,item,category,spent]
    transactions.append(transaction)
    return transaction

#Read transactions
def Display():
    headers = ["Transaction id","Item name","category","Amount Spent"]
    print(tabulate(transactions,headers=headers,tablefmt="grid"))

def getTransaction(tid):
    for i in range(len(transactions)):
        if tid in transactions[i]:
            return i
    return -1

def printMessage(message):
    print("Successfully, ",message)


#update transactions
def Update():
    tid = input("Enter the transaction id(T0xx):")
    rindex = getTransaction(tid)
    if rindex >=0:
        print("Which detail you want to change: ")
        print("1.Item name\t2.Category\t3.Ammount Spent")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                iname = input("Enter the item name: ")
                transactions[rindex][1] = iname
                printMessage("Updated item name in "+tid)
            case 2:
                icat = input("Enter the category name: ")
                transactions[rindex][2] = icat
                printMessage("Updated category name in "+tid)
            case 3:
                iamo = int(input("Enter the Amount Spent: "))
                transactions[rindex][3] = iamo
                printMessage("Updated amount in  "+tid)
            case _:
                print("Invalid choice try agian")
    else:
        print("Transaction with ",tid," is not found")

def Delete():
    tid = input("Enter the transaction id(T0xx):")
    rindex = getTransaction(tid)
    if rindex >=0:
        deleted_data = transactions.pop(rindex)
        printMessage(f"Transaction {deleted_data[1]}({deleted_data[0]}) is deleted")
    else:
        print("Transaction with ",tid," is not found")

def generateSummary():
    summary = {}
    total = 0
    for transaction in transactions:
        if transaction[2] in summary:
            summary[transaction[2]] += transaction[3] 
        else:
            summary[transaction[2]] = transaction[3] 
        total += transaction[3]
    summary["Total Spent"] = total
    return summary

def printSummary():
    summary = generateSummary()
    total = summary["Total Spent"]
    print("#"*15+" Expenditure Summary "+"#"*15)
    for category,amount in summary.items():
        if category == "Total Spent":
            print(f"{category}:{amount}")
        else:
            poi = ((amount)/total)*100
            if poi >= 30:
                colored_amount = colored(f'{amount}',"red")
            else:
                colored_amount = colored(f"{amount}","green")
            print(f"{category}:{colored_amount}")
    print("#"*50)


def main():
    print("Welcome to Expense tracker program created by Sharukh Khan")
    while True:
        print("Choose one option:")
        print("1.Insert\t2.Display\t3.Update\t4.Delete")
        print("5.Summary\t6.Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:takeInput()
            case 2:Display()
            case 3:Update()
            case 4:Delete()
            case 5:printSummary()
            case 6:
                print("Closing the programm....")
                return
            case _:
                print("Invalid option, try again")

main()
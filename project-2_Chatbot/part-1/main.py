def chatbot(username):
    while True:
        print("#"*30)
        print(f"1.what is the username?")
        print(f"2.dondakay bendakay ")
        print(f"3.cococola pepsi ")
        request = int(input("Enter your choice: "))
        
        match request:
            case 1:
                print(f"Your {username}")
            case 2:
                print(f"Anupuma na gundekay")
            case 3:
                print(f"Ballay babu sexy")
            case _:
                print("Invalid option")
        cont = input("Do you want to continue the chat?[y/n] : ")
        if(cont == 'n'):
            print("Thankyou!!")
            break

def main():
    username="sharukh"
    print(f"welcome {username} how can i help you?")
    chatbot(username)
    
main()
from helpers import greet_user

def main():
    name = input("What's your name? ")
    message = greet_user(name)
    print(message)

if __name__ == "__main__":
    main()

    #test change
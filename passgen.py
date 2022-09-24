import random


def passgen():
    print("-" * 60)
    print(" --- Passgen --- ")
    print("-" * 60)
    
    chars = ""
    size = int(input("[1] => Enter password length: "))
    lowerCase = input("[2] => Allow lower case ? [Yes/No] ")
    upperCase = input("[3] => Allow upper case ? [Yes/No] ")
    numbers = input("[4] => Allow numbers ? [Yes/No] ")
    special = input("[5] => Allow special characters ? [Yes/No] ")
    
    if numbers.lower() == "y" or numbers.lower() == "yes": chars = chars + "0123456789"
    if special.lower() == "y" or special.lower() == "yes": chars = chars + "!?@#$%^&+-=*()[]<>"
    if lowerCase.lower() == "y" or lowerCase.lower() == "yes": chars = chars + "abcdefghijklmnopqrstuvwxyz"
    if upperCase.lower() == "y" or upperCase.lower() == "yes": chars = chars + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if chars != "" and size != 0:
        characters = list(chars)
    
        print("-" * 60)
        
        random.shuffle(characters)
        
        password = []
        
        for i in range(size):
            password.append(
                random.choice(characters)
            )
        
        random.shuffle(password)
        print("".join(password))
        print("-" * 60)
    else:
        print("-" * 60)
        print("[!] => Error: the parameters is invalid")
        
        passgen()


passgen()

import random


def passgen():
    print("-" * 60)
    print(" --- Passgen --- ")
    print("-" * 60)
    
    chars = "abcdefghijklmnopqrstuvwxyz"
    size = int(input("[1] => Enter password length: "))
    upperCase = input("[2] => Upper case ? [Yes/No] ")
    numbers = input("[3] => Numbers ? [Yes/No] ")
    special = input("[4] => Special characters ? [Yes/No] ")
    
    if numbers.lower() == "y" or numbers.lower() == "yes": chars = chars + "0123456789"
    if special.lower() == "y" or special.lower() == "yes": chars = chars + "!?@#$%^&+-=*()[]<>"
    if upperCase.lower() == "y" or upperCase.lower() == "yes": chars = chars + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
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


passgen()

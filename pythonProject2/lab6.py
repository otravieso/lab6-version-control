def encode(password):
    e_pass = 0
    new_password = ""
    for x in range(0, len(password)):
        e_pass = int(password[x]) + 3
        if e_pass == 10:
            e_pass = 1
        elif e_pass == 11:
            e_pass = 2
        elif e_pass == 12:
            e_pass = 3
        new_password = new_password + str(e_pass)
    return new_password


while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    choice = int(input("Please choose an option: "))
    if choice == 1:
        password = str(input("Please enter your password to encode: "))
        enc_pass = encode(password)
        print("Your password has been encoded and stored!\n")
    elif choice == 2:
        print(f'The encoded pass word is {enc_pass}, and the original password is {password}.\n')
    elif choice == 3:
        quit()



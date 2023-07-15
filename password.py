# Originally written by Michael Jagiello, included main function and encoding
# imports

# define variable(s)
password = 0  # should not be in here once decode is implemented
encoded_pw = 0


# define function(s)
def encode_password(input_password):  # shifts all digits 3 numbers up
    temp_list = [*input_password]
    encoded = 0
    for i in range(len(temp_list)):
        temp_value = int(temp_list[i]) + 3
        if temp_value >= 10:
            temp_value -= 10
        temp_list[i] = temp_value
        encoded = ''.join(map(str, temp_list))
    return int(encoded)


# def decode_password():  # shifts all digits 3 numbers down
#    exit()


if __name__ == '__main__':  # required if main
    while True:
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit")  # print menu
        print("Please enter an option: ")
        option = int(input())
        if option == 1:  # encode inputted password
            print("Please enter your password to encode: ")
            pw_input = input()
            password = pw_input
            encoded_pw = encode_password(pw_input)
            print("Your password has been encoded and stored!")
        elif option == 2:  # print encoded password and original password
            print("The encoded password is " + str(encoded_pw) +
                  ", and the original password is " + str(password) + ".")
            # the original password should not be stored, only the encoded password
            # replace the password being stored with decode password function
        elif option == 3:  # quit program
            break
        else:  # because why not
            print("invalid")
            break

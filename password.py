# Originally written by Michael Jagiello, included main function and encoding
# import(s)

# define variable(s)
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


def decode(encoded):  # shifts all digits 3 numbers down
    decoded = ''
    encoded_str = str(encoded)
    for i in range(len(encoded_str)):
        decoded = decoded + str((int(encoded_str[i])-3) if (int(encoded_str[i])-3 >= 0) else (int(encoded_str[i])+7))
    return decoded


if __name__ == '__main__':  # required if main
    while True:
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit")  # print menu
        print("Please enter an option: ")
        option = int(input())
        if option == 1:  # encode inputted password
            print("Please enter your password to encode: ")
            pw_input = input()
            encoded_pw = encode_password(pw_input)
            print("Your password has been encoded and stored!")
        elif option == 2:  # print encoded password and original password
            print(f"The encoded password is {str(encoded_pw)}, and the original password is {decode(encoded_pw)}.")
        elif option == 3:  # quit program
            break
        else:  # because why not
            print("invalid")
            break

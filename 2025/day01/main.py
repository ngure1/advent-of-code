file_path = "input.txt"
'''
    * Safe starts at 50
    * If rotation is L and rotation is > n use the remainder(100-remainder) else use the rotation(n-rotation)
    * Alternatively we could always do (n-rotation) and if it is -ve add 100 to it
    * If rotation is R just add the rotation to n and mod 100 to find the new number
    * Maintain a count of the number of times the combination leads us to 0
    * Rembember to mod rotation by 100 to get rid of extra cycles ie (920) is just (20 which is 920 mod 100)
'''
def get_password_one():
    # count for the number of times we get 0(password)
    password = 0
    dail = 50
    # open the input file and process instructions line by line
    try:
        with open(file_path,"r") as file:
            for line in file:
                num = int(line[1:]) % 100
                direction = line[0].upper()
                if direction == "L":
                    dail -= num
                    if dail < 0:
                        dail += 100
                else:
                    dail += num
                    dail %= 100                    
                
                if dail == 0:
                    password += 1
    except Exception as e:
       print("Something went wrong: ",e)
    
    return password

'''
    * Safe starts at 50
    * If rotation is L and rotation is > n use the remainder(100-remainder) else use the rotation(n-rotation)
    * Alternatively we could always do (n-rotation) and if it is -ve add 100 to it
    * If rotation is R just add the rotation to n and mod 100 to find the new number
    * Maintain a count of the number of times the combination passes through (incliding landing) 0
    * Rembember to mod rotation by 100 to get rid of extra cycles ie (920) is just (20 which is 920 mod 100)
    * for extra cycles add them to the password
'''
def get_password_two():
    # count for the number of times we get 0(password)
    password = 0
    dail = 50
    # open the input file and process instructions line by line
    try:
        with open(file_path,"r") as file:
            for line in file:
                line_num = int(line[1:])
                # adding extra cycles
                password += line_num // 100
                num = line_num % 100
                direction = line[0].upper()
                if direction == "L":
                    prev_dail = dail
                    dail -= num
                    if dail < 0:
                        # To avoid over counting when starting from 0 and going backwards(edgest of edge cases)
                        if prev_dail > 0:
                            password += 1
                        dail += 100
                else:
                    dail += num
                    if dail > 100:
                        password += 1 
                    dail %= 100                    
                
                if dail == 0:
                    password += 1
    except Exception as e:
       print("Something went wrong: ",e)
    
    return password
    
if __name__ == "__main__":
    print(get_password_one())
    print(get_password_two())

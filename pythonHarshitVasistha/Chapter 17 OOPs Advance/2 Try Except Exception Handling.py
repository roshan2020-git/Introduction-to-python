# Exception Handling
# (try except) , (else  finally)
# Execption are those error which comes into picture during execution
# what if we put age as seven not 7
while True:
    try: # under try those code part should come where exception can happen
        age = int(input("Enter your age "))
        # print(f"user input {age}")
        # print("some codes to be written")
        # break

    except ValueError: # if the error is ValueError then this block of code will excecute
        print("Invalid Input !!! Please input an integer value   ")
    except:
        print('Unexpected Error .....')
    else: # this block runs when there is no error and try block has been executed successfully
        # in else block we wrote those statment which we want to do after getting valid inputs
        # else block is used to enhance code readibility 
        print(f"user input {age}")
        print("some codes to be written")
        break

    finally:# this section code will execute everytime whether an error occure or not
        print("code writeen in finally block will execute everytime ")
        print("code is in finally block .....")



if age<18:
    print("you can\'t play this game ")
else:
    print('You can play this game ')


'''
if we enter valid input the code will execute without any error 
if we input invalid input there will be an error at that age so except block will run
'''


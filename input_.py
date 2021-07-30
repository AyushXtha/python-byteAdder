#module for taking input from user and checking its validity
num1=0
num2=0
pos=""

def inputnum(): #function for taking input from user
    global num1 #global used to access and modify variable outside of function
    global num2
    global pos

    pos="first"
    num1 = check(num1)
   
    pos="second"
    num2 = check(num2)
    
   

def check(num): #function for checking its validity   
    continue_=True
    while continue_:
        try: #checking for exception
             while continue_:
                num = int(input(f"Enter {pos} number between 0 and 255:"))#asking user for input
                num=int(num)
                
                if (num>=0 and num<=255):#checking if the input lies in range of 0 and 255
                    return num
                    break #breaking loop if num is in range
                else:
                    print("ERROR:OUT OF RANGE! TRY AGAIN.\n")#error message for out of range values
                    
                    
             break #breaking loop if input is valid
    
        except:
            print("Invalid Input! TRY AGAIN\n")#error message for invalid input
            





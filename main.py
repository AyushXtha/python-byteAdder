#main module used to run the code

#importing codes from other modules
import input_
import convert
import sum_

run=True
while run:

    input_.inputnum() #calling inputnum() function from input module

    """converting input num1 from input module to binary with
    convert_to_binary() function from convert module"""
    bnum1=convert.convert_to_binary(input_.num1)
    bnum2=convert.convert_to_binary(input_.num2)

    #displaying the binary numbers to user
    print(f"\nBinary form of first number is {bnum1}")
    print(f"Binary form of second number is {bnum2}")

    #calling sum() function from sum module to add binary numbers bnum1 and bnum2
    totalsum = sum_.sum(bnum1,bnum2)

    if int(totalsum)>11111111:
        #displaying errors if total sum is greater than 9 bits
        print(f"Bit Overflow: Total sum {totalsum} is greater than 8 bits. ")
    else:
        #displaying total sum to user
        print("\nThe sum is "+totalsum)

    #asking user to quit
    quit_=input("\nDo you want to quit? [Y/N]: ")
    quit_=quit_.lower()#converting quit_ to lower case

    #quiting the program if the user inputs "y" or "yes"
    if (quit_=="y" or quit_=="yes"):
        break 



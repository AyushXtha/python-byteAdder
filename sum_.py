#module to sum binary numbers
def sum(n1,n2):
    
    #changing the binary numbers 8bit by adding aditional 0s to its front
    a = ("0"*(8-len(n1)))+n1
    b = ("0"*(8-len(n2)))+n2
    totalsum=""
    carry=0

    for n in range (-1,-9,-1):#for loop accessing values from last term

        #using XOR operation to find the sum of a bit
        sum_=(int(a[n])^int(b[n])^carry)
        #concatinating sum of a bit to totalsum
        totalsum=str(sum_)+totalsum

        '''determining carry over
        assigning carry to 1 if sum of bits and carry is greater than 1'''
        if (carry+int(a[n])+int(b[n]))>1:
             
            carry=1
        else:
            carry=0
            
    #concatinating 1 to totalsum if carry obtained at end of loop is 1
    if carry==1:            
        totalsum=(str(carry)+totalsum)

    return (totalsum)

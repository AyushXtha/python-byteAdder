#module for converting decimal into binary

def convert_to_binary(num):
    #Assigning empty string to converted
    converted="" 
    continue_ = True
    
    while continue_:
        
        if (num%2==0):
            #concatinating 0 in converted if num is divisible by 2
           converted = "0"+converted
        else:
            #concatinating 1 in converted if num is not divisible by 2
            converted = "1"+converted
            
        num= int(num/2) #dividing num by 2 for next cycle

        #breaking loop if num is 0 or 1
        if num==0:
            
            break
        elif num==1:
            #concatinating carryover 1 to MSB(most significant bit) if num is 1 
            converted = "1"+converted
            break
    
    return converted 

    
    
        
        


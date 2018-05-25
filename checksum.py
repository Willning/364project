# -*- coding: utf-8 -*-
def hextet_complement(x):   
    mask = 0xffff #8 bitmask        
    out = bin(~x&mask)
    return out

    


def internet_checksum(data, total=0x0):
    '''
    Internet Checksum of a bytes array.
    Further reading:
    1. https://tools.ietf.org/html/rfc1071
    2. http://www.netfor2.com/checksum.html
    
    '''
    
    sum = 0
    
    count = 0
    while count < len(data):
        
        tempA = bin(data[count])[2:]        
        tempB =bin(data[count+1])[2:]        
        while len(tempA)<8:
            tempA ="0"+tempA
        while len(tempB)<8:
            tempB="0"+tempB
            
        number = tempB + tempA        
               
        new = int(number,2)        
        sum +=new                
        count+=2
        
    sum = sum %0xffff   
    
    int_checksum = int(hextet_complement(sum)[2:],2)
         
       
    return int_checksum

# -*- coding: utf-8 -*-
from assignment import hextet_complement


def internet_checksum(data, total=0x0):
    '''
    Internet Checksum of a bytes array.
    Further reading:
    1. https://tools.ietf.org/html/rfc1071
    2. http://www.netfor2.com/checksum.html
    
    '''
    
    total = 0
    
    for element in data:
        total = total + element
        if total>0xffff: #if overflow
            total = total%0xffff
                        
   
    checksum = hextet_complement(total)
    
    return checksum
    


data = [0x0001, 0xf203, 0xf4f5, 0xf6f7]


print(internet_checksum(data))


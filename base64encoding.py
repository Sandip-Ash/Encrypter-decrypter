import math
from time import sleep

def convert(arr):
    m=1
    bin = 0
    for i in range(len(arr)-1,-1,-1):
        bin = bin + arr[i]*m
        m = m*10 
    # print(bin)
    return bin
    
    
def Bin_To_Dec(n):
    # n= int(input("Enter a number: "))
    dec = 0
    i = 0
    while (n!=0):
        rem = n % 10
        n = n // 10
        dec = dec + rem * pow(2, i)
        i = i+1
    return(dec)
    # print("Decimal value: ",dec)                                                  #PRINT STATEMENT
    
    
def DEC_TO_BIN(n):
    s=7
    arr = [0,0,0,0,0,0,0,0]
    while n>0:
        d=n%2
        arr[s] = d
        s = s-1
        n=n//2
    # print (arr)
    return arr
    

def base64_encoding(n):
    d1 = {0 :'A', 1 :'B', 2 :'C', 3 :'D', 4 :'E', 5 :'F', 6 :'G', 7 :'H', 8 :'I', 9 :'J', 10 :'K', 11 :'L', 12 :'M', 13 :'N', 14 :'O', 15 :'P', 16 :'Q', 17 :'R', 18 :'S', 19 :'T', 20 :'U', 21 :'V', 22 :'W', 23 :'X', 24 :'Y', 25 :'Z', 
        26 :'a', 27 :'b', 28 :'c', 29 :'d', 30 :'e', 31 :'f', 32 :'g', 33 :'h', 34 :'i', 35 :'j', 36 :'k', 37 :'l', 38 :'m', 39 :'n', 40 :'o', 41 :'p', 42 :'q', 43 :'r', 44 :'s', 45 :'t', 46 :'u', 47 :'v', 48 :'w', 49 :'x', 50 :'y', 51 :'z', 
        52 :'0', 53 :'1', 54 :'2', 55 :'3', 56 :'4', 57 :'5', 58 :'6', 59 :'7', 60 :'8', 61 :'9', 62 :'+', 63 :'/'}
    
    for i in d1:
        if n == i:
            return d1[i]
            # print(d1[i], end=' ')


#-------------------------------MAIN FUNCTION--------------------------------------#
if __name__ == '__main__':
    word = input("Enter the word or sentence: ")
    arr = []
    for i in word:
        ASCII = ord(i)
        bin = DEC_TO_BIN(ASCII)
        for j in bin:
            arr.append(j)
    # print("ASCII to Binary values: ", arr)                          #PRINT STATEMENT
    
    l = len(arr)
    # print(l)
    if l%6 != 0:
        copy = l
        while l%6 !=0:
            arr.append(0)
            l = len(arr)
    # print(l)
    # print("ASCII to Binary values: ", arr)                          #PRINT STATEMENT
    c=0
    index = 5
    a = []
    base64 = []
    
    for i in range(l-1,-1,-1):
        c = c+1
        if c == 6 or i == 0:
            # print(i)
            a.clear()
            for j in range(0,c):
                a.insert(j, arr[i+j])
                # print(arr[i+j], end=' ')
            # print("List a contains: ", a)                           #PRINT STATEMENT
            bin = convert(a)
            # print("Binary Value: ", bin)                            #PRINT STATEMENT
            base64.append(Bin_To_Dec(bin))
            c = 0
    base64.reverse()
    # print(base64)                                                     #PRINT STATEMENT
    
    for i in range(0, len(base64)):
        base64[i] = base64_encoding(base64[i])
    # print(base64)                                                     #PRINT STATEMENT

    l = len(word)
    # print(l)
    if l%3 != 0:
        # copy = l
        while l%3 !=0:
            base64.append('=')
            l = l+1
    # print(base64)
    # print(l) 
    output = ''
    for i in base64:
        output = output + i 
    print(output)
    sleep(3)
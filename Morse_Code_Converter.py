#   CONVERTS A CHARACTER TO IT'S RESPECTIVE MORSE CODE
def To_Morse(num):
    d1 = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--.."}
    d2 = {"0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"---."}
    num = num.upper()
    
    if num.isalpha() == True:
        for i in d1:
            if num == i:
                print(d1[i],end=" ")
                break
    elif num == ' ':
        print(' ')
    elif num.isdigit() == True:
        for i in d2:
            if num == i:
                print(d2[i],end=" ")
                break
    else:
        print("Wrong Input",end=" ")
        
                
                
#   CONVERTS A MORSE CODE TO IT'S RESPECTIVE ALPHABET OR NUMBER        
def From_Morse(num):
    d1 = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"---."}
    
    for i in d1:
        if num == d1[i]:
            print(i, end=" ")
            break
        # else:
        #     print("--x--",end=" ")
        

#MAIN FUNCTION        
if __name__ == '__main__':
    print("Press 1 for alphabet to morse")
    print("Press 2 for morse to alphabet")
    choice = int(input("Enter you choice: "))
    if choice == 1:
        num = input("Enter the word: ")
        for i in num:
            To_Morse(i)
    elif choice == 2:
        num = input("Enter the string: ")
        x = num.split()
        for i in x:
            From_Morse(i)
    else:
        print("Wrong Input")
        exit()
        
        
#  ... .- -. -.. -.-- 

#  ..... ....- ..--- ---.. -.... --... ..--- 
            
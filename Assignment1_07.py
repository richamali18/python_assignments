def ChkDivisible(iNo):
    if(iNo % 5 == 0):
        return True
    else:
        return False
    
def main():
    print("Enter Number :")
    ivalue = int(input())

    bRet = ChkDivisible(ivalue)

    if(bRet == True):
        print("Number is divisible by 5")
    else :
        print("Number is Not Divisible by 5")
        
if __name__ == "__main__":
    main()
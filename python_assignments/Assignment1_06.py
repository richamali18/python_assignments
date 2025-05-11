def ChkNum(iNo):
    if(iNo < 0):
        return -1
    elif (iNo > 0):
        return 1
    elif(iNo == 0):
        return 2
    
def main():
    print("Enter Number :")
    ivalue = int(input())

    iRet = ChkNum(ivalue)

    if(iRet == -1):
        print("Number is negative")
    elif(iRet == 1):
        print("Number is Positive")
    else :
        print("Number is Zero")

if __name__ == "__main__":
    main()
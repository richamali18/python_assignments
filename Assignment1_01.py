def Add(value1 , value2):
    Ans = value1 + value2 
    return Ans


def main():
    print("Enter First Number :")
    No1 = int(input())

    print("Enter Second Number :")
    No2 = int(input())

    iRet = Add(No1,No2)

    print("Addition is :",iRet)

if __name__ == "__main__":
    main()
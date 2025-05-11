def CountLength(str):
   return len(str)
    
def main():
    print("Enter String :")
    svalue = input()

    iRet = CountLength(svalue)

    print("Length is :",iRet)

if __name__ == "__main__":
    main()
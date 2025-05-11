def Display(iNo):

    while(iNo != 0):
        print("*\t")
        iNo = iNo - 1
    
def main():
    print("Enter Number :")
    ivalue = int(input())

    Display(ivalue)

if __name__ == "__main__":
    main()
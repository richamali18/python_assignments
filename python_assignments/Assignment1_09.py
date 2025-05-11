def DisplayEvenNum(iNo):

    for i in range(1, iNo + 1):
        print(2 * i)
    
def main():
    print("Enter Number :")
    ivalue = int(input())

    DisplayEvenNum(ivalue)

if __name__ == "__main__":
    main()
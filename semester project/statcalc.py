
import math


def getList():
    print("Enter a list of integers, or type q to end")
    userList = []
    check = True
    while check == True:
        option = input("Enter an integer: ")
        if option == "q":
            check = False
        else:
            try: 
                number = int(option)
            except Exception as e:
                print(e)
            else: 
                userList.append(number)
    return userList


def printMenu():
    print("choose the stat to calculate: ")
    print("1. Min")
    print("2. Max")
    print("3. Mean")
    print("4. Median")
    print("5. Clear List")

def getMean(userList):
    sum = 0
    for i in range(len(userList)):
        sum = sum + userList[i]
    return sum / len(userList)


def getMedian(userList):
    userList = sorted(userList)
    if len(userList) % 2 == 0:
        median = (userList[len(userList) // 2] + userList[len(userList) // 2 - 1]) / 2
    else:
        median = userList[len(userList) // 2]
    return median


def getMin(userList):
    min = userList[0]
    for i in range(len(userList)):
        if userList[i] < min:
            min = userList[i]
    return min


def getMax(userList):
    max = userList[0]
    for i in range(len(userList)):
        if userList[i] > max:
            max = userList[i]
    return max


def getStdDev(userList):
    mean = getMean(userList)
    n = len(userList)
    SSE = 0
    for i in range(len(userList)):
        SSE = SSE + (userList[i] - mean) ** 2
    SSE = SSE / n
    return math.sqrt(SSE)

def main():
    userList = getList()
    check = False
    while check == False:
        printMenu()
        option = input("Enter the number of the stat: ")
        if option == "1":
            print(f"The min is{getMin(userList)}")
        elif option == "2":
            print(f"The max is {getMax(userList)}")
        elif option == "3":
            print(f"The mean is {getMean(userList)}")
        elif option == "4":
            print(f"The median is {getMedian(userList)}")
        elif option == "5":
            print(f"The standard deviation is {getStdDev(userList)}")
            check = True
            break
        else:
            print("Invalid, try again.")

if __name__ == "__main__":
    main()

def getMin(userList):
    minVal = userList[0]   # candidate answer
    index = 1

    while index < len(userList):
        if userList[index] < minVal:
            minVal = userList[index]
        index += 1

    return minVal
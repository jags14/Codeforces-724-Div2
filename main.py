testCaseSize = int(input())


def isNice(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            diff = abs(array[i] - array[j])
            if diff in array:
                continue
            else:
                return False

    return True


def makeNice(array):
    b = array
    while isNice(b) != True and len(b) <= 300:
        for i in range(len(b)):
            for j in range(len(b)):
                if i == j:
                    continue
                else:
                    diff = abs(b[i] - b[j])
                    if diff in b:
                        continue
                    else:
                        b.append(diff)
    return b


for n in range(1, testCaseSize + 1):
    arraySize = int(input())
    arr = input().split()
    intArr = []
    for m in range(len(arr)):
        intArr.append(int(arr[m]))

    newArr = makeNice(intArr)
    if isNice(newArr):
        print('yes \n')
        print(len(newArr))
        print(*newArr)
    else:
        print('no')

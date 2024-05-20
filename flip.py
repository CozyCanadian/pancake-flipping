arr = [1,5,4,8,3,7,2,6] #integers represent pancakes with numbers with larger numbers representing larger pancakes (left to right is equivalent to top to bottom)

arrayLength = len(arr)
flipCount = 0

for currSize in range(arrayLength, 1, -1):
    maxIndex = 0
    for i in range(1, currSize):
        if arr[i] > arr[maxIndex]:
            maxIndex = i
    
    if maxIndex != currSize - 1:
        if maxIndex != 0:
            start = 0
            end = maxIndex
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            flipCount += 1

            print(*arr[:currSize], "|", *arr[currSize:])
        start = 0
        end = currSize - 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        flipCount += 1

        print(*arr[:currSize], "|", *arr[currSize:])


print("Sorted array:", arr)
print("Total flips:", flipCount)

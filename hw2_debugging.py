import rand

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    left = mergeSort(arr[:half])
    right = mergeSort(arr[half:])

    return recombine(left, right)

def recombine(leftArr, rightArr):
    leftIndex, rightIndex = 0, 0
    mergeArr = []

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            mergeArr.append(rightArr[rightIndex])
            rightIndex += 1

    mergeArr.extend(leftArr[leftIndex:])
    mergeArr.extend(rightArr[rightIndex:])
    
    return mergeArr


arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)

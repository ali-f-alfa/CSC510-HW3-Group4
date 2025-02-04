import rand
import os


def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    half = len(arr)//2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            rightIndex += 1
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        else:
            leftIndex += 1
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + rightIndex] = rightArr[i]
    
    for i in range(leftIndex, len(leftArr)):
        mergeArr[leftIndex + rightIndex] = leftArr[i]

    return mergeArr

arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)

def authenticate_user():
    user_input = input("Enter username: ")
    pass_input = input("Enter password: ")

    if user_input == user_input and pass_input == pass_input:
        print("Access Granted!")
    else:
        print("Access Denied!")

authenticate_user()


def delete_file():
    filename = input("Enter filename to delete: ")
    if os.path.exists(filename): 
        try:
            os.remove(filename)
            print(f"File {filename} deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")
    else:
        print("File not found.")

delete_file()

def infinite_recursion(n):
    print(n)
    return infinite_recursion(n + 1)  

infinite_recursion(1)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    return arr

nums = [5, 3, 8, 1, 2, 7]
print(bubble_sort(nums))

def divide_numbers():
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a / b)  

divide_numbers()

def unused_variables():
    x = 42  
    y = 100 

unused_variables()

import rand
import os


def mergesort(arr):
    if (len(arr) == 1):
        return arr

    half = len(arr)//2

    return recombine(mergesort(arr[:half]), mergesort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = []

    # Merge the two arrays as long as both have remaining elements
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] <= rightArr[rightIndex]:
            mergeArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            mergeArr.append(rightArr[rightIndex])
            rightIndex += 1

    # If leftArr still has elements, add them
    while leftIndex < len(leftArr):
        mergeArr.append(leftArr[leftIndex])
        leftIndex += 1

    # If rightArr still has elements, add them
    while rightIndex < len(rightArr):
        mergeArr.append(rightArr[rightIndex])
        rightIndex += 1

    return mergeArr

arr = rand.random_array([None] * 20)
arr_out = mergesort(arr)

print(arr_out)

def authenticate_user():
    user_input = input("Enter username: ")
    pass_input = input("Enter password: ")

    if user_input == user_input and pass_input == pass_input:
        print("Access Granted!")
    else:
        print("Access Denied!")




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


def infinite_recursion(n):
    print(n)
    return infinite_recursion(n + 1)  


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



def unused_variables():
    x = 42  
    y = 100 


if __name__ == '__main__':
    # Only run these if the file is executed directly,
    # NOT if it's being imported by pytest or anything else.
    authenticate_user()
    delete_file()
    infinite_recursion(1)
    unused_variables()
    divide_numbers()
    delete_file()

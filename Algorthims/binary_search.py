def binary_search(num_list,low,high,num):
    if (len(num_list) == 0):
        return 0 

    while low <= high:
        mid = (low + high)//2

        if num_list[mid] == num:
            return mid 

        elif num_list[mid] < num:
            low = mid + 1 

        else:
            high = mid - 1 

    return -1 


number = int(input("Enter the length of list :"))
num_list = []
for i in range(number):
    num_int = int(input())
    num_list.append(num_int)

low = 0 
high = len(num_list) -1 

num = int(input("Enter the requried number to get index :"))

result = binary_search(num_list,low,high,num)

if result == 0:
    print("Enter valid number if inputs in list")

elif result != -1:
     print("Number is present at index :", result)

else:
    print("Number is not present")



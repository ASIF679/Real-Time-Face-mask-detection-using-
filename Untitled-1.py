# def FindMissing_numbers(arr):
#     # Find the full range of numbers from 1 to the maximum in the array
#     full_range = set(range(1, max(arr) + 1))
#     # Find the missing numbers by subtracting the set of array elements from the full range
#     missing_numbers = full_range - set(arr)
#     # Return the missing numbers as a sorted list
#     return sorted(missing_numbers)
# # Example test case
# print(FindMissing_numbers([1, 2, 4, 7, 8, 10]))



# def FilterValueFromDic(students):
#     low_score_students = []
#     for student in students:
#         if student['score'] > 50:
#             low_score_students.append(student['name'])
    
#     return low_score_students

# # Pass the list of dictionaries when calling the function
# students_list = [
#     {"name": "Alice", "age": 20, "score": 85},
#     {"name": "Bob", "age": 22, "score": 45},
#     {"name": "Charlie", "age": 23, "score": 60},
#     {"name": "David", "age": 21, "score": 30},
#     {"name": "Eve", "age": 24, "score": 95}
# ]

# # Calling the function and passing the list
# print(FilterValueFromDic(students_list))

# def Findtarget(arr, key):
#     for i in range (0 , len(arr)):
#         for j in range(i+1 , len(arr)):
#             if arr[i] + arr[j] == key:
#              return arr[i],arr[j]
# print(Findtarget([1,2,3,4,5,6],  9))

# def CheckEvenOdd(num):
#     if num%2==0:
#         print("The number is Even")
#     else:
#         if num % 2 !=0:
#             print("The number is not even")
# CheckEvenOdd(4)
# CheckEvenOdd(5)
    
# def Findmax(num1,num2):
#     if num1 > num2:
#         print(num1, "is greater than" ,num2)
#     else:
#         print(num2 ,"is less than " ,num2)
# Findmax(8,5)


# def printNaturalNumbers():
#     for i in range(1,10+1):
#         print(i)
# printNaturalNumbers()


# def printSum(num1,num2):
#    for i in range(list(num1,num2)):
#     print(list)

# def RemoveDuplicates(list):
#    new_list=[]
#    for i in list:
#       if i not in new_list:
#          new_list.append(i)
#    return new_list
# print(RemoveDuplicates([1,2,3,4,5,1,2]))

def sumNumber(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
numbers_list = [1, 2, 3, 4, 5]  # Example list of numbers
print(sumNumber(numbers_list))

#1.  Check if year is a leap year
#Input: Year (integer)
#Output: Leap year or Not a leap year

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    else:
        return "Not a leap year"
year = int(input("Enter a year: "))
print(is_leap_year(year))

#2.	 Write a Python program to check whether the given list is sorted in ascending order or not.

#Method 1: Using a Loop
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return "Not sorted"
    return "Sorted in ascending order"
my_list = [1, 3, 5, 7]
print(is_sorted(my_list))
#Method 2: Using Python's built-in sorted()
def is_sorted(lst):
    return "Sorted in ascending order" if lst == sorted(lst) else "Not sorted"
my_list = [10, 20, 30, 25]
print(is_sorted(my_list))

#3.	Write a Python program to sort a list in ascending order without using the built-in sort() or sorted() functions.

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
my_list = [64, 25, 12, 22, 11]
sorted_list = bubble_sort(my_list)
print("Sorted list in ascending order:", sorted_list)

#4.	Input : s= ‘abc’     output:  ‘cde’

def shift_string(s):
    shifted = ""
    for char in s:
        shifted += chr(ord(char) + 2)
    return shifted
s = 'abc'
print("Output:", shift_string(s))
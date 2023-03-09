from random import randint

def bubble_sort(l): # l means list
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j+1], l[j] = l[j], l[j+1]
    
    return l


nums = [23, 1, 45, 4, 7, 7, 3, 3, 2, 4, 9]

nums2 = [randint(0, 100) for i in range(15)]

print(f"nums = {nums}")

print(f"sorted nums = {bubble_sort(nums)}")

print(f"nums2 = {nums2}")

print(f"sorted nums2 = {bubble_sort(nums2)}")

#!/usr/bin/env python3

list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
list2 = [ 'uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635' ]
list3 = [ 'uli101', 1, 'ops235', 2, 'ops335', 3, 'ops445', 4, 'ops535', 5, 'ops635', 6 ]

print(list1[0])  # First item in list1
print(list2[1])  # Second item in list2
print(list3[-1]) # Last item in list3


print(list1[0:5]) # Starting with index 0 and stopping before index 5
print(list2[2:4]) # Starting with index 2 and stopping before index 4
print(list3[3:])  # Starting with index 3 and going to the end

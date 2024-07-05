#!/usr/bin/env python3



my_number = 1000
my_list = [1,2,3,4,5]
f = open('file3.txt', 'w')
f.write(str(my_number) + '\n')
for num in my_list:
    f.write(str(num) + '\n')
f.close()

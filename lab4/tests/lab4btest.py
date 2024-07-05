#!/usr/bin/env python3

import lab4b
list1 = [1,2,3,4,5]
list2 = [2,1,0,-1,-2]
print(lab4b.join_lists(list1,list2))
# Will output [0, 1, 2, 3, 4, 5, -2, -1]
print(lab4b.match_lists(list1,list2))                                                                                                                 
# Will output [1, 2]
print(lab4b.diff_lists(list1,list2))                                                                                                                  
# Will output [0, 3, 4, 5, -2, -1]

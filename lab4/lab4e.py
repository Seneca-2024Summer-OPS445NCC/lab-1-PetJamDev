#!/usr/bin/env python3

# Author ID: pdevos

def is_digits(sobj):
    # place code here - loop through each character in sobj 
	i = 0
	while i < len(sobj):
		if '0' > sobj[i] or sobj[i] > '9':
			return False
		i += 1
	return True



if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')

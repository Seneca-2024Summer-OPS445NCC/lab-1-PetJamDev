#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: [pdevos]

def operate(number1, number2, operator):
    # Place logic in this function
	result = None
	#number1 = input("Enter the first number: ")
	#number2 = input("Enter the second number: ")
	#operator = input("Please select an operator (add, subtract, multiply, or divide): ")
	
	#If user wants to add
	if operator == 'add':
		result = int(number1) + int(number2)
	
	#If user wants to subtract
	elif operator == 'subtract':
		result = int(number1) - int(number2)

	#If user wants to multiply
	elif operator == 'multiply':
		result = int(number1) * int(number2)

	#If user wants to divide
	#elif operator == 'divide':
		#result = int(number1) / int(number2)
	else:
		result = 'Error: function operator can be "add", "subtract", or "multiply"'
	return result

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))

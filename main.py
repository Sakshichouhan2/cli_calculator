from arithmetic import *
from single_operand import *


opr_choice = input("for binary operand press 1 \ unary  operand press 2\n")

if opr_choice == "1":
	choice = input("please enter choice for performing operations press 1 for add\n press 2 for sub\n press 3 for div\n press 4 for mul\n press 5 for Exponentiation\n press 6 for modulus\n press 7 for floor_division\n")
	operand1 = int(input("enter first operation :")) 
	operand2 = int(input("enter second operation :")) 

	if choice =="1":
		z = add(operand1,operand2)
		print("{} + {} = {}".format(operand1,operand2,z))

	elif choice =="2":
		z = sub(operand1,operand2)
		print("{} - {} = {}".format(operand1,operand2,z))	

	elif choice =="3":
		z = div(operand1,operand2)
		print("{} / {} = {}".format(operand1,operand2,z))
		
	elif choice =="4":
		z = mul(operand1,operand2)
		print("{} * {} = {}".format(operand1,operand2,z)) 

	elif choice =="5":
		z = Exponentiation(operand1,operand2)
		z = print("{} ** {} = {}".format(operand1,operand2,z))

	elif choice =="6":
		z = modulus(operand1,operand2)
		z = print("{} % {} = {}".format(operand1,operand2,z))

	elif choice =="7":
		z = floor_division(operand1,operand2)
		z = print("{} // {} = {}".format(operand1,operand2,z))

	else: 
		print("Invalid Choice")
		
if opr_choice =="2":
	choice = input("please enter choice for performing operations press 1 for square\n press 2 for cube\n press 3 for square_root\n press 4 for cube_root\n press 5 for factorial\n")
	operand1 = int(input("enter first number: "))

	if choice == "1":
		z = square(operand1)
		print("square of {} = {}".format(operand1,z))

	elif choice == "2":
		z = cube(operand1)
		print("cube of {} = {}".format(operand1,z))

	elif choice == "3":
		z = square(operand1)
		print("square_root of {} = {}".format(operand1,z))

	elif choice == "4":
		z = square(operand1)
		print("scube_root of {} = {}".format(operand1,z))

	elif choice =="5":
		z = factorial(operand1)
		print("factorial of {} = {}".format(operand1,z))

	else:
		print("Invalid Choice")


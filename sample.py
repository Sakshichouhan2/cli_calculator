try:
	a = input("Enter a no.")
	b = input("Enter another no.")

	if ("." in a):
		x = float(a) 

	else :
		x = int(a)

		
	if ( "." in b):
		y = float(b)

	else :
		y = int(b)

	s1 = x+y	
	s2 = x-y
	s3 = x*y
	s4 = x/y

	print ("{} + {} = {}".format(x,y,s1))
	print ("{} - {} = {}".format(x,y,s2))
	print ("{} * {} = {}".format(x,y,s3))
	print ("{} / {} = {}".format(x,y,s4))

except TypeError:
	print ("Input given in string please provide valid inputs")

except ValueError:
	print ("Invalid number")
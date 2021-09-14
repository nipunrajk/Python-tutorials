#different ways of showing the details of  error message  in the except block
Method 1: 
	try:
	    age = int(input("Age: "))
	except ValueError as ex:
	    print("You didn't entered a valid number")
	    print(ex)
	    print(type(ex))
	else:
	    print("No exception were thrown")
	print("Execution completes")
	
Method 2:
	import sys
	try:
	    age = int(input("Age: "))
	except ValueError as ex:
	    print("You didn't entered a valid number")
	    print(sys.exc_info()[0])
	    print(type(ex))
	else:
	    print("No exception were thrown")
	print("Execution completes")
	
Method 3:
	try:
	    age = int(input("Age: "))
	except Exception as ex:
	    print("You didn't entered a valid number")
	    print(ex.__class__)
	    print(type(ex))
	else:
	    print("No exception were thrown")
	print("Execution completes")	

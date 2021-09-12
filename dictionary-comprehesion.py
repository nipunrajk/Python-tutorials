	Example 1:
	# values = {}
	# for i in range(1,11):
	#     values[i] = i*i

	values = {i:i*i for i in range(1,11)}
	print(values)

Example 2:
	#item price in dollars
	old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

	dollar_to_pound = 0.76
	new_price = {x:y*dollar_to_pound for x,y in old_price.items()}
	print(new_price)
	
Example 3:
	original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

	modified_dic = {x:y for x,y in original_dict.items() if y%2==0 }
	print(modified_dic)	
	
Example 4:
	original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

	modified_dic = {x:y for x,y in original_dict.items() if (y%2 != 0) and (y<34)}
	print(modified_dic)	

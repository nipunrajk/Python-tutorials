Example 1

	items = [
	    ("product1", 10),
	    ("product2", 9),
	    ("product3", 12)
	]

	# prices = list(map(lambda item:item[1], items))
	prices =  [item[1] for item in items]
	print(prices)

	# filtered = list(filter(lambda item : item[1] >= 10 , items))
	filtered = [item for item in items if item[1] >= 10 ]
	print(filtered)


Example 2

	# h_letters = []
	# for i in 'human':
	# h_letters.append(i)	


	h_letters = [i for i in 'human']
	print(h_letters)

Example 3

	#list = list(filter(lambda x:x%2==0,range(21)))

	list = [x for x in range(21) if x%2==0]
	print(list)
	
	
Example 4

	# list = []
	# for x in range(101):
	#     if (x %2 ==0) and (x %5 ==0):
	#         list.append(x)
	# print(list)	
	
	# result = list(filter(lambda x:x%2 == 0 and x%5 ==0, range(101)))
	# print(result)
	
	result = [x for x in range(101) if (x%2 == 0) and (x%5 ==0)]
	print(result)
	

Example 5

	# list = []
	# for i in range(11):
	#     if i %2 ==0:
	#         list.append('Even')
	#     else:
	#         list.append('odd')	

	# print(list)	
	
	# result = list(filter(lambda item:'even' if item%2==0 else 'odd', range(11)))
	
	result = ['even' if item %2 ==0 else 'odd' for item in range(11) ]
	print(result)
	
	
Example 6
	transposed = []
	matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

	for i in range(len(matrix[0])):	
	transposed_row = []

    	for row in matrix:
        transposed_row.append(row[i])
    	transposed.append(transposed_row)
	print(transposed)	
	
	matrix = [[1, 2], [3,4], [5,6], [7,8]]
	transpose = [[row[i] for row in matrix] for i in range(2)]
	print (transpose)

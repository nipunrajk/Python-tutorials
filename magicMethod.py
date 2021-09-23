__str__ Method:

	class Point:

	    def __init__(self, x, y):
		self.x = x
		self.y = y

	    def __str__(self):
		return f"({self.x}, {self.y})"

	    def draw(self):
		print(f'point ({self.x}, {self.y})')


	obj1 = Point(1, 2)
	print(str(obj1))

comparing objects: 
	class Point:

	    def __init__(self, x, y):
		self.x = x
		self.y = y

	    def __lt__(self, other):
		return self.x < other.x and self.y < other.y

	    def draw(self):
		print(f'point ({self.x}, {self.y})')


	obj1 = Point(1, 24)
	obj2 = Point(13, 2)

	print(obj1 < obj2)

Performing arithematic Operation:
	class Point:

	    def __init__(self, x, y):
		self.x = x
		self.y = y

	    def __str__(self):
		return f'{self.x, self.y}'

	    def __add__(self, other):
		return Point(self.x + other.x , self.y + other.y)

	    def draw(self):
		print(f'point ({self.x}, {self.y})')


	obj1 = Point(1, 24)
	obj2 = Point(13, 2)

	print(obj1 + obj2)


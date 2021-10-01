Example:1
	class Polygon:
	    def __init__(self, no_of_sides):
		self.n = no_of_sides
		self.sides = [0 for i in range(no_of_sides)]

	    def inputsides(self):
		self.sides = [float(input(f"Enter the sides magnitude {i + 1}: ")) for i in range(self.n)]

	    def displaysides(self):
		for i in range(self.n):
		    print(f"Sides are {i + 1}", self.sides[i])


	class Triangle(Polygon):
	    def __init__(self):
		Polygon.__init__(self, 3)

	    def area(self):
		a, b, c = self.sides
		s = (a + b + c) / 2
		area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
		print('the area of the triangle is %0.2f' % area)


	t = Triangle()
	t.inputsides()
	t.displaysides()
	t.area()


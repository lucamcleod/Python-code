class Rational:
	def __init__(self, n, d):
		self.n = n
		self.d = d

	def __add__(self, y):
		return Rational(self.n*y.d+y.n*self.d, self.d*y.d)

	def __str__(self):
		return '{}/{}'.format(self.n, self.d)

# Example
x = Rational(4, 2)
y = Rational(4, 1)

print(x+y)
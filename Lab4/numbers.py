class integer(object):
	def __init__(self, num, neg):
		self.number = num
		self.PosOrNeg = neg
	def display(self):
		print str(self.PosOrNeg) + str(self.number)
class NegativeInteger(integer):
	def __init__(self, num):
		super(NegativeInteger, self).__init__( num, "-" )
	def display(self):
		integer.display(self)
		print"i am awesome "
if __name__== "__main__":
	number = NegativeInteger(6)
	number.display()

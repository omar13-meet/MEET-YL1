def devisor(n):
	n = int(raw_input("give me a number!!"))
	x = 0
	while x != n :
		x = x+1
		if n<0:
			print "try again :("
		elif n%x == 0 :
			print x
			print "devisable"
		elif n%x != 0:
			print x
			print"isn't devisable"
if __name__ == "__main__":
	devisor(100)
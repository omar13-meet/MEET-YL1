def devisor (n):
	n = raw_input("give me a number")
	if n == str or n<0:
		print "try again"
	x = 1
	while x != n :
		x = x+1
		print x
if __name__=="__main__":
	devisor(n)

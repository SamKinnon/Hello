def announce(f):
	def wrapper():
		print("Abourt to run the function..")
		f()
		print("Done with the function.")
	return wrapper
@announce
def hello():
	print("Hello , World")
hello()
def swaplist(newlist):
	
	temp = newlist[0]
	newlist[0] = newlist[len(newlist)-1]
	newlist[len(newlist)-1] = temp
	return newlist
newlist = [12, 35, 9, 56, 24]
print (swaplist(newlist))


num = int(input("Enter a number to chech weather a prime: "))
if num > 1:
	for i in range(2,int(num/2)+1):
		if (num%i) ==0 :
			print(f"{num}: is not prime")
			break
	else:
			print(f"{num}: is prime the number we always wanted man")
else:
	print(f"{num} :  is a shit we dont want it any more please live it alone")



n = int(input("Enter a number to chech weather a prime: "))

if n > 1:
	for i in range n:
		if (n % i) == 0:
			if




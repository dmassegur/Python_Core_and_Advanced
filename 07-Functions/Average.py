def average(par1, par2) :
	avg = (par1 + par2) / 2
	print('Average of numbers %0.1f and %0.1f is: %0.1f.' %(par1, par2, avg))
	return avg   # function stops at return!!!!

x = 34
y = 35

z = average(x, y)
print('Returned value form average function: %0.1f.' %(z))
print('Returned value form average function: %0.1f.' %(average(x, y)))

average(par2=y, par1=x)
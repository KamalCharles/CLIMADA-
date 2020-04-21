def foo(val1,val2,val3,calcSum=True):
	if calcSum:
		return val1 + val2 + val3
	else:
	    return (val1 + val2 + val3)/3 

print(foo(1,2,3))	

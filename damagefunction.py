
	
def user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Sorry, must be an integer.")
            continue

        if value < 0:
            print("Sorry, must not be negative.")
            continue
        else:
            break
    return value

	
		
def damagefunc(vin = int,vhalf=int,vthresh=int):


    vin = max(vin - vthresh,0)/(vhalf - vthresh)
    vin3 = vin**3
    f = vin3/(1+vin3)

    return (f)








			





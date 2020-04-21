
	
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

	
		
def damagefunc(vin = int(user_input('Enter the maximum windgust speed: ')), 
	vhalf=int(user_input('Enter windgust speed where half the property is damaged : ')), 
        vthresh=int(user_input('Enter threshold, must be less than prior entry : '))):



    vin = max(vin - vthresh,0)/(vhalf - vthresh)
    vin3 = vin**3
    f = vin3/(1+vin3)

    print (f)

damagefunc()






			





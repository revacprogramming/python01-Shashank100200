# Functions


def computepay(hrs, rate):  
	pay = hrs*rate
	if hrs > 40:
    		extra = (hrs-40.0)*(rate * 0.5)
    		pay = pay + extra
	return pay
    
hrs = float(input("Enter Hours:"))
rate = float(input("Enter the Rate:"))
pay = computepay(hrs,rate)
print("Pay",pay)
    
              
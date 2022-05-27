# Functions


def computepay(hrs, rate):
    computepay(hrs,rate)
    return 0
    
    
hrs = float(input("Enter Hours:"))
rate = float(input("Enter the Rate:"))

if hrs > 40:
    regpay = hrs*rate
    extra = (hrs-40.0)*(rate * 0.5)
    extrapay=regpay+extra
    print("Pay",extrapay)
else:
    pay = (hrs*rate)
    print("Pay",pay)
        

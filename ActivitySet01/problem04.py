# Conditional Execution

hrs = float(input("Enter Hours:"))
rate = float(input("Enter the Rate:"))
if hrs > 40:
  regpay = hrs*rate
  extra = (hrs-40.0)*(rate * 0.5)
  extrapay=regpay+extra
  print(extrapay)
else:
  pay = (hrs*rate)
  print(pay)
        


        
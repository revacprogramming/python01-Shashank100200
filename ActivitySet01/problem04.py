# Conditional Execution

hrs = float(input("Enter Hours:"))
rate = float(input("Enter the Rate:"))
pay = hrs * rate
if hrs > 40:
  extra = (hrs-40.0)*(rate * 0.5)
  pay=pay+extra
print(pay)


        
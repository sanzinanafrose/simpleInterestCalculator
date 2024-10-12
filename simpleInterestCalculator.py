principal = int(input("Enter the amount borrowed: "))
years = float(input("Enter the period in years: "))
rate = float(input("Enter rate of interest: "))

interest = principal * years * rate /100
print("Simple interest calculated is: " + str(interest))
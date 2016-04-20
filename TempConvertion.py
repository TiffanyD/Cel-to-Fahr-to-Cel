#Celsius to Fahrenheit

operation = raw_input("Enter C for converting to Celsius or F to Fahrenheit: ")
while not (operation.upper() == "F" or operation.upper()== "C"):
	operation = raw_input("Enter C for converting to Celsius or F to Fahrenheit: ")
if operation.upper() == "F":
	num = raw_input("Enter Celsius to be converted: ")
	while num.isalpha():
		num = raw_input("Enter Celsius to be converted: ")
	num = float(num)*1.8+32
	print "The value in Fahrenheit is:"
	print num
elif operation.upper() == "C":
	num = raw_input("Enter Fahrenheit to be converted: ")
	while num.isalpha():
		num = raw_input("Enter Fahrenheit to be converted: ")
	num = (float(num)-32)*1.8
	print "The value in Celsius is:"
	print num

#Celsius to Fahrenheit

poop = raw_input("Enter C for converting to Celsius or F to Fahrenheit: ")
while not (poop.upper() == "F" or poop.upper()== "C"):
	poop = raw_input("Enter C for converting to Celsius or F to Fahrenheit: ")
if poop.upper() == "F":
	wow = raw_input("Enter Celsius to be converted: ")
	while wow.isalpha():
		wow = raw_input("Enter Celsius to be converted: ")
	wow = float(wow)*1.8+32
	print "The value in Fahrenheit is:"
	print wow
elif poop.upper() == "C":
	wow = raw_input("Enter Fahrenheit to be converted: ")
	while wow.isalpha():
		wow = raw_input("Enter Fahrenheit to be converted: ")
	wow = (float(wow)-32)*1.8
	print "The value in Celsius is:"
	print wow

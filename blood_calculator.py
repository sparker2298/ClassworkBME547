#This will be the calculator for blood values

def interface():
	print("Blood test analysis")
	keep_running = True
	
	while keep_running:
	
		print("Options:")
		print("1-HDL")
		print(" 9-Quit")
		
		choice = input("Enter your choice: ")
		
		if choice == "9": # Make sure this is a string
			keep_running = False
		elif choice == "1":
			HDL_Driver()
			
	return
		
	
def accept_input(test_name):
	entry = input("Enter the {} test Result: ".format(test_name))
	return int(entry)
	
def check_HDL(HDL_value):
	if HDL_value >= 60:
		ans = "Normal"
	elif 60 > HDL_value >= 40:
		ans = "Borderline low"
	else:
		ans = "Low"
	return ans
	
def print_result(test_name,test_value,test_class):
	out_string = "The test value of {} for {} is {}".format(test_value,test_name,test_class)
	print(out_string)

def HDL_Driver():
	HDL_value = accept_input("HDL")
	
	result = check_HDL(HDL_value)
	
	print_result("HDL", HDL_value, result)
	
interface()

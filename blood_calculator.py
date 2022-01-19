#This will be the calculator for blood values

def interface():
	print("Blood test analysis")
	keep_running = True
	
	while keep_running:
	
		print("Options:")
		print("1-HDL")
		print("2-LDL")
		print("3-TC")
		print(" 9-Quit")
		
		choice = input("Enter your choice: ")
		
		if choice == "9": # Make sure this is a string
			keep_running = False
		elif choice == "1":
			HDL_Driver()
		elif choice == "2":
			LDL_Driver()
		elif choice == "3":
			TC_Driver()
			
	return
		
	
def accept_input(test_name):
	entry = input("Enter the {} test Result: ".format(test_name))
	return int(entry)
	
def print_result(test_name,test_value,test_class):
	out_string = "The test value of {} for {} is {}".format(test_value,test_name,test_class)
	print(out_string)
	
#HDL Functions
def check_HDL(HDL_value):
	if HDL_value >= 60:
		ans = "Normal"
	elif 60 > HDL_value >= 40:
		ans = "Borderline low"
	else:
		ans = "Low"
	return ans
	
def HDL_Driver():
	HDL_value = accept_input("HDL")
	
	result = check_HDL(HDL_value)
	
	print_result("HDL", HDL_value, result)
	
#LDL Functions
def check_LDL(LDL_value):
	if LDL_value >= 190:
		ans = "Very High"
	elif 190 > LDL_value >= 160:
		ans = "High"
	elif 160 > LDL_value >= 130:
		ans = "Borderline High"
	else:
		ans = "Normal"
	return ans

def LDL_Driver():
	LDL_value = accept_input("LDL")
	
	result = check_LDL(LDL_value)
	
	print_result("LDL", LDL_value, result)
	
#Total Cholesterol Functions
def check_TC(TC_value):
	if TC_value >= 240:
		ans = "High"
	elif 240 > TC_value >= 200:
		ans = "Borderline High"
	else:
		ans = "Normal"
	return ans

def TC_Driver():
	TC_value = accept_input("TC")
	
	result = check_TC(TC_value)
	
	print_result("TC", TC_value, result)
	
interface()

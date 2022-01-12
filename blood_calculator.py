#This will be the calculator for blood values

def interface():
	print("Blood test analysis")
	keep_running = True
	
	while keep_running:
	
		print("Options:")
		print(" 9-Quit")
		
		choice = input("Enter your choice: ")
		
		if choice == "9": # Make sure this is a string
			keep_running = False
			
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
	
interface()

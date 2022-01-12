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
		
interface()

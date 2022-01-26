def add_patient(patient_name, patient_id, age):
	new_patient = [patient_name,patient_id, age, []]
	return new_patient
	
def main():
	db = []
	x = add_patient("abble baba", 234, 40)
	db.append(x)
	y = add_patient("hababa shushana", 343, 45)
	db.append(y)
	z = add_patient("pickle beut", 454, 55)
	db.append(z)
	db.append(add_patient("happy guy", 454, 55))
	
	
	#print(db[-1]) #gives you last entry from a list
	
	#print(db[0:3])#gives entries up to 3
	
	#for patient in db:
	#	for item in patient:
	#		print(item)
	
	found_patient = find_patient(db, 343)
	print(found_patient)
	
	print(db)
	
	add_test_to_patient(db, 343, "HDL", 100)
	print(db)
	return db
			
def find_patient(db,id_no):
	for patient in db:
		if patient[1] == id_no:
			return patient
			
	return
	
def add_test_to_patient(db, id_no, test_name, test_result):
	
	patient = find_patient(db, id_no);
	test_tuple = (test_name,test_result)
	
	patient[3].append(test_tuple)
	
	
def print_directory(db):
	rooms = ["Room 13", "Room 12", "room 99", "room 3"]
	for room, patient in zip(rooms, db):
		print("name: {} Room: {}".format(patient[0], room))

	
if __name__ == "__main__":
	db = main()
	print_directory(db)
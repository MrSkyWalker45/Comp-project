import random as rand


rand_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rand_numbers = ['1','2','3','4','5','6','7','8','9','10']



d = {	"Blr-Mum":900,"Blr-Del":2000,"Blr-Klt":1800,"Blr-Hyd":500,
		"Mum-Del":1200,"Mum-Klt":1700,"Mum-Hyd":700,"Del-Klt":1300,
		"Del-Hyd":1400,"Klt-Hyd":1500,"Mum-Blr":900,
		"Del-Blr":2000,"Klt-Blr":1800,"Hyd-Blr":500,
		"Del-Mum":1200,"Klt-Mum":1700,"Hyd-Mum":700,"Klt-Del":1300,
		"Hyd-Del":1400,"Hyd-Klt":1500,
}

global rail_v
global ariel_v 
global road_v


global cost_ariel_km
global cost_road_km
global cost_rail_km



isNumber = False
		

def user_input():
	global name,email_id,budget,to_place,from_place,age

	name = input("Enter your name:")

	email_id = input("Enter your email_id:")

	age = int(input("Enter your age:"))
	
	while True:
		to_place = input("Enter the place you want to travel to:")
		from_place = input("Enter the place where you are located currently:")
		if to_place == from_place:
			print("You Entererd the same place!")
			continue
		else:
			break
	budget = int(input("Enter your budget:"))


def calculate_time(ariel_v,road_v,rail_v):
	global time_ariel,time_road,time_rail
	time_ariel  = d[jry]/ariel_v 
	time_road = d[jry]/road_v
	time_rail = d[jry]/rail_v
	
	return time_ariel,time_road,time_rail
	
def cost(cost_ariel_km,cost_road_km,cost_rail_km):
	global net_ariel 
	global net_road
	global net_rail
	
	net_ariel = cost_ariel_km * d[jry]
	net_road = cost_road_km * d[jry]
	net_rail = cost_rail_km * d[jry]
	
	return net_ariel,net_road,net_rail

def pick_rand():
	global flight_number  
	global train_number
 
	flight_number=jry
	train_number=jry
	
	for j in range(2):
		flight_number+=rand.choice(rand_letters)
		flight_number+=rand.choice(rand_numbers)
	for k in range(2):
		train_number+=rand.choice(rand_letters)
		train_number+=rand.choice(rand_numbers)
	return flight_number,train_number

	
def booking_preference():
	print('Choose \'a\' for Ariel travel, \'b\' for Road travel, \'c\' for Rail travel')
	print('''Ariel Journey
	Time taken :''','hr',time_ariel,'''
	Cost of travel :''',net_ariel)

	print('''Journey by road
	Time taken :''','hr',time_road,'''
	Cost of travel :''',net_road)
	print('''Journey by rail
	Time taken :''','hr',time_rail,'''
	Cost of travel :''',net_rail)

	global preference
	perfernce = input("Enter your preference:")
	print("-"*100)
	print("From:",full_from,"\t","To:",full_to)
	print("Distance to be travelled:",d[jry],"km")
	if perfernce== "a":
		pick_rand()
		print("Time of journey:",time_ariel,"hr")
		print("Cost of journey:",net_ariel)
		print("GST",0.18 * net_ariel)
		print("Total Fare:",net_ariel*1.18)
	elif perfernce == "b":
		output()
		print("Time of journey:",time_road,"hr")
		print("Cost of journey:",net_road)
		print("GST",0.18 * net_road)
		print("Total Fare:",net_road * 1.18)
	elif perfernce == "c":
		pick_rand()
		print("Time of journey:",time_rail,"hr")
		print("Cost of journey:",net_rail)
		print("Gst",0.18 * net_rail)
		print("Total Fare:",net_rail + 1.18)
	
def print_output():
	print("Your booking is confirmed")
	print(f"Email id:{email_id}")
	print(f"--------------")
	
	
		

	
def main():
	global full_from,full_to,jry

	jry =""
	print(""" 
	Enter 1 for Banglore:
	Enter 2 for Mumbai:  
	Enter 3 for Kolkata: 
	Enter 4 for Delhi:
	Enter 5 for Hyderbad:""")
	
	user_input()
	
	if from_place=="1": 
		jry+="Blr-"
		full_from = "Banglore"
	elif from_place=="2":
		jry+="Mum-"
		full_from = "Mumbai"
	elif from_place=="3":
		jry+="Klt-"
		full_from = "Kolkata"	
	elif from_place == "4": 
		jry+="Del-"
		full_from = "Delhi"
	elif from_place == "5":
		jry+= "Hyd-"
		full_from = "Hyderabad"
	if to_place == "1":
		jry+="Blr"
		full_to = "Banglore"
	elif to_place == "2":
		jry+="Mum"
		full_to = "Mumbai"
	elif to_place == "3":
		jry+="Klt"
		full_to = "Kolkata"
	elif to_place == "4":
		jry+="Del"
		full_to = "Delhi"
	elif to_place == "5":
		jry+="Hyd"
		full_to = "Hyderbad"
	calculate_time(300,150,100)
	cost(100,10,30)

	if net_ariel > budget: 
		print("Air travel exceeds your budget!")
	if net_road > budget:
		print("Road travel exceeds your budget!")
	if net_rail > budget: 
		print("Rail exceeds your budget")
	booking_preference()

main()


def output():
	with open ("data_bill.txt","+w") as f:
		f.write(f"Your has been booked:")
		f.write("-"*50)
		f.write(f"Name:{name}\t Age:{age}\t EMAIL:{email_id}\t")

	
	
	




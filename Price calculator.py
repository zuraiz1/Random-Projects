# # DECLARE

# DECLARE name : STRING
# DECLARE Len, Wid, Area, Wood, Cost : REAL
# DECLARE run : BOOLEAN
# DECLARE ID : INTEGER

# DECLARE WoodType : ARRAY[1:3] OF STRING
# DECLARE Price : ARRAY[1:3] OF REAL

# Populating arrays

WoodType = ["Laminite", "Pine", "Oak"]
Price = [29.99, 39.99, 54.99]
Customers = []
Quotations = [[0 for col in range(5)] for row in range(3)]

run = True

while True :
# Getting the name and assigning an ID

	name = str(input("ENTER YOUR NAME : "))
	
	Customers.append(name)
	ID = len(Customers) - 1
	Quotations.append([0,0,0,0])
	
# Getting their data
	# Length
	
	while True:
		# correct = False
		Len = float(input(("Enter room length : ")))
		
		if Len < 1.5 or Len > 10.0 :
			print("Length is out of range") # DEnied 
			
		else :
			# correct = True
			Quotations[ID][0] = round(Len, 1) # rounding to 1 decimal
			break
	
	
	# Width
	
	while True:
		# correct = False
		Wid = float(input("Enter room Width : "))
		
		if Wid < 1.5 or Wid > 10.0 :
			print("Width is out of range") # DEnied 
			
		else : 
			# correct = True
			Quotations[ID][1] = round(Wid, 1) # rounding to 1 decimal
			break
	
	# Area
	
	Area = round(Len * Wid , 0)
	Quotations[ID][2] = Area
	
    # Woodchoice
	while True:
		print("1. Laminite",
			  "2. Pine",
			  "3. Oak")
		Wood = int(input("What type of wood would you like? (1, 2, or 3)"))
		if Wood >= 1 and Wood <= 3:
			Quotations[ID][3] = Wood
			break
		else:
			print("Enter a valid input (1, 2, or 3) : ")
	# Cost
	
	Cost = Area * Price[Quotations[ID][3]-1]
	Quotations[ID][4] = round(Cost, 2)
	
	# Output
	
	print("Name : ", Customers[ID])
	print("Choice of wood : ", Quotations[ID][3])
	print("Price : ", Quotations[ID][4])
	print("")
	print("")
	
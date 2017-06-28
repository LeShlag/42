import sys

if sys.argv[1] == None:
	print("Pas d'argument")

Arg = sys.argv[1].replace(" ","")
Total = Arg.split("=")[1]
Arg1 = "protect"
Arg2 = "protect"
Arg3 = "protect"


i = 0
deg = 0
for i in range(len(Arg)):
	if ( Arg[i] == '+' or Arg[i] == '-' or Arg[i] == '=' ) and i > 1 :
		if deg == 0 :
			Arg1_Splitted = Arg[0:i].split("*X^")
			oldi = i
		if deg == 1 :
			Arg2_Splitted = Arg[oldi:i].split("*X^")
			oldi = i
		if deg == 2 :
			Arg3_Splitted = Arg[oldi:i].split("*X^")
		deg = deg + 1
deg = deg - 1

Total_Splitted = Total.split("*X^")

i = float(deg)
while (i >= 0) :
	if (int(Arg1_Splitted[1]) == int(i)) :
		if (i == 2.0) :
			Sort_Arg1_Splitted = Arg1_Splitted
		elif (i == 1.0) :
			Sort_Arg2_Splitted = Arg1_Splitted
		elif (i == 0.0) :
			Sort_Arg3_Splitted = Arg1_Splitted
	elif (int(Arg2_Splitted[1]) == int(i)) :
		if (i == 2.0) :
			Sort_Arg1_Splitted = Arg2_Splitted
		elif (i == 1.0) :
			Sort_Arg2_Splitted = Arg2_Splitted
		elif (i == 0.0) :
			Sort_Arg3_Splitted = Arg2_Splitted
	elif (int(Arg3_Splitted[1]) == int(i)) :
		if (i == 2.0) :
			Sort_Arg1_Splitted = Arg3_Splitted
		elif (i == 1.0) :
			Sort_Arg2_Splitted = Arg3_Splitted
		elif (i == 0.0) :
			Sort_Arg3_Splitted = Arg3_Splitted
	i = i - 1.0


if (float(Total_Splitted[1]) == float(Sort_Arg1_Splitted[1])) :
	Sort_Arg1_Splitted[0] = str(float(Sort_Arg1_Splitted[0]) - float(Total_Splitted[0]))
elif (float(Total_Splitted[1]) == float(Sort_Arg2_Splitted[1])) :
	Sort_Arg2_Splitted[0] = str(float(Sort_Arg2_Splitted[0]) - float(Total_Splitted[0]))
elif (float(Total_Splitted[1]) == float(Sort_Arg3_Splitted[1])) :
	Sort_Arg3_Splitted[0] = str(float(Sort_Arg3_Splitted[0]) - float(Total_Splitted[0]))


print ("Reduced form: " + Sort_Arg1_Splitted[0] + " * X^2 " + Sort_Arg2_Splitted[0] + " * X^1 + " + Sort_Arg3_Splitted[0] + " * X^0 = 0" )
print ("Polynomial degree: " + str(deg))


delta = (float(Sort_Arg2_Splitted[0]) * float(Sort_Arg2_Splitted[0])) - (4.0 * float(Sort_Arg1_Splitted[0]) * float(Sort_Arg3_Splitted[0]))

if (delta > 0) :
	
	print ("Discriminant is strictly positive, the two solutions are:")
elif (delta < 0) :
	print ("Discriminant is strictly negative, the two complex solutions are:")
elif (delta == 0) :
	sol = -1.0 * float(Sort_Arg2_Splitted[0]) / (2 * Sort_Arg1_Splitted[1])
	print ("Discriminant is null, the solution is: " + sol)

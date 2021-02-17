motorbike = 2000

print ("The value of a motorbike is £" ,motorbike, "and loses 10% of its value every year. This program will print the bike’s value every year until it falls below £1000.")

motorbikevalue = 2000
while motorbikevalue > 1000:
  motorbikevalue = motorbikevalue * 0.9
  print("£" ,motorbikevalue,)
else:
   print ("Value is below £1000")
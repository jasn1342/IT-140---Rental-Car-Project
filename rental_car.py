import sys

#Rental Code Input
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

if rentalCode == 'B' or rentalCode == 'D':
	rentalPeriod = int(input("Number of Days Rented:\n"))
else:
	rentalPeriod = int(input("Number of Weeks Rented:\n"))

#Pricing
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

#Odemter Reading
odoStart = int(input("Starting Odometer Reading:\n"))
odoEnd = int(input("Ending Odometer Reading:\n"))
totalMiles = int(odoEnd) - int(odoStart)

#Pricing based on Rental Code input by user and miles driven
if rentalCode == "B":
  mileCharge = 0.25 * totalMiles
if rentalCode == "D":
  averageDayMiles = int(totalMiles) / int(rentalPeriod)
  if averageDayMiles <= 100:
    extraMiles = 0
  elif averageDayMiles > 100:
    extraMiles = averageDayMiles - 100
  mileCharge = .25 * extraMiles
  averageDayMiles = int(totalMiles) / int(rentalPeriod)
  if rentalCode == "W" and averageDayMiles > 900:
    mileCharge = rentalPeriod * 100
  elif rentalCode == "W" and averageDayMiles <= 900:
    mileCharge = 0

#Rental Summary
if rentalCode == "B":
  baseCharge = rentalPeriod * budget_charge
elif rentalCode == "D":
  baseCharge = rentalPeriod * daily_charge
elif rentalCode == "W":
  baseCharge = rentalPeriod * weekly_charge
  mileCharge = rentalPeriod * 100
  amountDue = float(baseCharge) + float(mileCharge)

print ("Rental Summary")
print ("Rental Code: " + str(rentalCode))
print ("Rental Period: " + str(rentalPeriod))
print ("Starting Odometer: " + str(odoStart))
print ("Ending Odometer: " + str(odoEnd))
print ("Miles Driven: " + str(totalMiles))
amountDue = amountDue = float(baseCharge) + float(mileCharge)
print ("Amount Due: " "${0:.2f}".format(amountDue))

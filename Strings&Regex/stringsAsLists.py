#We can turn a string into a list to make it more usable data
stringData = "Hattie Willem Leto Niko Franklin"
namesList = stringData.split(" ")
for name in namesList:
    print(name)

#we can also check a list to see if it contains a particular element
fallSportsString = "football,Cross Country,Volleyball,Soccer"
fallSports = fallSportsString.split(",")
print(fallSports)
chosenSport = input("What sport do you want to play?")
if chosenSport in fallSports:
    print("That will be great fun")
else:
    print(f"{chosenSport} is not available this fall.  So sorry.")
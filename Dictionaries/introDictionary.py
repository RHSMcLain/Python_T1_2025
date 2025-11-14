'''
    A dictionary gives you key value pairs: that is, you get to provide names for values inside a dictionary variable
    A dictionary cannot have duplicate keys
    '''
printer = {
    "name": "Betty",
    "AMS": "Veronica",
    "Capacity": 4
}
print(printer["AMS"])
print("Capacity: ", printer['Capacity'])

''' Use the len() function to get the numer of items in teh dictionary '''
print(len(printer)) #will print 3 in this case.


''' add to a dictionary on the fly '''
printer["Color1"] = "Bambu Green"

print(printer)
''' we can change existing values in the same way '''

printer["name"] = "Reginald the Fierce"
print(printer)

# get a list of all the keys in the dictionary
keys = printer.keys()
print(keys)

# get the values
vals = printer.values()
print(vals)

#remove items from a dictionary
val = printer.pop("Color1")
print(printer)
print(val)

# Loop through a dictionary
for key in printer:
    print(f'{key}: {printer[key]}')
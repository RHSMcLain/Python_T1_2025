
#formatting
#you can find great information at https://fstring.help/cheat

# so far we've done a lot of this: 
product = "jacket"
print("This product is a " + product)
print("This " + product + " is amazing!")
#but we can use "f-strings" to make this easier
print(f"This product is a {product}")
print(f"This {product} is amazing!")
#and we can put numbers in more easily
qty = 235
print(f"There are {qty} available {product}s")
#and we can format decimal places inline, too
price = 18.35 / 2
print(f"Those cost ${price:06.2f} each")
#AND we can do math inline
print(f"If you want all {qty}, that will be ${qty * price:.2f}")
#---------------------
#Quotes inside quotes
#there are two options for your quotation marks: double quotes ("") and single ('')
print("He said 'go left'!")
#or reverse it
print('He said, "Go Left"!')
#that gets more complicated if you need both, as in 
print('He said, "You can\'t go Left"')  #that backslash escapes the ' and says "this is just a string"
      

#multiline Strings
#triple quotes let you just type what you want, including line breaks
print(""" 
    When I have fears that I may cease to be
    Before my pen has gleaned my teeming brain
    Before High-Piled books in charact'ry hold
    Like rich garners the full-ripened grain

""")

#Strings as arrays (aka lists)
#strings are lists in Python
phrase = "Buyer Beware"
print (phrase[4])

print(phrase[1:4])
print(phrase[0:8]) #from the start to character 8
#same as this:  
print(phrase[:8])
print(phrase[3:])
#negative numbers go backwards
print(phrase[-1])
print(phrase[-5:])

#modifying
print(phrase.upper())
print(phrase.lower())

phrase = "     Diamond.   "
print(f'-{phrase}-')
phrase = phrase.strip()
print(f'-{phrase}-')
  #we can do replacements, too
phrase = phrase.replace("d", "!")
print(phrase)

#find the location of a character
n = phrase.find("a")
print(n)
print(phrase[n])
productID1 = "817-3016"
productID2 = "09-3185"
separator = productID2.find("-")
deptCode = productID2[:separator]
print(deptCode)

#splits and partitions -- converting strings into data
email = "amclain@riverdale.k12.or.us"
#partition takes a string to match, and returns a tuple with 3 parts: the part before the match, the match, and the part after
parts = email.partition("@")
print(parts)

#rpartition does the same thing, but searches for the last match, not the first
parts2 = email.rpartition(".")
print(parts2)

colors = "red,blue,green,chartreuse,magenta"
colorsList = colors.split(",")
print(colorsList)




#Check contents

#with strings and lists, you can check to see if it contains something particular
print("black" in colors)
myGroceries = "milk,sugar,eggs,cinnamon,powdered sugar,flour".split(",")
print(myGroceries)
if ('eggs' in myGroceries):
    print("You need that")
if ('motor oil' not in myGroceries):
    print("You don't need to go to the auto parts store")












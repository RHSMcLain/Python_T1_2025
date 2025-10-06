
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

#Strings as arrays


#Check contents

#slicing strings (and lists for that matter)


#modifying




#other methods




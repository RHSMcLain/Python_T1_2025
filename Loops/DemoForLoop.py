for n in range(10, 100, 5):
    print(n)

#which is the same as saying: 
n = 10
while n < 100:
    print(n)
    n += 5

fruits = ["persimmon", "dragon fruit", "mangosteen", "Pluot"]
print(fruits)
fruits.append("apple")
newFruit = input("What is your favorite fruit?")
fruits.append(newFruit)

for fruit in fruits: 
    #loops through all items in the list. In each iteration, the variable fruit gets the next item in the fruits list.
    print(fruit)
print("----")
print(fruits[1])


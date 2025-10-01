for n in range(10, 100, 5):
    print(n)

#which is the same as saying: 
n = 10
while n < 100:
    print(n)
    n += 5

fruits = ["persimmon", "dragon fruit", "mangosteen", "Pluot"]
print(fruits) #not a user-friendly way to print your list
fruits.append("apple") #add 'apple' as a new item at the end of the list
newFruit = input("What is your favorite fruit?")
fruits.append(newFruit)

for fruit in fruits: 
    #loops through all items in the list. In each iteration, the variable fruit gets the next item in the fruits list.
    print(fruit)
    fruit = "pineapple pizza"

print("pineapple pizza")
for fruit in fruits: 
    print(fruit)
print("----")
print(fruits[1]) #access an individual item in the list by its index. 



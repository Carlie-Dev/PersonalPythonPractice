#print
print('Hello Word!')

#how to take an input. input() reads the input and sets the variable to whatever is typed in it's place.
print('Input your last name:')
last_name = input()

print('input your first name:')
first_name = input()
print(last_name, '-', first_name)

#Getting numbers
print('Enter a number:')
num1 = int(input())
print('Enter a number:')
num2 = int(input())
print('Enter a number:')
num3 = int(input())
print('The product of the numbers you entered is:')
print(num1*num2*num3)

#concatanation
print('enter a number')
num_condos = input()

print('Sam sold', num_condos, 'condos.')

#Length of name
name = 'Carlie'
print(len(name))
print(name[2])

num1 = 14924
num2 = 140002
num3 = 247
num4 = 203

print(f'Hello, {name}, nice to meet you!')

#Displaying number with commas
print(f'{num1:,d}')

#displaying number with leading zero
print(f'{num2:07d}')

#displaying number in binary
print(f'{num3:b}')

#Hexidecimal
print(f'{num4:x}')

#Capital Hexidecimal
print(f'{num4:X}')

red = 144
green = 39
blue = 207

print(f'Red Binary: {red:b} | Red Hexidecimal: {red:x}')
print(f'Green Binary: {green:b} | Green Hexidecimal: {green:x}')
print(f'Blue Binary: {blue:b} | Blue Hexidecimal: {blue:x}')

#lists and collections
myList = [red,green,blue,255,'singer']
print(myList[4])
myList.pop(3)
print(myList[3])

myList.remove('singer')
print(myList)

#Strings and lists are types of collections so they behave similarly and both use len() for getting the length
#Length of list
print(len(myList))

myList2 = [100,25,209]

#Combining lists
superList = myList + myList2
print(superList)

#lists of lists
superList = [myList, myList2]
print(superList)

#opperations for lists
print(sum(myList))
print(max(superList))
#The index of 39 is one
print(myList.index(39))




#Sets
#Sets are similar because they are a collection
#Unlike a list it can only contain unique data

mySet = {30,11,59,600}
#mySet.add(30) will not change it because 30 already exists
print(mySet)
#use the value to get the value
print(mySet)


#Dictionary
myDict = {'Burger': 1.99, 'ChickenStrip': 2.99, 'Soda':.99}

print(myDict['Burger'])
#Lesson 3: Integers and Floats


#3.1: Assigning integers and basic arithmetic

num = 3

print (num)
print (type(num)) #shows whether number is an integer or a float

num = 3.14

print (type(num))

print (6+4)
print (6-4)
print (6*4)
print (6/4)
print (6**4)
print (6//4)
print (6%2) #Common check for even numbers
print (215%2) #Common check for odd numbers

#Note that Python follows regular order of operations


#3.2: Incrementing values

num = 2
num = num +1
#or shorthand version:
num += 1

print (num)


#3.3: Absolute values, rounding

print(abs(-3))

print(round(4.85))
print(round(4.85, 1)) #Rounds to first, second, etc.. digit after decimal


#3.4: Comparison operators

#These operators return a TRUE or FALSE boolean if numbers are equal, not equal, etc...

num_1 = 4
num_2 = 5

print (num_1 == num_2) #Checks if numbers are equal
print (num_1 != num_2) #Checks if numbers are not equal
print (num_1 > num_2) #Checks if greater than
print (num_1 < num_2) #Checks if less than
print (num_1 >= num_2) #Checks if greater than or equal to
print (num_1 <= num_2) #Checks if less than or equal to


#3.5: Confusing strings and integers

#Strings with numbers (from websites, etc...) can be confused as integers, and may not work properly in arithmetic

num_3 = '100'
num_4 = '300'

print (num_3 + num_4)

#Can fix this by casting the string with int()

num_3 = '100'
num_4 = '300'

num_3 = int(num_3)
num_4 = int(num_4)

print (num_3 + num_4)

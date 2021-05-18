#Lesson 7: Loops and Iterations

numbers = [2, 4, 6, 8, 10]

for int in numbers:
    print (int)


#7.1: Break and Continue Keywords

for int in numbers:
    if int == 6:
        print ('Found the number')
        break #Breaks out of the current loop if the conditional is met
    print (int)

for int in numbers:
    if int == 6:
        print ('Found the number')
        continue #Continues to the next iteration if the conditional is met
    print (int)


#7.2: Loops within loops

for int in numbers:
    for letter in 'xyz':
        print (int, letter) #This code prints out each character in the string for each number

#Be careful with nested loops, as they can grow quite fast


#7.3: The range function

#This function is very helpful for running through a loop a certain number of times

for i in range(8):
    print(i)

for i in range(2,6): #Puts upper and lower bounds on the desired range
    print (i)

for i in range(3,16):
    print (i)
    if i == 12:
        print ("It's the lucky number!")
        break


#7.4: While loops

#These loops go on forever until the condition at the top is evaluated as false

x = 0

while x < 25:
    print (x)
    x += 2

#Like with for loops, can use break to halt the loop at any time

y = 
while y > 12:

    print (y)
    x += 2

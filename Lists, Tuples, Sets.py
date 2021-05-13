#Lesson 4: Lists, Tuples, and Sets


#4.1: Creating a list

animals = ['chickens', 'dogs', 'cuttlefish', 'beetles']
primes = [1, 3, 5, 7]

print (animals)
print (primes)

print (len(animals)) #Prints the length of the list
print (animals[0]) #Prints the first value in the list
print (animals[-1]) #Always prints the last value in the list

print (animals[1:4])
print (animals[:2])


#4.2: Some addition list methods

#Several methods exist to make a list longer or add new values

animals.append('goats') #Appends value to the end of a list

print (animals)

animals.insert(2, 'bees') #Inserts value at the specified list location

print (animals)

#The extend method can merge one list's values with another

animals = ['chickens', 'dogs', 'cuttlefish', 'beetles']
animals_2 = ['cows', 'sharks']

animals.extend(animals_2)

print (animals)

#if you try this with append or insert, the whole list gets added instead of just the individual values

animals = ['chickens', 'dogs', 'cuttlefish', 'beetles']
animals_2 = ['cows', 'sharks']

animals.insert(2, animals_2)

print(animals)


#4.3: Some subtraction list methods

animals = ['chickens', 'dogs', 'cuttlefish', 'beetles']

animals.remove ('chickens') #Removes a value from the list

print (animals)

animals.pop() #Removes last value as default

print (animals)

popped = animals.pop() #can also be set as a variable assigned with the popped value. note this code pops the list again

print (animals)
print (popped)


#4.4: Ordering lists with methods

animals = ['chickens', 'dogs', 'cuttlefish', 'beetles']

animals.reverse() #Reverses the values in the list
print (animals)

animals.sort() #Sorts the list's values alphabetically
primes.sort() #Or in ascending order for numbers

print (animals)
print (primes)

#Lists can also be sorted in descending order by adding argument to sort method

animals = ['chickens', 'dogs', 'cuttlefish', 'beetles']

animals.sort(reverse = True)
primes.sort(reverse = True)

print (animals)
print (primes)

#You can also get a sorted version of the list without altering the original list

animals = ['chickens', 'dogs', 'cuttlefish', 'beetles']

sorted(animals) #Sorted function doesn't alter the original list
sorted_animals = sorted(animals)

print (sorted_animals)


#4.5: Other list techniques

print(min(primes)) #Prints the minimum value of list of numbers
print(max(primes)) #Prints the maximum value
print(sum(primes)) #Prints the sum of the values

#You can find values in list with index method

print(animals.index('dogs')) #Returns the list location of the value

print('sharks' in animals) #Shows if value is in the list
print('cuttlefish' in animals)

for animal in animals:
    print (animal)
#Above for loop runs through list and prints out each values

for index, animal in enumerate(animals):
    print (index, animal)
#Enumerate function gives index along with value, requires index and value input

for index, animal in enumerate(animals, start=1):
    print (index, animal)
#Modifies the starting index


#Lists can be converted into strings, and vice versa

animal_str = ', '.join(animals) #Join function converts list into a string

new_animals =  animal_str.split(', ') #Split function splits string into list of values at specified spot

print (animal_str)
print (new_animals)


#4.6: Tuples

#Tuples are similar to lists, but are immutable. This offers an advantage in situations where you don't want to change a list
#For example, in the following list_1 can't be modified without changing list_2

list_1 = ['red', 'green', 'blue']
list_2 = list_1

print (list_1)
print (list_2)

list_1[0] = 'orange'

print (list_1)
print (list_2)

#Using tuples instead ensures that either collection of values will change

tuple_1 = ('red', 'green', 'blue')
tuple_2 = tuple_1

print (tuple_1)
print (tuple_2)

for index, color in enumerate(tuple_1, 1):
    print (index, color)


#4.7: Sets

#Sets are values that are unordered and contain no duplicates.

colors = {'red', 'green', 'blue', 'orange'}

print (colors)

#Sets are often used to test whether a value is part of a set (membership test) or to remove duplicate values
#Can be done with lists and tuples, but sets are optimized for this

colors = {'red', 'green', 'blue', 'orange', 'blue'}

print (colors)

print ('blue' in colors)

#Sets can also be used to tell whether they share or don't share values with other sets

colors = {'red', 'green', 'blue', 'orange', 'blue'}
colors_2 = {'orange', 'yellow', 'pink'}

print (colors.intersection(colors_2)) #prints values the sets have in common
print (colors.difference(colors_2)) #prints the values in set 1, but not set 2
print (colors.union(colors_2)) #prints the combination of values from both sets


#4.8: Creating empty lists, tuples, and sets

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} #Wrong! Creates a dictionary, not an empty set
empty_set = set() #This is right

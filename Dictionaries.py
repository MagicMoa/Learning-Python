#Lesson 5: Dictionaries

#Dictionaries are groups of values that can be defined with key-value pairs

country = {'Name': 'Switzerland', 'Size': 'Small', 'Continent': 'Europe', 'Cities': ['Zurich', 'Basel']}

print (country)

print (country['Size']) #Can access the value for a specified key

print (country.get('Name')) #Alternative method, returns "none" for nonexistent key instead of error
print (country.get('Climate'))
print (country.get('Climate', 'Not Found')) #Specifies what to return for nonexistent key


#5.1: Adding and Updating Dictionary Entries

country['Climate'] = 'Temperate'
country['Name'] = 'Brazil'

print (country)

#As an alternative, update method allows us to change multiple entries at once

country.update({'Size':'Large', 'Continent':'South America', 'Cities':['Rio de Janeiro', 'Brasilia']})

print (country)


#5.2 Deleting Dictionary Entries

del country['Continent'] #Deletes a specific key

print(country)

brazilian_cities = country.pop('Cities') #Pops off specific value, which can then be assigned

print(brazilian_cities)


#5.3: Looping through Keys and Values in Dictionaries

country = {'Name': 'Switzerland', 'Size': 'Small', 'Continent': 'Europe', 'Cities': ['Zurich', 'Basel']}

print (len(country)) #Prints the dicitonary's length
print (country.keys()) #Prints the dictionary's keys
print (country.values()) #Prints the dictionary's values
print (country.items()) #Prints the dictionary's keys and values

for Item in country:
    print (Item) #Without a method, a for loop will only print a dictionary's keys

for key, value in country.items():
    print (key, value)

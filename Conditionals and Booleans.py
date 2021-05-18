#Lesson 6: Conditionals and Booleans


#6.1: Using If Statements

if True:
    print ('Conditional was true')

if False:
    print ('Conditional was false')

#Conditionals are not usually used alone, but alongside other code

language = 'Spanish'

if language == 'Spanish':
    print ('El idioma es espanol')


#6.2: Adding Else and Elif Statements:

language = 'English'

if language == 'Spanish':
    print ('El idioma es espanol')
else:
    print ('???')

language = 'English'

if language == 'Spanish':
    print ('El idioma es espanol')
elif language == 'English':
    print ('The language is English') #Can keep adding elif statements for more variables
else:
    print ('???')


#6.3: Boolean Operators (and, or, not)

customer = 'Member'
receptive = False

if customer == 'Member' and receptive:
    print ('See our new offers!')
else:
    print ("Sorry, we won't bother you again.")

if customer == 'Member' or receptive:
    print ('See our new offers!')
else:
    print ("Sorry, we won't bother you again.")

if not receptive:
    print ('Are you sure you want to cancel offers?')
else:
    print ('Glad to have you here!')


#6.4: Object Identities

#Object identity (is) tests if two objects have the same ID, not just if they're equal

first_set = [1, 2, 3]
second_set = [1, 2, 3]

print (first_set == second_set)

print (id(first_set))
print (id(second_set))
print (first_set is second_set) #Returns False since they're still different objects

first_set = [1, 2, 3]
second_set = first_set

print (id(first_set))
print (id(second_set))
print (first_set is second_set)

#Therefore, the is operator is really asking if:

print (id(first_set) == id(second_set))


#6.5: What Python evaluates to True or False

#Python will evaluate the following as False:
    # False
    # None
    # Zeroes of any numeric type
    # Any empty sequence, such as ()
    # Any empty mapping, such as {}

statement = None

if statement:
    print ("It's true")
else:
    print ("It's false")

#Everything else in Python will be mapped to true

statement = 'Yes'

if statement:
    print ("It's true")
else:
    print ("It's false")

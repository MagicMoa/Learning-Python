#Lesson 2: Strings

print('Hello World!')


message = 'Hello World!'
#assigns a string to a representation
print (message)


print (message.upper()) #changes string to uppercase
print (message.lower()) #changes string to lowercase

message = message.replace('World', 'my people') #replaces part of a string with something else

print (message)


#Strings can be combined either with +:

greeting = "Greetings friends"
question = "How are you?"

message = greeting + '. ' + question

print (message)

#Or more easily with brackets:

greeting = "Greetings friends"
question = "How are you?"

message = '{}, this is Joe. {}'.format(greeting,question)

print (message)

#As an alternative, python 3 features a new f-string format for simplifying string combinations

message_2 = f'{greeting}, this is not Joe. {question}'

print (message_2)

#

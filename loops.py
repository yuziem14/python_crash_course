'''
https://github.com/bradtraversy/python_sandbox
'''

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
    print('Current Person: {person}'.format(person=person))

# Break
for person in people:
    if person == 'Sara':
        break
    print('Current Person: {person}'.format(person=person))

# Continue
for person in people:
    if person == 'Sara':
        continue
    print('Current Person: {person}'.format(person=person))

# range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print('Number: {i}'.format(i=i))

# While loops execute a set of statements as long as a condition is true.

count = 0
while count < 10:
    print('Count: {count}'.format(count=count))
    count += 1

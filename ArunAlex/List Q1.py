# Create a list of week days (Sunday to Saturday).
weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Print 3rd item of the list.
print(weekdays.index('Tuesday'))

# Print 3rd item of the list.
print(weekdays[2])

# Print length of the list.
print(len(weekdays))

# Remove Friday from the list.
weekdays.pop(6)

# Add Friday to the list before Saturday
weekdays.insert(5, 'Friday')

# Print number of times Monday occured in the list.
weekdays.count('Monday')

# Remove Monday from the list
weekdays.pop(1)

# Print the list by reversing it
weekdays.reverse()
print(weekdays)

# Print the list by sorting ascending
weekdays.sort()
print(weekdays)

# Print the list by sorting descending
weekdays.sort(reverse=True)
print(weekdays)

# Print all the items in the list using for loop
for x in weekdays:
    print(x)

# Print all the index values for each item in the list (loop)
for x in weekdays:
    print(x, '-', (weekdays.index(x)))

#Copy this list to another new list
week_days_1=weekdays.copy()

#Merge both lists to first list
weekdays.extend(week_days_1)

#Clear all the items in the list
weekdays.clear()

#Print type of the list class
print(type(weekdays))

print(weekdays)

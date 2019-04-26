# Create a dict variable as stated above.
countries_population = {"India": "1.3", "China": "1.4", "USA": "0.32", "Indonesia": "0.26"}

# Print value of key India
print(countries_population["India"])

# Print length of the list
print(len(countries_population))

# Print value of key China
print(countries_population.get('China'))

# Return all the keys of the dict
print(countries_population.keys())

# Remove key = Indonesia from the list
countries_population.pop('Indonesia')

# Add new items Canada = 0.03 billion
countries_population.update({"Canada": "0.03"})
print(countries_population)

# Print all the dict keys in the list (loop)
for x in countries_population:
    print(x)
# Print all the dict values in the list (loop)
for x in countries_population:
    print(x, '=', countries_population[x])

# Print the values of countries USA and India
for x in countries_population:
    if x == 'India':
        print(x, '=', countries_population[x])
    elif x == 'USA':
        print(x, '=', countries_population[x])

# Print the values of countries except for USA
for x in countries_population:
    if x != 'USA':
        print(x, '=', countries_population[x])


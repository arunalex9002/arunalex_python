# Create a dict variable as stated above.
countries_population = {"India": "1.3", "China": "1.4", "USA": "0.32", "Indonesia": "0.26"}


# Create a function to add a new country and population.
def add_country(_country_name, _population):
    countries_population[_country_name] = _population


add_country('China', '1.4')

print(countries_population)


# Create a function to update a country’s pupulation based on country name.
def update_country(_country_name, _population):
    if _country_name in countries_population.keys():
        print('Country already Exists')
    else:
        countries_population.update({_country_name: _population})


update_country('Mexico', '0.5')


# Create a function to delete a country.Return error message if there no country with that name.
def del_country(_country_name):
    if _country_name in countries_population.keys():
        countries_population.pop(_country_name)
    else:
        print('Country not found')


del_country('China')

print(countries_population)


# Create a function to return all country names and population.
def show_all_countries():
    return (countries_population.keys())


show_all_countries()


# Create a function to return population given a country name.
def return_population(_country_name, ):
    if _country_name in countries_population.keys():
        return (countries_population[_country_name])
    else:
        print('Country not found')


return_population('USA')

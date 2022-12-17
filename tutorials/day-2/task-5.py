countries = ['USA', 'Argentina', 'Spain', 'Brasil', 'Uzbekistan']

print('countries: ', countries)
print('countries len: ', len(countries))

print('sorted countries: ', sorted(countries))
print('reversed countries: ', sorted(countries, reverse=True))
print('countries: ', countries)

countries.reverse()
print('reversed countries: ', countries)

countries.sort()
print('sorted countries: ', countries)

countries.sort(reverse=True)
print('reversed countries: ', countries)

numbers = list(range(120, 1200, 2))
print('numbers sum: ', sum(numbers))
print('max - min of numbers: ', max(numbers) - min(numbers))
print('count of numbers: ', len(numbers))

print('first twenty elements: ', numbers[:20])
print('last twenty elements: ', numbers[-20:])

middle = len(numbers) // 2
print('middle twenty elements: ', numbers[middle:middle + 20])

foods = ['Osh', 'Kabob', 'Hotdog', 'Burger']

launch = foods[:]
launch.remove('Hotdog')
launch.remove('Burger')
launch.append('Stake')
launch.append('Anything')

print('foods: ', foods)
print('launch: ', launch)

launch_tuple = tuple(launch)
print('Tuple launch: ', launch_tuple)

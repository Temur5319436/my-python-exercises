names = ['usmonaliyev', 'Temur', 'bekzod', 'javohir', 'Nozim', 'Shavkat']
names.sort()

print(f'List is sorted: {names}')

names.sort(reverse=True)
print(f'List is desc sorted: {names}')

print(f'List is sorted by sorted() function: {sorted(names)}')

print(
    f'List is desc sorted by sorted() function: {sorted(names, reverse=True)}')

usernames = ['sadettin', 'small', 'n0th1ng',
             'iutarian', 't1nnur', 'yamac', 'developer']
print(f'New usernames : {usernames}')

usernames.reverse()
print(f'Usernames is reversed: {usernames}')

print(f'Length of usernames: {len(usernames)}')

prices = [1000, 1100, 300, 500, 987, 2390]
print(f'New prices list: {prices}')

print(f'Max of prices: {max(prices)}')
print(f'Min of prices: {min(prices)}')
print(f'Sum of prices: {sum(prices)}')

print(f'List is cut: {prices[0:4]}')

print(f'First 3 elements: {prices[:3]}')
print(f'Last 3 elements: {prices[3:]}')

print(f'Copied from list: {prices[:]}')

places = ('Tashkent', 'Kokand', 'Asia', 'Europe', 'USA')
print(f'Tuples: {places}')

print(f'Converting tuple to list: {list(places)}')

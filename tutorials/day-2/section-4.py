numbers = [1, 2, 3, 4, 5]
names = ['Temur', 'Hamza', 'Jonny', 'Khusan', 'Doni']

print(numbers)
print(names)

print(f'First element: {numbers[0]}')
print(f'Last element: {numbers[-1]}')

numbers[1] = 6
numbers[-1] = 1

print(f'List is changed: {numbers}')

numbers.append(7)
numbers.append(8)

print(f'Items are added to list: {numbers}')

del numbers[1]
print(f'First element is deleted: {numbers}')

numbers.insert(2, 45)
print(f'Item is added to list: {numbers}')

numbers.pop(2)
print(f'Item is pop from list: {numbers}')

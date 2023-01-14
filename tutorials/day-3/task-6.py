from datetime import datetime

random_number = int(input('Istalgan sonni kiriting:'))
print(
    f'Kiritilgan raqamni kvadirati: {random_number**2}, kubi: {random_number**3}')

age = int(input('Yoshingiz nechida:'))

print(f'Sizning tug\'ilgan yilingiz: {datetime.now().year - age}')

first_number = int(input('Birinchi raqamni kiriting:'))
second_number = int(input('Ikkinchi raqamini kiriting:'))

print(f'{first_number} + {second_number} = {first_number + second_number}')
print(f'{first_number} - {second_number} = {first_number - second_number}')
print(f'{first_number} * {second_number} = {first_number * second_number}')
print(f'{first_number} / {second_number} = {first_number / second_number}')

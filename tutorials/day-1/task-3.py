import datetime

number = int(input("Istalgan sonni kiriting:"))

print(number, " sonining kvadirati ", number**2, " ga teng")
print(number, " sonining kubi ", number**3, " ga teng")

age = int(input("Yoshingiz nechida:"))
print("Siz ", datetime.datetime.now().year - age, " yilda tug'ilgansiz")

first_number = int(input("Birinchi sonni kiriting:"))
second_number = int(input("Ikkinchi sonni kiriting:"))
print(f'{first_number} + {second_number} = ', first_number + second_number)
print(f'{first_number} - {second_number} = ', first_number - second_number)
print(f'{first_number} * {second_number} = ', first_number * second_number)
print(f'{first_number} / {second_number} = ', first_number / second_number)

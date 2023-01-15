password = input('Enter your password: ')

# Password Criteria
# 8 characters or more in length
# at least one digit
# at least one capital letter

length = len(password)
result = {}

if length == 7:
    result["length_number"] = 7
elif length < 8:
    result["length"] = False
else:
    result["length"] = True

digit_signal = False
for char in password:
    if char.isdigit():
        digit_signal = True

result["number"] = digit_signal

capitalize_signal = False
for char in password:
    if char.isupper():
        capitalize_signal = True

result["upper-case"] = capitalize_signal

print(result) # dictionary

# if all(result) == True: //alternative code
if all(result.values()):
    print('Strong password.')
else:
    print('Weak password.')


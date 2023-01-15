
date = input("Please enter today's date: ")
mood = input("Please rate your mood: ")
thoughts = input("Please write down your thoughts:\n")

filepath = f'Files/Journal/{date}.txt'

with open(filepath, 'w') as file:
    file.write(mood + 2*'\n')
    file.writelines(thoughts)






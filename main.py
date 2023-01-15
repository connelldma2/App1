filenames = ["1. Bonus Material", "2. Literature Review", "3. Annexes"]
updated_filenames = []
i = 0

for filename in filenames:
    new_filename = filenames[i].replace('.', '-', 1)
    updated_filenames.append(new_filename)
    i = i + 1
print(updated_filenames)




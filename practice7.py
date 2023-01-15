filenames = ['Exercise1.txt', 'Exercise2.txt', 'Exercise3.txt']
word = 'Hello'

for filename in filenames:
    file = open(f'Files\{filename}', 'w')
    file.writelines(word)
    file.close()
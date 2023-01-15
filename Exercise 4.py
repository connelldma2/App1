
filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f'Files\{filename}')
    output = file.read()
    file.close()

    print(output)
    print(type(output))
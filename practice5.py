contents = ['Contents of File 1', 'Contents of File 2', 'Contents of File 3']
filenames = ['file1.txt', 'file2.txt', 'file3.txt']

for content, filename in zip(contents, filenames):
    filepath = f'Files\{filename}'
    file = open(filepath, 'w')
    file.write(content)
    file.close()




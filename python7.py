
filenames = ["1.document", "2.report", "3.presentation"]

filenames = [filename.replace('.', '-') + '.docx' for filename in filenames]

print(filenames)
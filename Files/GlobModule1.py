
import glob

myfile_collection = glob.glob("../MyFiles/*.txt")

print(myfile_collection)

for filepath in myfile_collection:
    print('File name: ', filepath.strip('../MyFiles\\'))
    with open(filepath, 'r') as file:
        print(file.readlines())


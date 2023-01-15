
filepath = 'Files\members.txt'

file = open(filepath, 'r')
members = file.readlines()
file.close()

print(members)

new_member = input('Admit a new member: ')
new_member = '\n' + new_member
members.append(new_member)

file = open(filepath, 'w')
file.writelines(members)
file.close()



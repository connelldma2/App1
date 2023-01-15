
user_entries = ['10', '19.1', '20']

user_entries_float = [float(user_entry) for user_entry in user_entries]

print(user_entries_float)
print(type(user_entries_float))

for i in user_entries_float:
    print(type(i))

print(sum(user_entries_float))

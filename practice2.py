todos = ['clean', 'polish', 'hoover']

for i, item in enumerate(todos):
    print('{}. {}'.format(i + 1, item.capitalize()))

print('\n')

for i, item in enumerate(todos):
    output = f'{i + 1}. {item.capitalize()}'
    print(output)

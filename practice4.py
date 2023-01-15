buttons = [('John', 'Millie', 'Sarah'), ('Linny', 'Jacob', 'Susan'), ('Sean', 'Caoimhe', 'Tadgh')]

for i, name in enumerate(buttons):
    #row = f'{i+1}. {name}'
    #print(row)
    print('\n')
    for index, item in enumerate(name):
        print(f'{index+1}. {item}')
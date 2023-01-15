waiting_list = ['ben', 'mike', 'matthew', 'stephen', 'susan', 'peter']

waiting_list.sort(reverse=True)

for i, item in enumerate(waiting_list):
    output = f'{i + 1}. {item.capitalize()}'
    print(output)


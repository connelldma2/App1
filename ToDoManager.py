from ToDoFunctions import show_list, get_file_todos, write_file_todos
import time

now = time.strftime("%d %b %Y %H:%M:%S")
print("Current Time: ", now)

exception = 'Incorrect command.'

while True:
    user_choice = input("Add, Show, Edit, Complete, or End: ")
    user_choice = user_choice.capitalize()
    user_choice = user_choice.strip()

    if user_choice.startswith('Add') or user_choice.startswith('New'):
        todo = user_choice.strip('Add')

        # file = open('external.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # with open('external.txt', 'r') as file:
            # todos = file.readlines()

        todos = get_file_todos('external.txt') # call function

        todos.append(todo + '\n')

        # new_file = open('external.txt', 'w')
        # new_file.writelines(todos)
        # new_file.close()

        # with open('external.txt', 'w') as new_file:
            # new_file.writelines(todos)

        write_file_todos(todos)

    elif user_choice.startswith('Show'):
        # file = open('external.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # with open('external.txt', 'r') as file:
            # todos = file.readlines()

        todos = get_file_todos() # call function

        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)

        # alternative method
        # new_todos = [item.strip('\n') for item in todos]

        index = 1
        for item in new_todos:
            item = item.title()
            print('{}. {}'.format(index, item))
            index = index + 1
        index = 0

    elif user_choice.startswith('Edit'):
        try:
            # with open('external.txt', 'r') as file:
                # todos = file.readlines()

            get_file_todos() # call function

            show_list(todos)

            select_number = user_choice.strip('Edit')
            todos_to_delete = todos[int(select_number)-1].strip('\n')
            # todos_to_delete = todos_to_delete.strip('\n')
            new_item = input("Enter a new value: ") + '\n'

            #update list of items
            todos[int(select_number)-1] = new_item

            #write revised list to file
            # with open('external.txt', 'w') as updated_file:
                # updated_file.writelines(todos)

            write_file_todos(todos)

            #confirm selected item deleted
            print(f'{todos_to_delete} has been removed from the source file.\n')
        except ValueError:
            print('This command is not recognised.\n')
            continue

    elif user_choice.startswith('Complete'):
        try:
            item_complete = int(user_choice.strip('Complete'))

            # with open('external.txt', 'r') as file:
                # todos = file.readlines()

            todos = get_file_todos() # call function

            item_removed = todos.pop(item_complete - 1)
            print('Item completed: {}'.format(item_removed.capitalize()))

            # with open('external.txt', 'w') as new_file:
                # new_file.writelines(todos)

            write_file_todos(todos) # call function

        except IndexError:
            print('This command is not recognised.\n')
            continue

    elif user_choice.startswith('End'):
        break
    else:
        print(exception)
print('\n')
print('Program ended.')
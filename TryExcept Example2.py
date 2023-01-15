try:
    waiting_list = ['john', 'mike', 'james', 'susan', 'marie']

    name = input('Please enter your name: ').lower()

    queue_num = waiting_list.index(name) + 1 # get index position for name location in list

    print(f"{name.title()}'s position in the queue is {queue_num}.")
except ValueError:
    print(f"{name.title()} is not located in the waiting register.")


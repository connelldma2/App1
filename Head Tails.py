with open('sides.txt', 'w') as file:
    file.write('')

while True:
    with open("sides.txt", 'r') as new_file:
        sides = new_file.readlines()

    side = input("Throw the coin and enter head or tail here: ? ") + "\n"

    sides.append(side)

    print(sides)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")
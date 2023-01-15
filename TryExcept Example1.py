
while True:
    try:
        width = float(input("Enter rectangle width: "))
        length = float(input("Enter rectangle length: "))

        if width == length:
            # exit("That looks like a square!") //red font used in error message // program closes
            print("The length must be greater than the width.")
            continue
        else:
            area = width * length
            print(area)
            break

    except ValueError:
        print("You must enter numbers only.")
        continue
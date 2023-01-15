def average_temp():
    total_temp = 0

    with open('data.txt', 'r') as file_local:
        temp = file_local.readlines()

    values = temp[1:]

    values = [float(i) for i in values]

    # for i in values:
        # total_temp = total_temp + i

    # average_temp = total_temp / len(values)

    average_temp = sum(values) / len(values)
    return average_temp

average = average_temp()

print(f'Average Temperature: {average} degrees Celsius')

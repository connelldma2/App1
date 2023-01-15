
def convert_to_metric(feet_inches_arg):
    parts = feet_inches_arg.split(" ") #converts to list
    feet = float(parts[0])
    inches = float(parts[1])

    #calculate metric values
    metres = (feet * 0.3048) + (inches * 0.0254)

    metres = round(metres, 1)

    return metres



feet_inches = input('Please enter feet and inches: ')

metric_conversion = convert_to_metric(feet_inches)

print(f'{feet_inches} converts to {metric_conversion} metres.')

if metric_conversion < 8:
    print('Permitted to proceed under archway.')
else:
    print('Height Restriction. Maximum height is 8 metres.')
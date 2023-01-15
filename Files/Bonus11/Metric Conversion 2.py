
from MetricConversionFunctions import parse, convert_to_metric


feet_inches = input('Please enter the imperial height (feet inches): ')

parsed_values = parse(feet_inches) # assigns dictionary key/values to variable

result = round(convert_to_metric(parsed_values['feet'], parsed_values['inches']), 1)

print(f'{parsed_values["feet"]} feet and {parsed_values["inches"]} inches converts to {result} metres.')

if result < 8:
    print('Please proceed under arch way.')
else:
    print('Height restrictions apply. Maximum height is 8 metres.')
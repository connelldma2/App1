
def parse(feet_inches_arg):
    feet_inches_local = feet_inches_arg.split(' ') #convert string to list with parts
    feet = float(feet_inches_local[0])
    inches = float(feet_inches_local[1])
    # return feet, inches
    return {'feet': feet, 'inches': inches} # create a dictionary and return key-value pairs


def convert_to_metric(feet_arg, inches_arg):
    meters = (feet_arg * 0.3048) + (inches_arg * 0.0254)
    return meters

if __name__ == '__main__':
    print('This conditional IF BLOCK can be used for scripting testing and/or debugging purposes.')
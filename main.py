import re


def check_size(size):
    last = 0
    if len(size) > 5:
        return 'Incorrect size: Too many sizes'
    for x in size:
        if re.search('\.', x):
            print('X is: ', x)
            return "Incorrect size: Decimal number in size"
        if x == '0':
            return 'Incorrect size: Size too small'
        if int(x) > 48:
            return 'Incorrect size: Size too big'
        if int(x) <= last:
            return 'Incorrect size: Not in ascending order'
        last = int(x)

# NAME
# Additional functions
def has_numbers(inputString):
    return bool(re.search(r'\d', inputString))

def check_name(name):
    print('LENGHT IS: ', len(name))
    if (len(name) < 2):
        return 'Incorrect name: Name too short'
    if (len(name) > 15):
        return 'Incorrect name: Name too long'
    if not name.isalpha():
        return 'Incorrect name: Special characters in name'



# FORMAT
# Additional functions
def is_number(size):
    for x in size:
        print('SIZE IS: ', x)
        if re.search('[a-zA-Z]', x):
            print('NON DIGIST')
            return False
    return True


def valid_number(size):
    for i in size:
        if ' ' in i:
            return False
    return True


# Check if drink meets format constraints
def check_format(name, size):
    if name == '':
        return 'Incorrect format: No name found'
    if not size:
        return 'Incorrect format: No sizes provided'
    if not (name.isalpha()):
        return 'Incorrect format: Non letter in name'
    if not valid_number(size):
        return 'Incorrect format: Space in size'
    if not is_number(size):
        return 'Incorrect format: Letters in size'


# Check if drink meets all requirements
def add_drink(string):
    # Parsing input
    values = string.split(',')

    values[0] = values[0].replace(' ', '')
    for i in range(1, len(values)):
        values[i] = values[i].lstrip()


    name = values[0]
    size = values[1:len(values)]
    # print(name)
    # print(size)

    # Check constraints
    # Format
    format = check_format(name, size)
    if format:
        # print(format)
        return format
    # Names
    name = check_name(name)
    if name:
        # print(name)
        return name
    # Sizes
    size = check_size(size)
    if size:
        print("SIZE IS: ", size)
        return size
    print('Drink has been added')
    return "Drink has been added"

def main(string):
    add_drink(string)


if __name__ == '__main__':
    main('xy, 0')


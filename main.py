def main():
    # TODO: set up main function
    location = getLocation()                    # get location
    name = getName()                            # get establishment
    number = getNumber()                        # number of bathrooms
    types = getType(number)                     # bathroom types (men, women, unisex, family)
    changingTable = getChangingTable(types)     # changing table? which?
    needle = getNeedle()                        # needle disposal?
    rating = getRating()                        # rating
    comment = getComment()                      # comments

    print(location)
    print(name)
    print(number)
    print(types)
    print(changingTable)
    print(needle)
    print(rating)
    print(comment)


def getLocation():
    return input('Enter the name of a location: ')

def getName():
    return input('Enter the name of an establishment: ')

def getNumber():
    return int(input('How many bathrooms?: '))

def getType(num):
    types = []
    while num > 0:
        types.append(input('What type of bathroom is this?: '))
        num -= 1
    return types

def getChangingTable(types):
    tables = {}
    for b in types:
        yesNo = input(f'Is there a changing table in the {b} bathroom? (\'y\' or \'n\'): ')
        if yesNo == 'y':
            tables[b] = True
        elif yesNo == 'n':
            tables[b] = False
    return tables


def getNeedle():
    needle = input('Does this bathroom have a needle disposal? (\'y\' or \'n\'): ')
    if needle == 'y':
        return True
    elif needle == 'n':
        return False

def getRating():
    # stars = [1, 2, 3, 4, 5]
    return int(input('Enter a rating 1-5: '))

def getComment():
    return input('Comments?: ')


if __name__ == '__main__':
    main()
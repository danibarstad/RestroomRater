def main():
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
    """ gets location from user """
    # TODO: make sure location is valid
    
    return input('Enter the name of a location: ')

def getName():
    """ gets names of establishmen of bathroom(s) to be rated """
    # TODO: location should generate list of establishments. user should not enter manually

    return input('Enter the name of an establishment: ')

def getNumber():
    """ the number of bathrooms in a single establishment """
    # TODO: either choose from list or add validation for int

    return int(input('How many bathrooms?: '))

def getType(num):
    """ get the type of bathroom for each bathroom in an establishment """
    # TODO: user should choose from a list

    types = []
    while num > 0:
        types.append(input('What type of bathroom is this?: '))
        num -= 1
    return types

def getChangingTable(types):
    """ returns True or False whether a bathroom has a changing table or not """
    # TODO: can you do this using a check box?

    tables = {}
    for b in types:
        yesNo = input(f'Is there a changing table in the {b} bathroom? (\'y\' or \'n\'): ')
        if yesNo == 'y':
            tables[b] = True
        elif yesNo == 'n':
            tables[b] = False
    return tables


def getNeedle():
    """ returns True if an establishment's bathrooms have needle disposal boxes """
    # TODO: simple check box. should we you do for each bathroom or for the whole establishment?

    needle = input('Does this bathroom have a needle disposal? (\'y\' or \'n\'): ')
    if needle == 'y':
        return True
    elif needle == 'n':
        return False

def getRating():
    """ get user's rating for an establishment's bathroom(s) """
    # TODO: choose from list instead of manual input

    # stars = [1, 2, 3, 4, 5]
    return int(input('Enter a rating 1-5: '))

def getComment():
    """ get user's overall comments for an establishment's bathroom(s) """

    return input('Comments?: ')


if __name__ == '__main__':
    main()
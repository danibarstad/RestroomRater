import yelp

def main():
    location = yelp.get_location()                      # get location
    names = yelp.get_name(location)                     # gets list of establishments
    index = display_names(names)                        # displays list of establishments and user chooses which one to evaluate
    public = public_bathroom(names, index)              # does this establishment have public restrooms?
    if public == True:
        numberOf = get_number()                         # number of bathrooms
        types = get_type(numberOf)                      # bathroom types (men, women, unisex, family)
        changingTable = get_changing_table(types)       # changing table? which?
        needleDisposal = get_needle()                   # needle disposal?
        handicap = get_handicap()                       # handicap accessibility
        rating = get_rating()                           # rating
        comment = get_comment()                         # comments

        display_output(location, names, index, numberOf, types, changingTable, needleDisposal, handicap, rating, comment)
    else:
        print('oh well!')


def display_output(location, names, nameNum, bathrooms, types, tables, needle, handicap, rating, comment):
    print('*****************')
    print(f'Location: {location}')
    print(f'Name: {names[nameNum-1]}')
    print(f'Number of bathrooms: {bathrooms}')
    print(f'Types of bathrooms: {types}')
    print(f'Does this bathroom have a changing table?: {tables}')
    print(f'Does this bathroom have a needle disposal box?: {needle}')
    print(f'Is this bathroom handicap accessible?: {handicap}')
    print(f'Rating: {rating}/5')
    print(f'Comments: {comment}')
    # print(name)
    print('*****************')

def public_bathroom(name, num):
    """ checks if the establishment has a public bathroom or not """

    publicBath = input(f'Does {name[num-1]} have a public bathroom? (\'y\' or \'n\'): ')
    if publicBath == 'y':
        return True
    elif publicBath == 'n':
        return False

def display_names(names):
    """ display list of restaurants in area """

    counter = 0
    print('Choose a restaurant:')
    for n in names:
        counter += 1
        print(f'{counter}. {n}')
    return int(input('Enter a number: '))

def get_number():
    """ the number of bathrooms in a single establishment """
    # TODO: either choose from list or add validation for int

    return int(input('How many bathrooms?: '))

def get_type(num):
    """ get the type of bathroom for each bathroom in an establishment """
    # TODO: user should choose from a list

    types = []
    while num > 0:
        types.append(input('What type of bathroom is this?: '))
        num -= 1
    return types

def get_changing_table(types):
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

def get_needle():
    """ returns True if an establishment's bathrooms have needle disposal boxes """
    # TODO: simple check box. should we you do for each bathroom or for the whole establishment?

    needle = input('Does this bathroom have a needle disposal? (\'y\' or \'n\'): ')
    if needle == 'y':
        return True
    elif needle == 'n':
        return False

def get_handicap():
    """ returns True if the bathrooms are handicap accessible """
    # TODO: should do this for each bathroom?

    handicap = input('Is this bathroom handicap accessible? (\'y\' or \'n\'): ')
    if handicap == 'y':
        return True
    elif handicap == 'n':
        return False

def get_rating():
    """ get user's rating for an establishment's bathroom(s) """
    # TODO: choose from list instead of manual input

    # stars = [1, 2, 3, 4, 5]
    return int(input('Enter a rating 1-5: '))

def getComment():
    """ get user's overall comments for an establishment's bathroom(s) """

    return input('Comments?: ')


if __name__ == '__main__':
    main()
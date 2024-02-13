#CS175
#Jimmy Kong
#restaurant

question = True

while True:
    vegetarian = str(input('Is anyone in your party vegetarian?: '))
    vegan = str(input('Is anyone in your party vegan?: '))
    gluten_free = str(input('Is anyone in your party gluten_free?: '))

    print()
    print('Here are your restaurant choices:')

    if (vegetarian == 'no') and (vegan == 'no') and (gluten_free == 'no'):
        print("Joe's Gourmet Burgers \nMama's Fine Italian \nMain Street Pizza Company \nCorner Cafe \nThe Chef's Kitchen")
                
    elif (vegetarian == 'yes') and (vegan == 'no') and (gluten_free == 'no'):
        print("Mama's Fine Italian \nMain Street Pizza Company \nCorner Cafe \nThe Chef's Kitchen")

    elif (vegetarian == 'no') and (vegan == 'no') and (gluten_free == 'yes'):
        print("Main Street Pizza Company \nCorner Cafe \nThe Chef's Kitchen")

    elif (vegetarian == 'yes') and (vegan == 'no') and (gluten_free == 'yes'):
        print("Main Street Pizza Company \nCorner Cafe \nThe Chef's Kitchen")

    elif (vegetarian == 'no') and (vegan == 'yes') and (gluten_free == 'no'):
        print("Corner Cafe \nThe Chef's Kitchen")

    elif (vegetarian == 'no') and (vegan == 'yes') and (gluten_free == 'yes'):
        print("Corner Cafe \nThe Chef's Kitchen")

    elif (vegetarian == 'yes') and (vegan == 'yes') and (gluten_free == 'no'):
        print("Corner Cafe \nThe Chef's Kitchen")

    elif (vegetarian == 'yes') and (vegan == 'yes') and (gluten_free == 'yes'):
        print("Corner Cafe \nThe Chef's Kitchen")

    print()
    question = input('Do you want to continue?: ')

    while question == True:
        continue
    if question == 'no':
        break
             


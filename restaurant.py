#CS-175L-02
#Jimmy F Kong

vegetarian = str(input('Is anyone in your party vegetarian?: '))
vegan = str(input('Is anyone in your party vegan?: '))
gluten_free = str(input('Is anyone in your party gluten_free?: '))

print()
print('Here are your restaurant choices:')

if (vegetarian == 'No' or vegetarian == 'no') and (vegan == 'No' or vegan == 'no') and (gluten_free == 'No' or gluten_free == 'no'):
    print("Joe's Gourmet Burgers \nMama's Fine Italian \nMain Street Pizza Company \nCorner Cafe \nThe Chef's Kitchen")

elif (vegetarian == 'Yes' or vegetarian == 'yes') and (vegan == 'No' or vegan == 'no') and (gluten_free == 'No' or gluten_free == 'no'):
    print("Mama's Fine Italian \nMain Street Pizza Company \nCorner Cafe \nThe Chef's Kitchen")

elif (vegetarian == 'No' or vegetarian == 'no') and (vegan == 'No' or vegan == 'no') and (gluten_free == 'Yes' or gluten_free == 'yes'):
    print("Main Street Pizza Company \nCorner Cafe \nThe Chef's Kitchen")

elif (vegetarian == 'Yes' or 'yes') and (vegan == 'No' or vegan == 'no') and (gluten_free == 'Yes' or 'yes'):
    print("Main Street Pizza Company \nCorner Cafe \nThe Chef's Kitchen")

elif (vegetarian == 'No' or vegetarian == 'no') and (vegan == 'Yes' or vegan == 'yes') and (gluten_free == 'No' or gluten_free == 'no'):
    print("Corner Cafe \nThe Chef's Kitchen")

elif (vegetarian == 'No' or vegetarian == 'no') and (vegan == 'Yes' or vegan == 'yes') and (gluten_free == 'Yes' or gluten_free == 'yes'):
    print("Corner Cafe \nThe Chef's Kitchen")

elif (vegetarian == 'Yes' or vegetarian == 'yes') and (vegan == 'Yes' or vegan == 'yes') and (gluten_free == 'No' or gluten_free == 'no'):
    print("Corner Cafe \nThe Chef's Kitchen")

elif (vegetarian == 'Yes' or vegetarian == 'yes') and (vegan == 'Yes' or vegan == 'yes') and (gluten_free == 'Yes' or gluten_free == 'yes'):
    print("Corner Cafe \nThe Chef's Kitchen")
    
else:
    print('Please answer with only "yes" or "no"')


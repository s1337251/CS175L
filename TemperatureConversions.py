def main():
    controlLoop()

def controlLoop():
    #Inputs 'Do you want to do some conversions(Yes or No)?'
    decision = (input('Do you want to do some conversions (yes or no)? '))
    if decision == 'yes':
        repeat()
    elif decision == 'no':
        print('Goodbye!')
    else:
        print('Invalid input')

def repeat():
    #Inputs How many conversions would you like to do this time?
    #for x in range how many
    #doConversion()
    how_many = int(input('How many conversions would you like to do this time? '))
    for x in range(how_many):
        doConversion()

def getFahrenheit():
    #Inputs 'Enter Fahrenheit temperature (must be -50 to 130):'
    #(validation loop)'Please re-enter'
    #return Fahrenheit
    fahrenheit = int(input('Enter temperature in Fahrenheit (must be -50 to 130): '))
    if fahrenheit < -50 or fahrenheit > 130:
        fahrenheit = int(input('Please re-enter: '))
    return fahrenheit

def convertToKelvin():
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Kelvin
    #return Kelvin
    fahrenheit = getFahrenheit()
    kelvin = 273.15 + (fahrenheit-32) * (5/9)
    return kelvin

def convertToCentigrade():
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Centigrade
    #return Centigrade
    fahrenheit = getFahrenheit()
    celsius = (fahrenheit-32) * (5/9)
    return celsius

def doConversion():
    #getFahrenheit(), get back Fahrenheit
    #convertToKelvin(), send Fahrenheit get back Kelvin
    #convertToCentigrade(), sends Fahrenheit gets back Centigrade
    #prints for example: 'Fahrenheit: xx Kelvin xx Centigrade: xx'
    f = getFahrenheit()
    k = convertToKelvin()
    c = convertToCentigrade()
    print('Fahrenheit:', f, 'Kelvin:', k, 'Centigrade:', c)

#Call the main function.
if __name__ == '__main__':
    main()

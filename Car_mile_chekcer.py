# Create a car class
class Car:
    
    # Create a class object attributes
    wheels = 50000
    oil = 6000
    max_miles = 50000
    
    # The init initializes the max_miles data attribute
    # part name will be string and part miles limit will be an int data type
    def __init__(self, miles_driven):
        self.__miles = miles_driven 

     # Create a method that says miles_driven that documents how many miles the user has driven
    def new_miles_driven(self, amount):
        self.__miles += amount

    # The miles_diff method will subtrack the max_miles from the userage
    def miles_diff_wheels(self, wheels):
        if wheels - self.__miles >= 0: 
            print('Your wheels are still good')
        else:
            print('Its now time to change one of your wheels')
            
    # The miles_diff method will subtrack the max_miles from the userage
    def miles_diff_oil(self, oil):
        if oil - self.__miles >= 0: 
            print('Your oil is still good')
        else:
            print('Its now time to change one of your oil')


    # Create a function to return the miles used    
    def get_miles_driven(self):
        return self.__miles 
    
    # Create a function to return how many miles left  
    def get_wheels(self):
        if self.wheels - self.__miles >=0:
            return self.wheels - self.__miles
    
    # Create a function to return how many miles left  
    def get_oil(self):
        if self.oil - self.__miles >= 0: 
            return self.oil - self.__miles
        

if __name__ == "__main__":

    def main():
    
         # Ask the user how many miles they have already driven
        miles_used = int(input('How many miles have you already driven? '))
        
         # Create a Car Objec
        miles_usage = Car(miles_used)

         # Ask the user how many miles they have just driven to get the new miles driven
        new_miles_used = int(input('How many miles did you just drive? '))
        print('I will now document how many miles you just drove: ')
        miles_usage.new_miles_driven(new_miles_used)
        
        # Display how many miles have been used
        print(miles_usage.get_miles_driven())
        
        # Now check if it is time to change any parts
        wheels = 50000
        oil = 6000
        miles_usage.miles_diff_wheels(wheels)
        miles_usage.miles_diff_oil(oil)
        
        # Now return the left over miles
        print(f'You have: {miles_usage.get_wheels()} miles left before changing your wheels')
        print(f'you have: {miles_usage.get_oil()} miles left before changing your oil')
        
# Call back the main function
if __name__ == '__main__':
    main()

#S.McDonald
#My first Python program
#intro.py -- asking user for name, age and income
#MODIFIED: 10/18/2016 -- use functions


#create three functions to take care of Input
def get_name():
    #capture the reply and store it in 'name' variable
    name = input ("what's your name?")
    return name

def get_age():
    #capture the reply, convert to 'int' and store in 'age' variable
    age =  int(input ("How old are you?"))
    return age

def get_income():
    #capture the reply, convert to 'float' and store in 'income' variable
    income = float(input ("what's your income?"))
    return income

#create a main function
def main():
    #call the other functions by their names
    name = get_name() #return the value from function
    age = get_age()
    income = get_income()
    print(name, age, income)

#call the main() function
main()

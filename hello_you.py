name = input("What is your name?: ")


age = input("What is your age?: ")


city = input("In Which you Live?: ")
enjoy = input("What you enjoy doing?: ")

string = "your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name,age,city,enjoy)
print(output)

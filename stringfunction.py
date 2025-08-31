info="hii my name is {2} and my favourate cricketer is {1} and my country is {0}"
name = "harshad"
cricketer = "joss buttler"
country = "india"
print(info.format(country,cricketer,name)) # format replace {} with some data

print(f"hii my name is {name} and my favourate cricketer is {cricketer} and my country is {country}") # we use this also

price = 98.6647764
txt=f"the price of 1 bat is only {price:.2f} dollars" # for conversion of any float value to 2 decimal number only
print(txt)

print(f"hii my name is {{name}} and my favourate cricketer is {{cricketer}} and my country is {{country}}")

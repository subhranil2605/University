# print(mtcars)

Data_Cars <- mtcars # create a variable for the data set

# dimension of the data set
print(dim(Data_Cars))

# names of the variables from the data set 
# column names
print(names(Data_Cars))

# name of each row of the first column
print(rownames(Data_Cars))


# print variable values
print(Data_Cars$mpg)
print(Data_Cars$cyl)
print(Data_Cars$disp)
print(Data_Cars$hp)
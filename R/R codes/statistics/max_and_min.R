# Data_Cars <- mtcars

print(max(Data_Cars$hp))
print(min(Data_Cars$hp))


# which 
# it helps us to find the index number from the data set
print(which.max(Data_Cars$hp))
print(which.min(Data_Cars$hp))

# getting the row name of the data 
print(rownames(Data_Cars)[which.max(Data_Cars$hp)])
print(rownames(Data_Cars)[which.min(Data_Cars$hp)])
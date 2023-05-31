# Data_Cars <- mtcars

# print(Data_Cars)

# find the average weight of the cars
print(mean(Data_Cars$wt))

# Median - middle value of the data set
print(median(Data_Cars$wt))

# Mode - most occuring value from the data set
mode_value <- sort(-table(Data_Cars$wt))[1]

print(mode_value)
# Percentiles are used in statistics 
# to give you a number that describes 
# the value that a given percent of the values are lower than.


# Data_Cars <- mtcars

three_by_four <- quantile(Data_Cars$wt, c(0.75))

print(three_by_four)

# What is the 75. percentile of the weight of the cars?
# The answer is 3.61 or 3 610 lbs, meaning that 
# 75% or the cars weight 3 610 lbs or less:

quntl <- quantile(Data_Cars$wt)
print(quntl)
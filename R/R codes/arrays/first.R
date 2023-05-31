# one dimension array with 24 elements
thisarray <- c(1:24)
thisarray


# create array
multi_array <- array(thisarray, dim = c(4, 3, 2))
multi_array

# access elements
multi_array[2, 3, 2]


# access whole row or column
multi_array[c(1), , 1]

multi_array[,c(2) , 2]

thismatrix <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 3, ncol = 2)


# print the matrix
thismatrix


# accessing matrix elements
thismatrix[2, 2]


# entire row
thismatrix[2,]


# entire column
thismatrix[,2]

# accessing more than one rows/cols
thismatrix[c(1, 2),]
thismatrix[,c(1, 2)]


# add rows / columns from the matrix

# new matrix 3x3
thismatrix <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3, ncol = 3)

thismatrix

# Add columns
new_matrix <- cbind(thismatrix, c(10, 11, 12))
new_matrix

# add rows
new_matrix2 <- rbind(thismatrix, c(4, 7, 10))
new_matrix2


# remove rows or columns
thismatrix <- thismatrix[-c(1), -c(1)]
thismatrix

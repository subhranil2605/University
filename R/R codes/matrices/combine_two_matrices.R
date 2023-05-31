# create two matrices
matrix_1 <- matrix(c("apple", "banana", "cherry", "grape"), nrow = 2, ncol = 2)
matrix_2 <- matrix(c("orange", "mango", "pineapple", "watermelon"), nrow = 2, ncol = 2)

# adding them in a row
adding_row <- rbind(matrix_1, matrix_2)
adding_row

# adding them in a column
adding_column <- cbind(matrix_1, matrix_2)
adding_column

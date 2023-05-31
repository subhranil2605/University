thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)

thismatrix

nrow(thismatrix)
ncol(thismatrix)

# looping through a 2 dimensional matrix
for (row in 1:nrow(thismatrix)) {
  for (col in 1:ncol(thismatrix)) {
    print(thismatrix[row, col])
  }
}




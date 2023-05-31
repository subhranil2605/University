#Question 2
data1 <- rnorm(n = 100, mean = 50, sd = 5)

data2 <- rnorm(n = 100, mean = 51, sd = 5)

# combined
data <- data.frame(cbind(data1, data2))

# staked
data <- stack(data)

res <- t.test(values~ind, data = data)

res


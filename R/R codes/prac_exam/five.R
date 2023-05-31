# question 5
set.seed(123) 
sugar_cookie <- rnorm(30, mean = 9.99, sd = 0.04)

sugar_cookie

# H0 : mu = 10
res <- t.test(sugar_cookie, mu = 10)

res


#H0: The average level of sugar is equal to 10 . H3: The average level of sugar is different than 10
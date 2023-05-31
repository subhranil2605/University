# single point plot
plot(1, 3)

# two points plot
plot(c(1, 5), c(4 ,5))


# multi-points
x <- c(1, 2, 3, 4, 5, 6, 7, 8, 9)
y <- x^2


plot(x, y)


# sequence of points
plot(1:10)

plot(c(1:10), c(100:109),
     main = "Graph Name", xlab = "X-axis", ylab = "Y-axis",
     col = "red",
     cex = 2,
     pch = 0
)



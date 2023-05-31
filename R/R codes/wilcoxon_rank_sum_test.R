std_therapy <- c(75, 8, 9, 8, 9, 15, 20)
new_therapy <- c(8, 10, 9, 60, 15, 20, 33)


data <- data.frame(cbind(std_therapy, new_therapy))

data
summary(data)

data <- stack(data)
data

boxplot(values~ind, col = rainbow(2), data = data)

wilcox.test(
  values ~ ind,
  data = data,
  mu = 0,
  conf.level = 0.05,
  paired = F,
  exact = F,
  correct = T
)

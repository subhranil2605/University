normal <- c(1200, 1000, 980, 900, 750, 800)
osteopenia <- c(1000, 1100, 700, 800, 500, 700)
osteoporesis <- c(890, 650, 1100, 900, 400, 350)


data <- data.frame(cbind(normal, osteopenia, osteoporesis))

data

summary(data)

# stacking groups
data <- stack(data)
data

# plotting the data
library(ggplot2)
ggplot(data, aes(ind, values, fill=values)) + geom_boxplot()

#boxplot(values~ind, data = data)

results <- aov(values ~ ind, data=data)
results

summary.aov(results)


# using lm() function

lm.model <- lm(data$values ~ data$ind)
summary(lm.model)


lm(formula = values ~ ind)

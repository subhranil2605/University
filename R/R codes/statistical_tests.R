my_data <- data.frame(
  name = paste0(rep("M_", 10), 1:10),
  weight = round(rnorm(10, 20, 2), 1)
)
summary(my_data$weight)

# library(ggplot2)
# ggplot(my_data, aes(weight)) + geom_boxplot()
# 
# median(my_data$weight)
# sort(my_data$weight)

res <- t.test(my_data$weight, mu=19.57)
res

res$p.value
res$alternative

mean(my_data$weight)


require(graphics)
d = sleep
View(d)

plot(extra ~ group, data = sleep)


library(ggplot2)

ggplot(d, aes(group, extra, fill=group)) + geom_boxplot()



t.test(extra ~ group, data = sleep)

mtcars_aov <- aov(mtcars$disp ~ factor(mtcars$gear))
summary(mtcars_aov)


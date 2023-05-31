# Question 4
View(mpg)

library(ggplot2)


# summarizes the distribution of hwy with respect drv variable using boxplot
ggplot(mpg, aes(drv, hwy, fill=hwy)) + geom_boxplot()


# Explain the utilization of facet_grid() in the mpg dataset
p <- ggplot(mpg, aes(displ, cty)) + geom_point()

p + facet_grid(rows = vars(drv))

p + facet_grid(vars(drv), vars(cyl))

ggplot(data = mpg) +
  geom_point(mapping = aes(x = hwy, y = cty)) +
  facet_grid(drv ~ cyl)

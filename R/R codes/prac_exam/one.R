# Question 1

data <- read.csv("C:/Users/imsub/Desktop/poisons.csv") %>%
  select(-X) %>% 
  mutate(poison = factor(poison, ordered = TRUE))

# Time: Survival time of the animal
# poison: Type of poison used: factor level: 1,2 and 3
# treat: Type of treatment used: factor level: 1,2 and 3

glimpse(data)

# levels
levels(data$poison)

# compute the count, mean and standard deviation.
data %>%
  group_by(poison) %>%
  summarise(
    count_poison = n(),
    mean_time = mean(time, na.rm = TRUE),
    sd_time = sd(time, na.rm = TRUE)
  )

# plot box plot
library(ggplot2)
ggplot(data, aes(x = poison, y = time, fill = poison)) + geom_boxplot() 


## one way anova test
anova_one_way <- aov(time~poison, data = data)

summary(anova_one_way)

# pairwise comparison
pairwise.t.test(data$time, data$treat)

pairwise.t.test(data$time, data$poison)

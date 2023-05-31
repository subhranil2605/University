library(readr)
salaries <- read_csv("G:/Downloads/Salaries.csv")
View(salaries)
spec(salaries)


unique(salaries$rank)


length(salaries$rank)

dim(salaries)


which(salaries$rank == 'Prof')


sum(as.numeric(rownames(salaries)))

# professor's salary 
sal_prof <- salaries$salary[which(salaries$rank == 'Prof')]

sal_prof

# salaries greater than 137200
salaries$salary[which(salaries$rank == 'Prof' & salaries$salary > 173200)]

# getting the index of the professor which has salary > 173200
index <- which(salaries$rank == 'Prof' & salaries$salary > 173200)
index


prof_173 <- salaries[index, ]
dim(prof_173)


colnames(prof_173)
colnames(prof_173)[3] <- "phd"

colnames(prof_173)[4]
colnames(prof_173)[4] <- "service"

colnames(prof_173)[2]
colnames(prof_173)[2] <- "disc"

# scatter plot
plot(prof_173$phd, prof_173$salary)

# line plot
plot(prof_173$phd, prof_173$salary, type = "l")

x <- prof_173$service

y <- prof_173$salary

# customizing the plot 
plot(x, y, main="My Graph", xlab="phd years", ylab = "salary")


# color
plot(x, y, col = "red")

# size 1 means default and 2 means 100% larger
plot(x, y, cex = 2)


# point shapes
plot(x, y, pch=25)



# histogram
hist(salaries$salary)
colnames(salaries)


# prof and ass prof names who are teaching in discipline B
unique(salaries$rank)

index <- which(salaries$rank == 'Prof' | salaries$rank == 'AssocProf')

prof_and_asso <- salaries[index, ]

index <- which(prof_and_asso$discipline == 'B')

View(prof_and_asso[index, ])



density(salaries$salary)


plot(density(salaries$salary))

hist(salaries$salary)


# females
unique(salaries$sex)


salaries$salary[which(salaries$sex == "Female")]


plot(density(salaries$salary[which(salaries$sex == "Female")]))

plot(density(salaries$salary[which(salaries$sex != "Female")]))



f_prof <- salaries$salary[which(salaries$sex == "Female" & salaries$rank == "Prof")]

m_prof <- salaries$salary[which(salaries$sex != "Female" & salaries$rank == "Prof")]


mean(f_prof)
mean(m_prof)

if (mean(f_prof) > mean(m_prof)) {
  print("Female > Male")
} else {
  print("Male > Female")
}


sd(f_prof)
sd(m_prof)

barplot(m_prof)


# multiple plot in a single plot
par(mfrow=c(2, 2))

plot(density(f_prof))
plot(density(m_prof))

barplot(f_prof)
barplot(m_prof)

#install.packages("ggplot2")

library(ggplot2)


d <- as.data.frame(m_prof)

ggplot(d, aes(m_prof)) + geom_boxplot()

d <- data.frame(m_prof <- m_prof[1:18], f_prof)

View(d)


ggplot(melt(d), aes(variable, value, fill=variable))+geom_boxplot()

library(reshape)


v <- seq(from = 0, to = 1, by = 0.005)
v

v <- seq(0, 1, 0.25)
v

# show the first value
v[1]

# print without the first value
v[-1]



data <- matrix(data = c(1:9), ncol=3)

data <- matrix(1:8, ncol=2, nrow=4, byrow = TRUE)

data <- matrix(1:9, ncol=3, byrow = TRUE, dimnames = list(c("X", "Y", "Z"), c("A", "B", "C")))
data
data <- as.data.frame(data)
data
View(data)

cbind(c(1, 2, 3), c(4, 5, 6))
rbind(c(1, 2, 3), c(4, 5, 6))


data
data[c(1, 2), c(1, 2)]


data <- rbind(data, c(10, 11, 12))
data

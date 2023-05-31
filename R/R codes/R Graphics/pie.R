x <- c(10, 20, 30, 40)

my_label <- c("apple", "banana", "orange", "kola")
colors <- c("blue", "yellow", "green", "black")

pie(x, label = my_label, main = "fruits", col = colors)
  
legend("bottomright", my_label, fill = colors, col = colors)

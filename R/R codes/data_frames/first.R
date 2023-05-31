Data_Frame <- data.frame(
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

Data_Frame


# summarize the data frame

summary(Data_Frame)


# access items
Data_Frame[1]

# or 
Data_Frame[["Training"]]

# or 
Data_Frame$Training
Data_Frame$Pulse

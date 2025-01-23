library(tidyverse)

occupation_data <- read_csv("they_all_models.csv" ) 


ggplot(data = occupation_data, aes(x = " ", y = occupation, fill = occupation)) + 
  geom_col() +
  theme_light() +
  ggtitle( "Percentage of Each Occupation (%)") +
  labs(y =  " ",  x = " " ) +
  geom_text(aes(label = "Model 100%")) +
  coord_polar(theta = "y") + 
  guides(fill = guide_legend(title = "Occupation")) +
  scale_fill_discrete(labels = c("Model"))
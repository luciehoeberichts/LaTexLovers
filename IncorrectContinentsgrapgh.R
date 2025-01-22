library(tidyverse)
shoe_size_by_wikepedia <- read_csv("data_foot_size_new.csv") |>
  na.omit() 
  

ggplot(data = shoe_size_by_wikepedia) + 
  aes( y = shoeSize, x = continent ) + 
  labs(y =  "Average Shoe Size in Celebrities ",  x = "Continent") + 
  ggtitle("Average Shoe Size in Celebrities Per Country") + 
  geom_col()

ggsave("wikepedia.pdf")
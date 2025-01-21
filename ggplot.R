library(tidyverse)
shoe_size_by_country <- read_csv("shoe-size-by-country-2024.csv") |>
  mutate( total = (AverageWomenShoeSize + AverageMenShoeSize) /2 ) 


# Scatterplot 
ggplot( data = shoe_size_by_country) + 
  aes( y = total, x = country) + 
  labs( y =  "Average Shoe Size",  x = "Country") + 
  ggtitle("Average Shoe Size Per Country") +  
  geom_col()
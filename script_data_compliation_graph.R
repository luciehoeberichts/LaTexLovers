libraryrary(tidyverse)
shoe_size_by_wikepedia <- read_csv("data_foot_size.csv") |>
  na.omit() 


ggplot(data = shoe_size_by_wikepedia) + 
  aes( y = shoeSize, x = continent ) + 
  labs(y =  "Sum of (U.S) shoe sizes",  x = "Continent") + 
  ggtitle("Sum of shoe sizes per continent") + 
  geom_col()

ggsave("sum_shoe_sizes_continent.pdf")
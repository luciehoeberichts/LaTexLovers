library(tidyverse)

shoe_size_by_wikepedia <- read_csv("data_foot_size.csv") |>
  na.omit() |>
  mutate(continent = fct_infreq(continent))


ggplot(data = shoe_size_by_wikepedia) + 
  aes(x = continent) + 
  labs(y =  "Count of shoe sizes",  x = "Continent") + 
  ggtitle("Count of shoe sizes per continent") + 
  theme_light() + 
  geom_bar(stat="count", fill = "darkblue")

ggsave("count_shoe_sizes_continent.pdf")


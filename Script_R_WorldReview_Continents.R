library(tidyverse)
shoe_size_by_worldreview <- read_csv("data_world.csv") |>
  na.omit() |> 
  group_by(continent) |> 
  summarise (mean_per_con = mean(average_shoe_size)) 



ggplot(data = shoe_size_by_worldreview) + 
  aes( y = mean_per_con, x = continent ) + 
  labs(y =  "Average Shoe Size (US)",  x = "Continent") + 
  ggtitle("Average Shoe Size per Continent") + 
  theme_light() +
  geom_col( fill = "lightblue")

ggsave("worldreview_continent.pdf")
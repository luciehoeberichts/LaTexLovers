library(tidyverse)

shoe_size_by_wikepedia <- read_csv("data_foot_size.csv") |>
  na.omit() |> 
  filter(shoeSize > 0) |>
  filter(shoeSize < 20) |> 
  group_by(place)|>
  summarise(continent, mean_shoeSize = mean(shoeSize)) |> 
  ungroup() |> 
  group_by(continent) |> 
  summarise(wikipedia = mean(mean_shoeSize)) 

print(shoe_size_by_wikepedia)

shoe_size_by_worldreview <- read_csv("data_world.csv") |>
  na.omit() |> 
  group_by(continent) |> 
  summarise (world_review = mean(average_shoe_size))

shoe_size_combined <- full_join( shoe_size_by_wikepedia, shoe_size_by_worldreview) |>
  pivot_longer ( cols = -continent, names_to = "dataset", values_to = "mean_per_con") |> 
  filter( continent != "Unknown") |> 
  filter( continent != "Oceania")

ggplot(data = shoe_size_combined) + 
  aes( y = mean_per_con, x = continent, fill = dataset ) + 
  labs(y =  "Average Shoe Size (US) ", x = "Continent") + 
  ggtitle("Average Shoe Size Per Continent") + 
  theme_light() +
  geom_col(position = position_dodge())

ggsave("wikepedia2.pdf")

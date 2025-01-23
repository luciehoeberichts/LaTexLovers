library(tidyverse)
 shoe_size_by_wikepedia <- read_csv("data_foot_size.csv") |>
  filter(shoeSize > 0) |>
  filter(shoeSize < 20) |> 
  filter(country == "Brazil"| country == "UnitedStates" |country == "UnitedKingdom") |>
  group_by(country)|>
  summarise(Model = mean(shoeSize)) 



shoe_size_by_worldreview <- read_csv("data_world.csv") |>
  na.omit() |> 
  filter(country == "Brazil"| country == "UnitedStates" |country == "UnitedKingdom") |>
  group_by(country) |> 
  summarise (Population = mean(average_shoe_size))

shoe_size_combined <- full_join( shoe_size_by_wikepedia, shoe_size_by_worldreview) |>
  pivot_longer (cols = -country, names_to = "People", values_to = "Model") 

ggplot(data = shoe_size_combined) + 
  aes( y = Model, x = country, fill = People ) + 
  labs(y =  "Average Shoe Size (US) ", x = "Country") + 
  ggtitle("Average Shoe Size Per Country") + 
  theme_light() +
  geom_col(position = position_dodge())

ggsave("wikepedia2.pdf")
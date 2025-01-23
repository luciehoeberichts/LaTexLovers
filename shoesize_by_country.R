library(tidyverse)

shoe_size_by_wikepedia <- read_csv("data_foot_size.csv") |>
  na.omit() |>
  mutate(place = fct_lump_n(place, n=10)) |>
  mutate(place = fct_infreq(place)) |>
  select(-continent) |>
  filter(place != "Other")

ggplot(data = shoe_size_by_wikepedia) + 
  aes(x = place) + 
  labs(y =  "Count of shoe sizes",  x = "Country") + 
  ggtitle("Count of shoe sizes per country") + 
  theme_light() + 
  geom_bar(stat="count", fill = "darkblue")

ggsave("count_shoe_size_per_country.pdf")

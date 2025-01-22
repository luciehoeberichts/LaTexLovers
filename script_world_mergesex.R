library(tidyverse)
shoe_size_by_country <- read_csv("shoe-size-by-country-2024.csv") |>
  mutate( total = (AverageWomenShoeSize + AverageMenShoeSize) /2 ) |> 
  select(country,total)

write.csv(shoe_size_by_country, file = "WorldReviewdata.csv", row.names = FALSE)

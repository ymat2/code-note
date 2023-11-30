## Environment Variables
.libPaths()
sessionInfo()

## Installing packages
install.packages("languageserver")
install.packages("tidyverse")
install.packages("BiocManager")
BiocManager::install("ggtree")

library(conflicted)
library(tidyverse)

mpg2 = mpg |>
  dplyr::filter(year >= 2000) |>
  dplyr::select(displ, cty, drv)

ggplot(mpg2) +
  aes(x = displ, y = cty, color = drv) +
  geom_point() +
  scale_color_viridis_d() +
  theme_classic()

# test code to use Japanese character in WSL
# WSLで日本語使うためのテストコード

library(conflicted)
library(tidyverse)

ggplot(mpg) +
  aes(x = displ, y = cty, color = drv) +
  geom_point() +
  labs(x = "ディスプレイスメント", y = "市街地燃費") +
  theme_classic(base_size = 22)

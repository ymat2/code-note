library(conflicted)
library(tidyverse)


## sep comma 4 longer ----------------------------------------------------------

df = data.frame(
  chr = c("1", "1", "1", "2", "2", "2"),
  start = c("100", "100", "100", "105", "105", "205"),
  end = c("101", "101", "101", "106", "106", "206"),
  seq = c(
    "ATGATGATG,ATCATCATC,AGGAGGAGG",
    "ATGATGATG,ATCATCATC,AGGAGGAGG,CCGCCGTTG",
    "ATGATGATG,ATCATCATC,AGGAGGAGG,AGGAGGCCCTTTGGG,AAATTT",
    "ATGATGATG,ATCATCATC",
    "ATGATGATG,ATCATCATC,AGGAGG,ATGATGATG,ATCATC,AGGAGGAGG",
    "ATGATGATGATTGGCCTGG"
  ),
  strain = c("A", "B", "C", "A", "D", "D")
)

df_sep = df |>
  tidyr::separate(seq, into = letters, sep = ",", extra = "merge", fill = "right") |>
  dplyr::select(!where(~all(is.na(.)))) |>
  tidyr::pivot_longer(4:9, names_to = "ll", values_to = "seq") |>
  tidyr::drop_na() |>
  mutate(seq_length = nchar(seq))

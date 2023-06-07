BiocManager::install("fgsea")
BiocManager::install("org.Hs.eg.db")

library(conflicted)
library(tidyverse)
library(fgsea)
library(org.Hs.eg.db)

gene_symbol <- as.list(org.Hs.egSYMBOL)
scores = runif(length(gene_symbol), 0, 1)
named_scores = setNames(scores, gene_symbol)

kegg_pathways = gmtPathways("./rstat/c2.cp.kegg.v2022.1.Hs.symbols.gmt")

fgseaRes <- fgsea(
  pathways = kegg_pathways,
  stats    = named_scores,
  minSize  = 15,  # 15
  maxSize  = length(named_scores)-1,  # 500
  scoreType = "pos"  # c("std", "pos", "neg")
  )

head(fgseaRes %>% arrange(pval))

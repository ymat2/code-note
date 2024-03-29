library(conflicted)
library(tidyverse)
library(phytools)
library(ggtree)


## Simulating Brownian motion
# http://phytools.org/eqg/Exercise_4.1/
t = 0:100
sig2 = 0.01
x = rnorm(n = length(t)-1, sd = sqrt(sig2))
x = c(0, cumsum(x))
plot(t, x, type = "l", ylim = c(-2,2))

nsim = 100
X = matrix(
  rnorm(n = nsim*length(t)-1, sd = sqrt(sig2)),
  nsim,
  length(t)-1
)
X = cbind(rep(0, nsim), t(apply(X, 1, cumsum)))
plot(t, X[1, ], xlab = "time", ylab = "phenotype", ylim = c(-2, 2), type = "l")
apply(X[2:nsim, ], 1, function(x, t) lines(t, x), t = t)

X <- matrix(0, nsim, length(t))
for (i in 1:nsim) X[i, ] <- c(0, cumsum(rnorm(n = length(t) - 1, sd = sqrt(sig2))))
plot(t, X[1, ], xlab = "time", ylab = "phenotype", ylim = c(-2, 2), type = "l")
for (i in 1:nsim) lines(t, X[i, ])

t = 100  # total time
n = 30  # total taxa
b = (log(n) - log(2))/t
tree <- pbtree(b = b, n = n, t = t, type = "discrete")
plotTree(tree)

## simulate evolution along each edge
X <- lapply(tree$edge.length, function(x) c(0, cumsum(rnorm(n = x, sd = sqrt(sig2)))))
## reorder the edges of the tree for pre-order traversal
cw <- reorder(tree)
## now simulate on the tree
ll <- tree$edge.length + 1
for (i in 1:nrow(cw$edge)) {
  pp <- which(cw$edge[, 2] == cw$edge[i, 1])
  if (length(pp) > 0) 
    X[[i]] <- X[[i]] + X[[pp]][ll[pp]] else X[[i]] <- X[[i]] + X[[1]][1]
}
## get the starting and ending points of each edge for plotting
H <- nodeHeights(tree)
## plot the simulation
plot(H[1, 1], X[[1]][1], ylim = range(X), xlim = range(H), xlab = "time", ylab = "phenotype")
for (i in 1:length(X)) lines(H[i, 1]:H[i, 2], X[[i]])
## add tip labels if desired
yy <- sapply(1:length(tree$tip.label), function(x, y) which(x == y), y = tree$edge[,2])
yy <- sapply(yy, function(x, y) y[[x]][length(y[[x]])], y = X)
text(x = max(H), y = yy, tree$tip.label)

## simulate Brownian evolution on a tree with fastBM
x <- fastBM(tree, sig2 = sig2, internal = TRUE)
## visualize Brownian evolution on a tree
phenogram(tree, x, spread.labels = TRUE, spread.cost = c(1, 0))

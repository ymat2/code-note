library(conflicted)
library(tidyverse)
library(phytools)
library(ggtree)

## Rでブラウン運動進化シミュレーションしたい！したいの！ -----------------------

### 使うパッケージ: phytools
### 参考: http://phytools.org/eqg/Exercise_4.1/


## まあとにかくやってみる ------------------------------------------------------

### 100世代、sigma=0.01 のブラウン運動を可視化する
t = 0:100  # generation
sig2 = 0.01  # 分散を決める。でかいほど形質がばらつく
x = rnorm(n = length(t)-1, sd = sqrt(sig2))
x = c(0, cumsum(x))
plot(t, x, type = "l", ylim = c(-2,2))

### 軽く関数化してみる
simBM = function(gen, sigma, alpha = 0) {
  delta = rnorm(n = length(gen)-1, sd = sqrt(sigma))
  pheno = c(alpha, alpha + cumsum(delta))
  df_bm = data.frame(
    t = gen,
    x = pheno
  )
  return(df_bm)
}

simBM(gen = 0:100, sigma = 0.01, alpha = 0) |>
  ggplot2::ggplot() +
  aes(t, x) +
  geom_line() +
  scale_y_continuous(limits = c(-2, 2)) +
  theme_bw() +
  theme(panel.grid = element_blank())


## 系統樹上でシミュレーションする
set.seed(1234)

t = 100
n = 3
b = (log(n)-log(2))/t
tree<-pbtree(b=b,n=n,t=t,type="discrete")
plot(tree)

# 枝長を世代時間とするBMをシミュレート
sig2 = 0.02
X<-lapply(tree$edge.length,function(x) c(0,cumsum(rnorm(n=x,sd=sqrt(sig2)))))
# ツリーのエッジを並べ替える(for what?)
# cw<-reorder(tree)
# れっつシミュレート？
ll<-tree$edge.length+1
for(i in 1:nrow(tree$edge)){
  pp<-which(tree$edge[,2]==tree$edge[i,1])
  if(length(pp)>0) X[[i]]<-X[[i]]+X[[pp]][ll[pp]]
  else X[[i]]<-X[[i]]+X[[1]][1]
}
## get the starting and ending points of each edge for plotting
H<-nodeHeights(tree)
## plot the simulation
plot(H[1,1],X[[1]][1],xlim=range(H),xlab="time",ylab="phenotype",ylim = c(-2,2))
for(i in 1:length(X)) lines(H[i,1]:H[i,2],X[[i]])
## add tip labels if desired
yy<-sapply(1:length(tree$tip.label),function(x,y) which(x==y),y=tree$edge[,2])
yy<-sapply(yy,function(x,y) y[[x]][length(y[[x]])],y=X)
text(x=max(H),y=yy,tree$tip.label)

### これを理解しつつ関数化したい


### scrible
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


# pythonは基本的に参照渡し

## lとmが参照する先を変更するので両方変わる
l = [1,2,3]
m = l
l[0] = 0
m

## l に新しい参照を与えるのでmの参照先は変更されない
l = [1,2,3]
m = l
l = [4,5,6]
m

# strはimmutable
s = "hoge"
s[1]
s[1] = "a"

# ll
vec = [0,0,0]
vec[2] = vec[1] + 1
vec
vec[1] = vec[0] + 1
vec

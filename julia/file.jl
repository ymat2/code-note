# exec: julia file.jl file

lst = []

open(ARGS[1]) do f
for line in eachline(f)
  tbs = split(chomp(line), "\t")
  push!(lst, tbs[2])
end
end

println(join(lst, ","))

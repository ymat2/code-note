println("##### STDOUT #####")
println("Hello World")


println("##### IF-ELSE #####")
if true
  println("Hello")
else
  println("Bye")
end

i = 12
if i > 10
  println("i>10")
elseif i > 8
  println("10>=i>8")
else
  println("8>=i")
end


println("##### AND/OR #####")
println(true && false)
# false
println(true || false)
# true
println(true && !true)
# false
println(true || !true)
# true


println("##### ARRAY #####")
chrs = ["hoge", "fuga", "piyo"]
println(chrs)
println(chrs[1])
println(chrs[end])
println(";;;")


println("##### HASH #####")
dict = Dict("a"=>"hoge", "b"=>"fuga", "c"=>"piyo")
println(dict["a"])

dicts = Dict(:a=>"hoge", :b=>"huga", :c=>"piyo")
println(dicts[:b])

for (key, value) in dict
  println("key = $key")
  println("value = $value")
end


println("##### LOOPING #####")
for i in 1:5
  println("Hello world")
end

chrs = ["hoge", "fuga", "piyo"]
for i in chrs
  println(i)
end

chrs = ["hoge", "fuga", "piyo"]
foreach(i -> println(i), chrs)


println("##### FUNCTION #####")
function hypo(x, y)
  return sqrt(x^2 + y^2)
end

println(hypo(3,4))

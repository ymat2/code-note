puts "##### STDOUT #####"
puts 'Hello World'
printf("Hello Ruby\n")


puts "##### IF-ELSE #####"
if true
	puts 'Hello'
else
	puts 'Bye'
end

i = 12
if i>10
	puts "i>10"
elsif i>8
	puts "10>=i>8"
else
	puts "8>=i"
end


puts "##### AND/OR #####"
puts true && false  # >>> false
puts true || false  # >>> true
puts true && !true  # >>> false
puts true || !true  # >>> true


puts "##### ARRAY #####"
languages = ["hoge", "fuga", "piyo"]
puts languages[-1]

languages.each do |i|
  puts i
end


puts "##### HASH #####"
dict = {"a"=>"hoge", "b"=>"fuga", "c"=>"piyo"}
puts dict["a"]

dicts = {a:"hoge", b:"huga", c:"piyo"}
puts dicts[:b]

dict.each do |key, value|
   puts "#{key}の値は#{value}だよ。"
end


puts "##### LOOPING #####"
5.times do
  puts "Hello world"
end

i = 0
while i < 5 do
  puts i
  i+=1
end

chrs = ["hoge", "fuga", "piyo"]
for i in chrs
  puts i
end


puts "##### FUNCTION #####"
def hypo(x, y)
  z = (x**2+y**2)**0.5
  return z
end

puts hypo(3,4)

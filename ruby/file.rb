# exec: ruby file.rb file

## open()
lst = []

File.open(ARGV[0]) do |f|
  f.each_line do |line|
    tbs = line.chomp.split("\t")
    lst << tbs[1]
  end
end

puts lst.join(",")


## foreach
lst2 = []
File.foreach(ARGV[0]) do |line|
  tbs = line.chomp.split("\t")
  lst2 << tbs[0]
end

puts lst2.join(";")

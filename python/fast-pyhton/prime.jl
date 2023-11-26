function isPrime(n::Int64)
  bool_ = true
  for i in 2:n-1
    if n % i == 0
      bool_ = false
  break
    end
  end
  return bool_
end

n = 50000
cnt = 0
for i in 1:n
  if isPrime(i)
    global cnt += 1
  end
end

println(cnt)

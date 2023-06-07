package main

func main() {
	var n = 100000
	var cnt = 0
	for i:=0; i<n; i++ {
		if is_prime(i+1) {
			cnt += 1
		} else {
			continue
		}
	}
	println(cnt)
}

func is_prime(n int) bool {
	var prime bool = true
	for i:=2; i<n; i++ {
		if n%i == 0 {
			prime = false
			break
		}
	}
	return prime
}

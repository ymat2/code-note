def main():
	n = 100000
	cnt = 0
	for i in range(n):
		if isPrime(i+1):
			cnt += 1

	print(cnt)


def isPrime(n):
	bool_ = True
	for i in range(2,n):
		if n%i==0:
			bool_ = False
			break
	return bool_


if __name__ == "__main__":
	main()

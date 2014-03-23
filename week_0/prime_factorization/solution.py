def is_prime(n):
	if n == 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True



def prime_factorization(n):
	i = 2
	res = []
	while n != 1:
		count = 0 #pazi stepenta
		if is_prime(i):
			while n % i == 0:
				count += 1
				n /= i
			if count != 0:
				res.append((i, count))
		i += 1
	return res		

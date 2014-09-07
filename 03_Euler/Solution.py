def findLargestPrimeFactors(number):
	# Prime numbers have to be above 1
	i = 2

	# Finding largest prime number
	# Enter first loop by multiplying "i" together recieving a Prime Factor
	# Enter loop if prime factor is under given number therefore exiting loop
	# when Largest prime factor is found.
	while i * i < number:
			# Continue looping until a prime factor is found; if no factor found increase "i" by one
	    while number%i == 0:
	    		# If prime factor found divide number by "i" recieving factor
	        number = number / i

	    i = i + 1

	print (number)

def main():
	findLargestPrimeFactors(600851475143)

if __name__ == '__main__':
	main()
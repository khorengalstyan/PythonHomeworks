import math



#Check if number is prime or not
def isPrime(number):
	for i in range(2, int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False
	return True




#Generate prime numbers infinitely. 
def primeNumberGenerator():
	number = 2
	while(1):

    		if (isPrime(number)):
    			yield number
    		number = number + 1
		
# Print generated prime numbers
for value in primeNumberGenerator():
	print(value)

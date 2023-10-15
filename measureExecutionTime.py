import math
import time

# measure execution time of function. 
def measureExecutionTime(function):
	def wrapFunction(*args, **kwargs):
		startTime = time.time()
		result = function(*args, **kwargs)
		endTime = time.time()
		executionTime = endTime - startTime
		print(f"Function {function.__name__} took {executionTime} to execute")
		return result
	return wrapFunction



@measureExecutionTime
def primeNumberGenerator(finish):
	number = 2
	while(1):
		if (number >= finish):
			break
		else:
    			isPrime = 1
    			for i in range(2, int(math.sqrt(number) + 1)):
        			if number % i == 0:
            				isPrime = 0
    			if (isPrime == 1):
    				yield number
    			number = number + 1
		
	
primeNumberGenerator(10000000)

def caching_fibonacci():
    """
    The function is used for creating inner fibonacci(n) function and empty cache = {} dictionary.  .
    """
    cache = {} #Create a dictionary for saving cached values
    def fibonacci(n):
        """
        The function is used for recursive calculation of Fibonacci numbers. "n" is the number of Fibonacci sequence.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache: #Check if the value is already in the cache
            return cache[n]
        cache[n] = fibonacci(n-1) + fibonacci(n-2) #Calculate the value and save it in the cache
        return cache[n] #Return the value
    return fibonacci #


#Create a fibonacci function using caching_fibonacci
fib = caching_fibonacci()

# Call fibonacci function with different values
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

        

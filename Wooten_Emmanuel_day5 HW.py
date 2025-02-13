'''Question 1: Solve the following problem: Write a function to find all prime numbers in a given range.'''

def find_primes(start, end):
    primes = []  
    
    for num in range(start, end + 1):  
        if num > 1:  
            is_prime = True  
            
            for i in range(2, num):  
                if num % i == 0:
                    is_prime = False  
                    break  
            
            if is_prime:  
                primes.append(num)

    return primes

# Test Cases
print(find_primes(10, 20))  
# Output: [11, 13, 17, 19]




'''Question 2: Research one real-world problem that was solved using Python and summarize it in 2-3 sentences.'''

#NASA uses Python to analyze space data.

## NASA leverages Python and machine learning to process and analyze astronomical images from space telescopes like the Hubble and James Webb. 
## Python libraries such as NumPy, SciPy, and Matplotlib help detect and classify galaxies, exoplanets, and cosmic events, allowing scientists to automate and speed up discoveries.



'''Write a function that takes a list of numbers and returns a new list with only the even numbers.'''

def filter_even_numbers(lst):
    even_numbers = []  

    for num in lst: 
        if num % 2 == 0:  
            even_numbers.append(num)  

    return even_numbers 

# Test Cases
print(filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))  
# Output: [2, 4, 6, 8]

print(filter_even_numbers([11, 23, 35, 47]))  
# Output: []


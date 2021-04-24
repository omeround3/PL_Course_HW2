""" 
Task #2 of the Programming Languages course.

@authors
Omer Lev-Ron
Sam Medina
"""

# Q1.1:
# This class returns an iterator for prime numbers
class PrimeList:
    # Constructor
    def __init__(self, max_num):
        self.max_num = max_num
        self.value = 2
        
    # Return Iterator
    def __iter__(self):
        return self

    # Check if a prime number
    def is_prime(self, num):
        while True:
            try:
                y = next(self)
                if num % y == 0:
                    return False

            except StopIteration:
                return True
    # Iterate over next nubmer
    def __next__(self):

        while self.value < self.max_num:
            divisors = PrimeList(int(self.value ** 0.5) + 1)  # recursion
            found = divisors.is_prime(self.value)
            self.value += 1
            if found:
                return self.value - 1

        raise StopIteration()

#  Test Class
test = PrimeList(100)
print('Q1.1:\n', *test, sep=",", end='\n\n')

# Q1.2:
# Generate an sequence of prime numbers up to max_number
def generator_primes(max_number):
    new_dict = {}
    num = 2
    while num < max_number - 1:
        if num not in new_dict:
            yield num   # Yields a new primt if it's not in the dictionary
            new_dict[num * num] = [num] # KEY is no a prime; VALUE is a prime
        else:   # if num not in new_dict; than append it as a KEY (not prime)
            for p in new_dict[num]:
                new_dict.setdefault(p + num, []).append(p)
        
        num += 1
        
#  Test Generator
gen = generator_primes(100)
print('Q1.2:')
for i in gen:
    print(i, end=',')
print()

# Q2:
n = 24
q2_list = [i for i in range(2,n + 1) if n % i == 0]
print('\nQ2:\n', q2_list,'\n')

# Q3:
# A function to check if a prime number
def is_prime(num):
    if num > 1:
        for i in range(2, num):
                if (num % i) == 0:
                   return 'Not Prime'
        return 'Prime'
    return 'Not Prime'

# Test function
n = 6
m = 24
q3_list = [is_prime(i)  for i in range(n,m)]
print('Q3:\n',q3_list,'\n')

# Q4:
# A Generator function that gets two integers and returns all the even numbers
# between the two integers, and whose unity digit is an integter product of the 
# number of tens
def generator_between_two_numbers(n, m):
    for i in range(n, m):
        if i < 10 and i % 2 == 0:
            yield i
        else:
            if i % 2 == 0 and ( i % 10) % (i // 10) == 0: # // is for floating the divide number.
                yield i

# Test Q4
print("Q4:")
for i in generator_between_two_numbers(15,36):
    print(i, end=',')
print()

# Q5:
# This function returns a dictionary with each char as KEY and the number
# of occurences of the char in the string as the VALUE
def check_even_and_numbers_of_chars(text):
     return { char:(text.count(char)) for char in text }
print('\nQ5:\n', check_even_and_numbers_of_chars("omer and sam"),'\n')

# Q6:
print('Q6.1:')
# A generator to compare chars indices of 2 strings
def generator_same_chars(str_1, str_2):
    for i in range(max(len(str_1),len(str_2))):
        if str_1[i] == str_2[i]:
            yield str_1[i]

# Test Q6.1
for i in generator_same_chars('loke', 'like'):
    print(i , end=',')
print('\n')

# This class returns an iterator that returns two chars at the same index of two strings
class TwoCharsItr():
    # Constructor
    def __init__(self, str_1, str_2):
        self.str_1 = str_1
        self.str_2 = str_2
        self.index = 0

    # Return Iterator
    def __iter__(self):
        return self

    # Iterate over strings
    def __next__(self):
        if self.index < len(self.str_2): 
            if self.str_1[self.index] == self.str_2[self.index]:
                result = self.str_1[self.index]
                self.index += 1
                return result
            self.index += 1
        else:
            # End of Iteration
            raise StopIteration
# Test Q6.2
test_itr = TwoCharsItr('loke', 'like')
print('Q6.2:')
for i in test_itr:
    if i is not None:
     print(i,',', end='')
print()

# Q7:
# This function gets two lists; a char list and an integers list.
# It retruns a string whose characters are sorted by the cooressponding indices of the lists
def list_of_chars_combine_with_numbers(list_chars, list_numbers):
    return "".join([char for _, char in sorted(zip(list_numbers, list_chars))])

# Test Q7
print('\nQ7 - Input String: sam --> Output String: ', list_of_chars_combine_with_numbers(['s','a','m'] , [2 , 1 , 0]),'\n')

# Q8:
print('Q8:')
# A generator function that generates all the numbers between the two given numbers
# in ascending order and then reverse them. After each iteration, the user can give a new input
# number. If the new number is positive, the function will continue from the last number to the 
# bigger number between the two.
# Else, if the user input nubmer is negative, the function will continue from the minimum number
# between the two.

def generator_two_numbers_loop(n, m):
    while(True): 
        for i in (range (min(n, m), max(n, m) + 1)):
            yield i
        from_max = max(n, m) - 1
        while from_max >= min(n, m):
            yield from_max
            from_max -= 1
        user_input = int(input("Next number? "))
        if user_input > 0:
            yield from generator_two_numbers_loop(max(n,m), user_input)
        else:
            yield from generator_two_numbers_loop(min(n,m), user_input)

# Test Q8's generator function
# for i in generator_two_numbers_loop(1,10):
#     print(i , end= ', ')


# Q9
# Sentences a,b,d are in seperate WORD file.
print('\nQ9:')
cars = ["Volvo" , "BMW" , "Ford" , "Mazda"]
it = iter(cars)
print(next(it))


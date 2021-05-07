""" 
Task #2 of the Programming Languages course.

@authors
Omer Lev-Ron
Sam Medina
"""

# Class - This class returns an iterator for prime numbers
def q1a(input_num):
	class PrimeSmallerThan:
		# Constructor
		def __init__(self, input_num):
			self.input_num = input_num
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
			while self.value < self.input_num:
				divisors = PrimeSmallerThan(int(self.value ** 0.5) + 1)  # recursion
				found = divisors.is_prime(self.value)
				self.value += 1
				if found:
					return self.value - 1

			raise StopIteration()

	instance = PrimeSmallerThan(input_num) # add parameters
	return instance

# Generator - Generate an sequence of prime numbers up to max_number
def q1b(input_num):
	new_dict = {}
	num = 2
	while num < input_num - 1:
		if num not in new_dict:
			yield num   # Yields a new primt if it's not in the dictionary
			new_dict[num * num] = [num] # KEY is no a prime; VALUE is a prime
		else:   # if num not in new_dict; than append it as a KEY (not prime)
			for p in new_dict[num]:
				new_dict.setdefault(p + num, []).append(p)
		num += 1

# List comprehension
def q2(n):
	return [i for i in range(2,n + 1) if n % i == 0]

# One line
# m - min, n - max; A function to check if a prime number
def q3(m, n):
	return ["prime" if 0 not in [num % i for i in range(2, int(num / 2) + 1)] else "not prime" for num in range(m, n)]

# Generator
# A Generator function that gets two integers and returns all the even numbers
# between the two integers, and whose unity digit is an integter product of the 
# number of tens
# m - min, n - max
def q4(m, n):
	for i in range(m, n):
		if i < 10 and i % 2 == 0:
			yield i
		else:
			if i % 2 == 0 and (i % 10) % (i // 10) == 0 and (i % 10) != 0: # // is for floating the divide number.
				yield i

# One line
# This function returns a dictionary with each char as KEY and the number
# of occurences of the char in the string as the VALUE
def q5(str):
	return {char:(str.count(char)) for char in str}

# Generator - A generator to compare chars indices of 2 strings
def q6a(str1, str2):
	for i in range(max(len(str1),len(str2))):
		if str1[i] == str2[i]:
			yield str1[i]

# Class - This class returns an iterator that returns two chars at the same index of two strings
def q6b(str1, str2):
	class StringsCompare: # add class functions
		# Constructor
		def __init__(self, str1, str2):
			self.str1 = str1
			self.str2 = str2
			self.index = 0

		# Return Iterator
		def __iter__(self):
			return self

		# Iterate over strings
		def __next__(self):
			if self.index < len(self.str2): 
				if self.str1[self.index] == self.str2[self.index]:
					result = self.str1[self.index]
					self.index += 1
					return result
				else:
					self.index += 1
			else:
				# End of Iteration
				raise StopIteration

	instance = StringsCompare(str1, str2) # add parameters
	return instance

# One line
def q7(char_list, index_list):
	return "".join([char for _, char in sorted(zip(index_list, char_list))])

# Generator
def q8a(a, b):
	while(True): 
		for i in (range(min(a, b), max(a, b) + 1)):
			yield i
		from_max = max(a, b) - 1
		while from_max >= min(a, b):
			yield from_max
			from_max -= 1

# q8a with user_choice
def q8b(a, b):
    index = a
    u_choice = 1
    while True:
        user_choice = yield index
        if user_choice :
            yield index
            u_choice = user_choice
        if u_choice < 0:
                if index is not a:
                    index = index - 1
        else:
            if u_choice > 0:
                if index is not b:
                        index = index + 1

# Remove the '#' to run the corresponding test
# Don't forget to fill in the parameters.
if __name__ == "__main__":
	# q1a #
	# print('q1a:')
	# input_num = 100
	# for num in q1a(input_num):
	# 	print(num, end=', ')
	# print()

	# q1b #
	# print('q1b:')
	# for num in q1b(100):
	# 	print(num, end=', ')
	# print()
	
	# q2 #
	# print('q2:')
	# print(q2(24))

	# q3 #
	# print('q3:')
	# print(q3(2, 14))

	# q4 #
	# print('q4:')
	# for c in q4(12, 45):
	# 	print(c, end=', ')
	# print()	

	# q5 #
	# print('q5:')
	# print(q5("this is a simple string"))
	
	# q6a #
	# print('q6a:')
	# for c in q6a("like", "love"):
	# 	print(c)

	# q6b #
	# print('q6b:')
	# for c in q6b("like", "love"):
	# 	if c:
	# 		print(c)	
	
	# q7 #
	# print('q7:')
	# print(q7(['a', 'h', 'f', 'e', 'y', 'u'], [1, 5, 3, 6, 2, 4]))
	
	# q8a #
	# print('q8a:')
	# for c in q8a(3, 11):
	# 	print(c, end= ', ')

	# q8b #
	print('q8b:')
	generator = q8b(3, 11)
	counter = 0

	for i in generator:
	 	if counter == 1:
	 		generator.send(32)
	 	if counter == 3:
	 		generator.send(-3)
	 	if counter == 6:
	 		generator.send(23)
	 	if counter == 8:
	 		generator.send(3)
	 	if counter == 10:
	 		generator.send(-13)
	 	if counter == 25:
	 		break
	 	print(i, end=', ')
	 	counter += 1

"""
/*	Turner Atwood
 *	10/1/18
 *	All About that Base [2.9] (https://open.kattis.com/problems/allaboutthatbase)
 *	Brute Force - try every equation in every base (1-36)
 */
"""

# Messy way to build the two maps (char->int) and (int->char)
POSSIBLE_BASES = [str(i) for i in range(1,10)] + [chr(i) for i in range(97,123)]
DIGIT_VALUES = {j:i+1  for i,j in enumerate(POSSIBLE_BASES)}
DIGIT_VALUES['0'] = 0
POSSIBLE_BASES = {i+1:j for i,j in enumerate(POSSIBLE_BASES)}
POSSIBLE_BASES[36] = '0'

# Go from a number string (in a given base) to decimal integer
def _str_base_to_decimal(base, number_str):
	power = 1
	total = 0
	# Bases one is just tally marks
	if (base  == 1):
		if not set(number_str) == {'1'}:
			return -1
		return len(number_str)

	# Normal base conversion (2-35)
	for digit in number_str[::-1]:
		digit_value = DIGIT_VALUES[digit]
		if base <= digit_value:
			return -1
		total += power * digit_value
		power *= base

	return total 

# Take string operators and perform their operations
def _perform_operation(num_a, num_b, op):
	if op == "+":
		result = num_a + num_b
	elif op == "-":
		result = num_a - num_b
	elif op == "*":
		result = num_a * num_b
	else:
		result = num_a / num_b
	return result

# Find all the bases for which the proposed operations are valid
def main():
	num_cases = int(input())
	for _ in range(num_cases):
		in_line = input().split(" ")
		nums = in_line[::2]
		op = in_line[1]
		found_bases = []

		# Try all of the bases
		for base in POSSIBLE_BASES:
			num_in_decimal = [_str_base_to_decimal(base, num) for num in nums]
			result = _perform_operation(num_in_decimal[0], num_in_decimal[1], op)
			# At least one number not interpretable in this base
			if -1 in num_in_decimal:
				continue
			# The result does not match the calculated result
			elif not result == num_in_decimal[2]:
				continue
			else:
				found_bases.append(POSSIBLE_BASES[base])
		
		# Output
		if not found_bases:
			print("invalid")
		else: 
			print("".join(found_bases))

if __name__ == "__main__":
	main()

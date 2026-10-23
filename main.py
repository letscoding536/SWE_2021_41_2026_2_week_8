from typing import List

def even_list(int_list: List[int]) -> List[int]:
	even_int_list = []

	for n in int_list:
		if n % 2 == 0:
			even_int_list.append(n)

	return even_int_list

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
	total = 0

	for n in even_int_list:
		total += n ** 2

	return total


def main():
	int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	even_int_list = even_list(int_list)
	output = sum_of_squares_of_even(even_int_list)
	print(output)


if __name__ == "__main__":
	main()

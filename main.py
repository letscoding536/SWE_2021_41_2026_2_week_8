from typing import List

def even_list(int_list: List[int]) -> List[int]:
	even_int_list = []

	for n in int_list:
		if n % 2 == 0:
			even_int_list.append(n)

	return even_int_list

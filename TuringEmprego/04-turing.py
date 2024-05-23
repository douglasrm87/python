def solution(n: int, m: int, k) -> bool:
	# write your solution here
	return False


# R E A D M E
# DO NOT CHANGE the code below, we use it to grade your submission. If changed your submission will be failed automatically.
if __name__ == "__main__":
	n = int(input())
	m = int(input())
	mtx = [[int(val) for val in pair.split()] for pair in input().strip().split(',')]

	output = solution(n, m, mtx)
	if output == True:
		print("true")
	else:
		print("false")
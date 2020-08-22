def cycle(end, incr):
	a = 0
	nums = []
	while a < end:
		print(a)
		nums.append(a)
		a += incr

	print('Значения списка nums:')
	for b in nums:
		print(b)

cycle(10, 2)
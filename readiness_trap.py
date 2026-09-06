def mean_and_max(*numbers):
	mean = sum(numbers) / len(numbers)
	return mean, max(numbers)


print("Hello, I am Tyler J Trapani, and my student ID is R01886666.")

sample_numbers = [3, 7, 2, 9, 5]
mean, maximum = mean_and_max(*sample_numbers)
print(f"Mean: {mean}, Maximum: {maximum}")

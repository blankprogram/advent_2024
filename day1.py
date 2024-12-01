from collections import Counter

with open("day1in.txt", 'r') as file:
    lines = [line.split() for line in file if line.strip()]
    left_list = [int(pair[0]) for pair in lines]
    right_list = [int(pair[1]) for pair in lines]

sorted_left = sorted(left_list)
sorted_right = sorted(right_list)

total_distance = sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))

count_right = Counter(right_list)
similarity = sum(x  * count_right[x] for x in left_list)

print(f'similarity: {similarity}')
print(f'distance: {total_distance}')

import random
from collections import Counter

counts = {0: 2845, 1: 2575, 2: 2197, 3: 2756, 4: 4518, 5: 4585, 6: 2703, 7:3491}  

def generate_label_pairs(total_lines, counts):
    col1 = []
    for num, count in counts.items():
        col1.extend([num] * count)

    remaining = total_lines - len(col1)
    col1.extend(random.choices(list(counts.keys()), k=remaining))

    random.shuffle(col1)

    col2 = []
    for num in col1:
        choices = [x for x in range(8) if x != num] 
        col2.append(random.choice(choices))

    return list(zip(col1, col2))

total_lines = 45000

label_pairs = generate_label_pairs(total_lines, counts)

col1_counter = Counter(pair[0] for pair in label_pairs)
col2_distribution = {num: Counter(pair[1] for pair in label_pairs if pair[0] == num) for num in counts.keys()}

output_file = "train_label_pair.txt"
with open(output_file, "w") as f:
    for pair in label_pairs:
        f.write(f"{pair[0]} {pair[1]}\n")

print(f"File '{output_file}' đã được tạo thành công!")
print("Phân bố cột 1:", col1_counter)
print("Phân bố cột 2 theo từng loại số ở cột 1:")
for num, dist in col2_distribution.items():
    print(f"  Số {num}: {dict(dist)}")

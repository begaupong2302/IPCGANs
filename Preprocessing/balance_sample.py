import random

# reduce
input_file = "../../Exdata2/lists/train_age_group_1.txt"
output_file = "../../Exdata2/lists/train_age_group_1.txt"

def reduce_file_lines(input_file, output_file, target_lines=4000):
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()

        if len(lines) <= target_lines:
            return

        reduced_lines = random.sample(lines, target_lines)
        with open(output_file, "w") as f:
            f.writelines(reduced_lines)

        print(f"old: {target_lines}, new: {output_file}")

    except Exception as e:
        print(f"{e}")

reduce_file_lines(input_file, output_file)


# duplicate and shuffle
input_file = "../../Exdata2/lists/train_age_group_3.txt"
output_file = "../../Exdata2/lists/train_age_group_3.txt"

def duplicate_and_shuffle_lines(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()

        original_line_count = len(lines)
        print(f"old:{original_line_count}")

        doubled_lines = lines * 2
        random.shuffle(doubled_lines)

        with open(output_file, "w") as f:
            f.writelines(doubled_lines)

        print(f"new {len(doubled_lines)}. save: {output_file}")

    except Exception as e:
        print(f"{e}")

duplicate_and_shuffle_lines(input_file, output_file)

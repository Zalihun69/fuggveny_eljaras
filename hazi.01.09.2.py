import random
sample_list = []
for i in range(10):
    sample_list.append(random.randint(1, 1000))


def harommal_oszthatok(numbers):
    count = sum(1 for number in numbers if number % 3 == 0)
    return count


result = harommal_oszthatok(sample_list)
print(f"A listában {result} darab hárommal osztható szám található.")

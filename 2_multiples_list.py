factor = int(input())
count = int(input())
initial_factor = factor
sequence = []
for _ in range(count):
    sequence.append(factor)
    factor += initial_factor
print(sequence)


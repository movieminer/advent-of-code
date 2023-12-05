
with open("day1/input.txt", "r") as f:
  lines = f.readlines()

numbers = [[int(n) for n in line if n.isdigit()] for line in lines]
added = [number[0]*10 + number[-1] for number in numbers]
print(added)
value = sum(added)

print(f"sum of calibration inputs: {value}")
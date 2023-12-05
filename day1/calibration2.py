
with open("day1/input.txt", "r") as f:
  lines = f.readlines()

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

lines_new = []
for line in lines:
    numb = []
    for l in range(len(line)):
      if line[l].isdigit():
         numb.append(int(line[l]))
      for d in digits:
        if l+len(d)<=len(line) and d in line[l:l+len(d)]:
           numb.append(digits.index(d)+1)
    lines_new.append(numb)

print(lines_new)

added = [number[0]*10 + number[-1] for number in lines_new]
print(added)
value = sum(added)

print(f"sum of calibration inputs: {value}")